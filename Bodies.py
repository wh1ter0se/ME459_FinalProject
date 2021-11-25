import math
from enum import Enum

class WorkPiece():
    # Modulus = modulus of elasticity (Pa)
    # Area, length given in SI units (m^2,m)
    def __init__(self,modulus,area,length):
        self.modulus = modulus
        self.area = area
        self.length = length

class Rod(WorkPiece):
    def __init__(self,modulus,radius,length):
        area = math.pi * (radius**2)
        super().__init__(modulus,area,length)

class Prism(WorkPiece):
    def __init__(self,modulus,width,length):
        area = width ** 2
        super().__init__(modulus,area,length)

