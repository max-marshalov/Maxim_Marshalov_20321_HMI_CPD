##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-01 7:53:36 pm
 # @copyright SMTU
 #
import asyncio
class AsyncService:
    def __init__(self,app, interval=1/20) -> None:
        '''В этом классе выполняются все асинхронные процессы'''
        self.__interval = interval
        self.__tasks = []
        self.__app = app
        self.__loop = self.__app.loop
        self.__app.protocol("WM_DELETE_WINDOW", self.close)
        self.__process_window_controller = self.__app.process_window.process_controller
        self.__os_service = self.__process_window_controller.os_processes_service

        self.__tasks.append(self.__loop.create_task(self.processes_updater()))
        self.semaphore = asyncio.Semaphore(5)
    

    async def processes_updater(self):
         async with self.semaphore:
            await self.semaphore.acquire()
            try:
                 self.__app.update()
                 self.__process_window_controller.add_processes()
            finally:
                self.semaphore.release()
         while True:
            try:
                if self.__os_service.sort_flag != self.__os_service.old_flag:
                    self.semaphore = asyncio.Semaphore(5)
                    async with self.semaphore:
                        await self.semaphore.acquire()
                        try:
                            self.processes_sorter()
                        finally:
                            self.semaphore.release()
                self.__process_window_controller.update_processes()
                self.__app.update()
                await asyncio.sleep(self.__interval)
            except Exception as e:
                print(e)
    
    def processes_sorter(self):
            try:
                    self.__app.process_window.table.delete(*self.__app.process_window.table.get_children())
                    self.__os_service.procs.clear()
                    self.__process_window_controller.add_processes()
                    self.__os_service.change_old_flag()
            except Exception as e:
                print(e)

    def close(self):
        for task in self.__tasks:
            task.cancel()
        self.__loop.stop()
        self.__app.destroy()
        exit()
