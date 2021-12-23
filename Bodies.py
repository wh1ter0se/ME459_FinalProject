import math
from enum import Enum

class Workpiece():
    # Modulus = modulus of elasticity (Pa)
    # Area, length given in SI units (m^2,m)
    def __init__(self,modulus,area,length,I_xx,I_yy):
        self.modulus = modulus
        self.area = area
        self.length = length
        self.I_xx = I_xx
        self.I_yy = I_yy

    def summary(self):
        print('Young\'s Modulus (Pa): ' + str(self.modulus))
        print('Cross-sectional Area (m^2): ' + str(self.area))
        print('Length (m): ' + str(self.length))
        print('I_xx (m^4): ' + str(self.I_xx))
        print('I_yy (m^4): ' + str(self.I_yy))

class Rod(Workpiece):
    def __init__(self,modulus,radius,length,*args):
        area = math.pi * (radius**2)
        I_xx = (math.pi * radius**2) / 16 # Ixx = (pi*D^2)/64
        I_yy = I_xx
        self.radius = radius
        super().__init__(modulus,area,length,I_xx,I_yy)
    
    def summary(self):
        super().summary()
        print('Radius (m): ' + str(self.radius))

class SquarePrism(Workpiece):
    def __init__(self,modulus,width,length,*args):
        area = width ** 2
        I_xx = (width**4) / 12 # Ixx = bh^3 / 12
        I_yy = I_xx
        super().__init__(modulus,area,length,I_xx,I_yy)

    def summary(self):
       super().summary()
       print('Width (m): ' + str(self.width))


class RectangularPrism(Workpiece):
    def __init__(self,modulus,base,height,length,*args):
        area = base * height
        I_xx = (base * (height**3)) / 12 # Ixx = bh^3 / 12
        I_yy = (height * (base**3)) / 12 # Iyy = hb^3 / 12
        super().__init__(modulus,area,length,I_xx,I_yy)

    def summary(self):
       super().summary()
       print('Base (m): ' + str(self.base))
       print('Height (m): ' + str(self.height))

# All elastic moduli given in Pa
# (MPa = 10^6 Pa, GPa = 10^9 Pa)
class Elasticity(Enum):
    # All woods use modulus at 12% moisture grade
    # and are measured along longitudinal axis.
    # https://amesweb.info/Materials/Youngs-Modulus-of-Wood.aspx
    BIRCH     = 13900 * 10**6
    MAPLE     = 12600 * 10**6
    OAK_RED   = 12500 * 10**6
    OAK_WHITE = 12300 * 10**6
    PINE_RED  = 11200 * 10**6
    WALNUT    = 12600 * 10**6

    # Metal/plastic axis doesn't matter due to isotropy.
    # Average of high/low is used if a range is given.
    # https://www.engineeringtoolbox.com/young-modulus-d_417.html
    ABS       = 2.25  * 10**9  # 1.4-3.1 GPa
    ALUMINUM  = 69    * 10**9
    BRASS     = 113.5 * 10**9  # 102-125 GPa
    CONCRETE  = 17    * 10**9
    COPPER    = 117   * 10**9
    GLASS     = 70    * 10**9  # 50-90 GPa
    HDPE      = 0.8   * 10**9
    IRON      = 210   * 10**9
    LEAD      = 13.8  * 10**9
    MDF       = 4     * 10**9
    NICKEL    = 170   * 10**9
    PLATINUM  = 147   * 10**9
    PVC       = 3.25  * 10**9  # 2.4-4.1 GPa
    SILVER    = 72    * 10**9
    STEEL_A36 = 200   * 10**9
    TIN       = 47    * 10**9
    TITANIUM  = 112.5 * 10**9  # Titanium Alloy, 105-120 GPa

piecetypes = [Rod,
              SquarePrism,
              RectangularPrism]