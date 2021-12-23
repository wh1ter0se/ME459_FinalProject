Welcome to ME459_FinalProject's documentation!
==============================================

.. toctree::
   :maxdepth: 4
   :caption: Contents:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
* `FEAFunctions.py`
* `Bodies.py`


FEAFunctions.py
================

Solve_SimpleAxialTension()
----------------------------

   This is from the first simple example.
   It solves setup given EITHER force (N) or displacement (m).
   Force and displacement are both numpy column vectors.
   Positive values correlate with tension.

   Args:
      * workpiece: The workpiece object storing object parameters to be tested
      * force: The force on the unfixed end in Newtons (optional)
      * displacement: The axial displacement on the unfixed end in Meters (optional)
      * verbose: True if data should be printed (default true)

   Returns:
      * List of data columns in the following order: [force, displacement, strain, stress]

Solve_MultipleAxialTension()
------------------------------

   Allows you to solve for local/global displacement, given pairs of locations and forces. 
   The area is assumed to be the same along the entire piece. 
   Positive values correlate with tension.

   Args:
      * workpiece: The workpiece object storing object parameters to be tested
      * force_pos_pairs: An array of (node,force) tuples
      * nodes: The number of discrete chunks to calculate
      * verbose: True if data should be printed (default true)

   Returns:
      * List of data columns in the following order: [force, displacement, strain, stress]

Solve_SimpleCantileverDeflection()
-----------------------------------

   Solves for cantilever deflection (fixed at one end, free at the other). 
   Displacement is perpendicular rather than parallel (as in tension). 
   All forces/displacements are on the free end of the workpiece.

   Args:
      * workpiece: The workpiece object storing object parameters to be tested
      * force: The force on the unfixed end in Newtons (optional)
      * displacement: The lateral displacement on the unfixed end in Meters (optional)
      * verbose: True if data should be printed (default true)



Bodies.py
==========


Workpiece (Class)
----------------

   Stores the modulus of elasticity, length, area, and area moment of inertia of a workpiece.

__init__()
**********

   Args:
      * modulus: the modulus of elasticity of the chosen material
      * area: cross-sectional area of the workpiece (m^2)
      * length: length of the workpiece (m)
      * I_xx: area moment of inertia with respect to x (m^4)
      * I_yy: area moment of inertia with respect to y (m^4)

summary()
**********

   Prints the modulus, area, I_xx, and I_yy of the workpiece.


Rod (Class)
----------------

   Subclass of Workpiece. Generates a cylindrical rod.

__init__()
**********

   Args:
      * modulus: the modulus of elasticity of the chosen material
      * radius: radius of the workpiece (m)
      * length: length of the workpiece (m)

summary()
**********

   Prints the summary from the superclass. Prints the radius.


SquarePrism (Class)
----------------

   Subclass of Workpiece. Generates a square prism.

__init__()
**********

   Args:
      * modulus: the modulus of elasticity of the chosen material
      * width: width of the workpiece (m)
      * length: length of the workpiece (m)

summary()
**********

   Prints the summary from the superclass. Prints the width.


RectangularPrism (Class)
----------------

   Subclass of Workpiece. Generates a rectangular prism.

__init__()
**********

   Args:
      * modulus: the modulus of elasticity of the chosen material
      * base: base width of the workpiece (m)
      * height: height of the workpiece (m)
      * length: length of the workpiece (m)

summary()
**********

   Prints the summary from the superclass. Prints the base width and height.