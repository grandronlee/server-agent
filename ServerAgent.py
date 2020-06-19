import configparser
import wmi
import csv
import logging
import logging.handlers
import os
import sys
from ServerObj import ServerObj
from Storage import *

path_current_directory = os.path.dirname(__file__)
path_config_file = os.path.join(path_current_directory, 'config.ini')
config = configparser.ConfigParser()
config.read(path_config_file)

console_handler = logging.StreamHandler(sys.stdout)
logfile = os.path.join(path_current_directory, 'log', config['Default']['logFile'])
os.makedirs(os.path.dirname(logfile), exist_ok=True)
logging.basicConfig(filename=logfile, filemode='w', level=logging.DEBUG)
log = logging.getLogger("serveragent")
log.addHandler(console_handler)

log.info(path_config_file)

servers = []
serverList = config['Default']['serverList']
serversFile = os.path.join(path_current_directory, 'csv', config['Default']['serverCSV'])
serverDisksFile = os.path.join(path_current_directory, 'csv', config['Default']['serverDisksCSV'])
os.makedirs(os.path.dirname(serversFile), exist_ok=True)
os.makedirs(os.path.dirname(serverDisksFile), exist_ok=True)
serverNames = serverList.split(',')

for serverName in serverNames:
  try:
    conn = wmi.WMI(serverName, user=config['Default']['wmiUser'], password=config['Default']['wmiPwd'])
    log.info('Connected: ' + serverName)
    cs = conn.Win32_ComputerSystem()
    os = conn.Win32_OperatingSystem()
    memTotal = int(int(cs[0].TotalPhysicalMemory)/1024/1024)
    memFree = int(int(os[0].FreePhysicalMemory)/1024)
    server = ServerObj()
    server.name = serverName
    server.os = os[0].Caption
    server.totalPhysicalMemory = memTotal
    server.freePhysicalMemory = memFree  

    for disk in conn.Win32_LogicalDisk (DriveType=3):    
        d = {"ID": disk.DeviceID, "DiskSize": format(int(disk.Size)/1000000000,'.2f'), "DiskFreeSpace": format(int(disk.FreeSpace)/1000000000,'.2f')}
        server.disks.append(d)
  
    servers.append(server)
  except Exception as e:
      log.error(e)
  

fieldnames = ("Server", "OS","Total Physical Memory MB", "Free Physical Memory MB", "Date")
Storage.csvFileHeader(serversFile, fieldnames)
fieldnames = ("Server", "Disk ID","Disk Size GB", "Disk Free Space GB", "Date")
Storage.csvFileHeader(serverDisksFile, fieldnames)

Storage.csv(servers,serversFile,serverDisksFile)
