#0-SECURITIES
%%writefile ../implementations/securitySolution.py 
#Uncomment line above & run cell to save solution
#TODO Define class that implements securityInterface & allows for the management of a security
import ipytest
#import securityInterface

from interfaces.securityInterface import securityInterface

class security(securityInterface):
    def __init__(self, name):
        self.name = name
    
    def getName(self) -> str:
        return self.name

