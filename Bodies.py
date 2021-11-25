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