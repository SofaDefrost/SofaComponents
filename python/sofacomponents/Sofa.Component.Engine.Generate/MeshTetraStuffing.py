# -*- coding: utf-8 -*-


"""
Component MeshTetraStuffing

.. autofunction:: MeshTetraStuffing

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MeshTetraStuffing(attachedTo , name='MeshTetraStuffing', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, vbbox=array([[0., 0., 0.],
       [0., 0., 0.]]), size=-8.0, inputPoints=array([], shape=(0, 3), dtype=float64), inputTriangles=array([], shape=(0, 3), dtype=int32), inputQuads=array([], shape=(0, 4), dtype=int32), outputPoints=array([], shape=(0, 3), dtype=float64), outputTetrahedra=array([], shape=(0, 4), dtype=int32), alphaLong=0.24999, alphaShort=0.42978, snapPoints=0, splitTetrahedra=0, draw=0, **kwargs):
    """Create a tetrahedral volume mesh from a surface, using the algorithm from F. Labelle and J.R. Shewchuk, "Isosurface Stuffing: Fast Tetrahedral Meshes with Good Dihedral Angles", SIGGRAPH 2007.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 vbbox: BBox to restrict the volume to

		 size: Size of the generate tetrahedra. If negative, number of grid cells in the largest bbox dimension

		 inputPoints: Input surface mesh points

		 inputTriangles: Input surface mesh triangles

		 inputQuads: Input surface mesh quads

		 outputPoints: Output volume mesh points

		 outputTetrahedra: Output volume mesh tetrahedra

		 alphaLong: Minimum alpha values on long edges when snapping points

		 alphaShort: Minimum alpha values on short edges when snapping points

		 snapPoints: Snap points to the surface if intersections on edges are closed to given alpha values

		 splitTetrahedra: Split tetrahedra crossing the surface

		 draw: Activate rendering of internal datasets


    """
    return attachedTo.createObject("MeshTetraStuffing" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, vbbox=vbbox, size=size, inputPoints=inputPoints, inputTriangles=inputTriangles, inputQuads=inputQuads, outputPoints=outputPoints, outputTetrahedra=outputTetrahedra, alphaLong=alphaLong, alphaShort=alphaShort, snapPoints=snapPoints, splitTetrahedra=splitTetrahedra, draw=draw, **kwargs)
