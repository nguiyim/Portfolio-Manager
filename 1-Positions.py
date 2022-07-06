#Run this cell before running the your testing cell. This will setup the ipytest cell magic command. If you're running this notebook locally you may need to install ipytest from pip or conda
#1-POSITIONS
#%conda install ipytest
#%pip install ipytest
import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
    
import ipytest
from interfaces.securityInterface import securityInterface
from interfaces.positionInterface import positionInterface
from implementations import securitySolution


#Allow for a position to be created with a security name or object and a seed position value
#Allow for gathering of the position's security and position value
#Allow for updating of the position's size via addition & setting

class positionInterface():
    def __init__(self, securityIn, initialPosition: int):
        self.name = name
        self.security = securityIn
        
        if  isinstance()
        
        self.security= 

    def getSecurity(self) -> securityInterface:
        pass

    def getPosition(self) -> int:
        pass
    
    def setPosition(self, inputValue: int) -> None:
        pass
    
    def addPosition(self, inputValue: int) -> None:
        pass
ipytest.autoconfig()