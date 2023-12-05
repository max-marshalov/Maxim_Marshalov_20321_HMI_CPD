##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-01 7:31:58 pm
 # @copyright SMTU
 #
import psutil
class OsProcessesService:
    def __init__(self) -> None:
        '''Сервис для получения информации о процессах от OC'''
        self.__cpu_count = psutil.cpu_count()
        self.__cpu_percent = psutil.cpu_percent()
        self.__memory_usage = psutil.virtual_memory().percent
        self.__virtual_memory = psutil.virtual_memory().total
        self.__disk_usage = psutil.disk_usage('/').percent
        self.__netio = psutil.net_io_counters(pernic=True)
        self.__network_upload = self.__netio['Ethernet'].bytes_sent/8
        self.__network_download = self.__netio['Ethernet'].bytes_recv/8
        self.__sort_flag = 'pid'
        self.__cpu_data = []
        self.__mem_data =[]
        self.__disk_data= []
        self.__nw_upload_data = []
        self.__nw_download_data = []
        self.__old_flag = self.__sort_flag
        self.__procs = []

    def __get_processes(self):
        '''Возвращает информацию о процессах в виде словаря'''
        return psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_percent', "connections"])
    
    def get_sort_processes(self):
        try:
            return sorted(self.__get_processes(), key=lambda p : p.info[self.__sort_flag], reverse=True)
        except Exception as e:
            print(e)
    def get_processes_names(self):
        return psutil.process_iter(attrs=['name'])
    def change_old_flag(self):
        self.__old_flag = self.sort_flag
    
    def change_sort_flag(self, value:str):
        self.sort_flag = value
    
    def values_as_dict(self):
        self.__cpu_data.append(self.__cpu_percent)
        self.__mem_data.append(self.__memory_usage)
        self.__disk_data.append(self.__disk_usage)
        self.__nw_download_data.append(self.__network_download)
        self.__nw_upload_data.append(self.__network_upload)
        return {"CPU":self.cpu_data, "Memory":self.mem_data, "Disk usage":self.disk_data, "Network Dowload":self.nw_download_data, "Network Upload":self.nw_download_data}
    
    def kill(self, pid):
        '''Метод удаления процесса'''
        try:
            p = psutil.Process(pid)
            p.terminate()
            p.wait()
            self.procs.remove(pid)
        except Exception as e:
            pass
    
    @property
    def procs(self):
         return self.__procs
    @property
    def cpu_count(self):
        return self.__cpu_count
    
    @property
    def virtual_memory(self):
        return self.__virtual_memory
     
    
    @property
    def sort_flag(self):
        return self.__sort_flag
    
    @sort_flag.setter
    def sort_flag(self, value):
        self.__sort_flag = value
    
    @property
    def old_flag(self):
        return self.__old_flag
    
    @property
    def network_upload(self):
        return self.__network_upload
    @property
    def network_download(self):
        return self.__network_download
    @property
    def disk_usage(self):
        return self.__disk_usage
    
    @property
    def cpu_data(self):
        return self.__cpu_data
    @property
    def mem_data(self):
        return self.__mem_data
    @property
    def disk_data(self):
        return self.__disk_data
    @property
    def nw_download_data(self):
        return self.__nw_download_data
    @property
    def nw_upload_data(self):
        return self.__nw_upload_data