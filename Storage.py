import csv
import datetime
import logging

class Storage:
    """Storage class for saving data"""    

    def csvFileHeader(file, fieldnames):
        with open(file, 'a+', newline='') as csvfile: pass
        headers = ''
        with open(file) as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader, None)  # returns the headers or `None` if the input is empty
            
        if headers is None:
            with open(file, 'a+', newline='') as csvfile:                
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

    def csv(servers, serversFile,serverDisksFile):
        log = logging.getLogger("serveragent")
        for server in servers:
            log.info('Name: ' + server.name)
            log.info('OS: ' + server.os)
            log.info('memTotal: ' + str(server.totalPhysicalMemory)+'Mb')
            log.info('memFree: ' + str(server.freePhysicalMemory)+'Mb')

            date = datetime.datetime.now()
            dt = date.strftime("%Y-%m-%d %H:%M:%S")
            log.info('Date: ' + dt)
            with open(serversFile, 'a+', newline='') as csvfile:                
                writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([server.name, server.os, server.totalPhysicalMemory, server.freePhysicalMemory, dt])

            for disk in server.disks:
                log.info(disk["ID"] + 'DiskSize: ' + str(disk["DiskSize"])+'Gb')
                log.info(disk["ID"] + 'DiskFreeSpace: ' + str(disk["DiskFreeSpace"])+'Gb')
                with open(serverDisksFile, 'a+', newline='') as csvfile:                
                    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([server.name, disk["ID"], disk["DiskSize"], disk["DiskFreeSpace"], dt])
