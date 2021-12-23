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