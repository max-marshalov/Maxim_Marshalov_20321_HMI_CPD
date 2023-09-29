# https://metanit.com/python/tkinter/4.1.php

import tkinter as tk
from tkinter import ttk
import psutil
import time
import asyncio


class App(tk.Tk):
    def __init__(self, loop, interval=1/20):
        super().__init__()
        self.loop = loop
        self.title("TSKMNGR")
        self.geometry("600x600")
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.tasks = []
        self.sort_flag = 'memory_percent'
        self.old_flag = 'memory_percent'
        self.procs = []
        self.tasks.append(loop.create_task(self.updater(interval)))
        self.tasks.append(loop.create_task(self.sort_processes(interval)))
        #Инициализация окон
       
     # self.processes_widget = ttk.Widget(self, widgetname="processes")
        # #self.performance_frame = ttk.Frame(self, height=600)
        # self.processes_widget.pack(self, side="top", expand=True)
        
        
        self.processes = psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_percent'])
        self.sorted_processes = sorted(self.processes, key=lambda p : p.info[self.sort_flag], reverse=True)
        # Настройка Scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient="vertical")
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        # Создание Treeview
        self.tree = ttk.Treeview(self, columns=("PID", "Name", "CPU", "Memory"), yscrollcommand=self.scrollbar.set, show="headings") # yscrollcommand=self.scrollbar.set
        self.tree.heading("PID", text="PID", command=lambda: self.change_flag('pid'))
        self.tree.heading("Name", text="Name", command= lambda: self.change_flag('name'))
        self.tree.heading("CPU", text="CPU", command= lambda: self.change_flag('cpu_percent'))
        self.tree.heading("Memory", text="Memory", command=lambda:self.change_flag('memory_percent'))

        self.tree.column("PID", width=150)
        self.tree.column("Name", width=150)
        self.tree.column("CPU", width=150)
        self.tree.column("Memory", width=150)
        self.tree.grid(row=0, column=0, sticky="nsew")

        # Связываем полосу прокрутки с Treeview
        self.scrollbar.config(command=self.tree.yview) # Метод yview управляет вертикальной прокруткой в Treeview.

        # Кнопка удаления
        self.delete_button = ttk.Button(self, text="Delete Process", command=self.delete_selected)
        self.delete_button.grid(row=1, column=0, columnspan=2, pady=20)

        #Меню бар
        self.main_menu = tk.Menu(self)
        self.config(menu=self.main_menu)
        self.processes_menu = tk.Menu(self.main_menu, tearoff=0)
        self.performance_menu = tk.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label='Процессы', menu=self.processes_menu)
        self.main_menu.add_cascade(label='Производительность', menu=self.performance_menu)
        # Задаем вес столбцов и строк, чтобы Treeview мог растягиваться
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.add_processes()
    async def updater(self, interval):
        while True:
            self.update_processes()
            self.update()
            await asyncio.sleep(interval)
        
    def change_flag(self, flag):
        self.sort_flag = flag
        
    def delete_selected(self):
        selected_items = self.tree.selection()
        for item in selected_items:
            try:
                proc_pid = self.tree.item(item)['values'][0]
                p = psutil.Process(proc_pid)
                p.terminate()
                p.wait()
                self.tree.delete(item)
                self.procs.remove(proc_pid)
            except Exception as e:
                print(e)
            
    def add_processes(self):
        #self.tree.delete(*self.tree.get_children())
        for i in range(len(self.sorted_processes)):
            self.tree.insert("", tk.END, values = (f"{self.sorted_processes[i].info['pid']}", f"{self.sorted_processes[i].info['name']}", f"{self.sorted_processes[i].info['cpu_percent']}", f"{float(self.sorted_processes[i].info['memory_percent']) / 100 * float(psutil.virtual_memory().total)}"))
            self.procs.append(self.sorted_processes[i].info['pid'])

    def update_processes(self):
        for i in range(len(self.sorted_processes)):
                item = self.tree.get_children()[i]
                if(self.tree.item(item)['values'][0] == self.sorted_processes[i].info['pid']):
                    self.tree.item(item, values = (f"{self.sorted_processes[i].info['pid']}", f"{self.sorted_processes[i].info['name']}", f"{self.sorted_processes[i].info['cpu_percent']}", f"{float(self.sorted_processes[i].info['memory_percent']) / 100 * float(psutil.virtual_memory().total)}"))
                elif self.sorted_processes[i].info['pid'] not in self.procs:
                    self.tree.insert("", tk.END, values = (f"{self.sorted_processes[i].info['pid']}", f"{self.sorted_processes[i].info['name']}", f"{self.sorted_processes[i].info['cpu_percent']}", f"{float(self.sorted_processes[i].info['memory_percent']) / 100 * float(psutil.virtual_memory().total)}"))
                    self.procs.append(self.sorted_processes[i].info['pid'])
                    
    async def sort_processes(self, interval):
        while True:
            if(self.old_flag == self.sort_flag):
                self.processes = psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_percent'])
                self.sorted_processes = sorted(self.processes, key=lambda p : p.info[self.old_flag], reverse=True)
            else:
                self.tree.delete(*self.tree.get_children())
                self.procs.clear()
                self.processes = psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_percent'])
                self.sorted_processes = sorted(self.processes, key=lambda p : p.info[self.sort_flag], reverse=True)
                self.add_processes()
                self.old_flag = self.sort_flag
            await asyncio.sleep(interval)

    def close(self):
        for task in self.tasks:
            task.cancel()
        self.loop.stop()
        self.destroy()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    app = App(loop)
    try:
        loop.run_forever()
    except Exception as e:
        loop.close()
        print(e)
