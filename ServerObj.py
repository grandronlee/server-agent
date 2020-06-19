class ServerObj:
    """Server class"""
    def __init__(self):
        self._name = ''
        self._totalPhysicalMemory = 0
        self._freePhysicalMemory = 0
        self._disks = []
    
    @property
    def name(self):          
        return self._name 
       
    @name.setter 
    def name(self, n): 
        self._name = n 

    @property
    def os(self):          
        return self._os 
       
    @os.setter 
    def os(self, o): 
        self._os = o

    @property
    def totalPhysicalMemory(self):          
        return self._totalPhysicalMemory 
       
    @totalPhysicalMemory.setter 
    def totalPhysicalMemory(self, tpm): 
        self._totalPhysicalMemory = tpm 

    @property
    def freePhysicalMemory(self):          
        return self._freePhysicalMemory 
       
    @freePhysicalMemory.setter 
    def freePhysicalMemory(self, fpm): 
        self._freePhysicalMemory = fpm
    
    @property
    def disks(self):          
        return self._disks 
       
    @disks.setter 
    def disks(self, d): 
        self._disks = d