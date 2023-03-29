# -*- coding: utf-8 -*-


"""
Component TetrahedronSetTopologyContainer

.. autofunction:: TetrahedronSetTopologyContainer

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TetrahedronSetTopologyContainer(attachedTo , name='TetrahedronSetTopologyContainer', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, filename='', position=array([], shape=(0, 3), dtype=float64), checkTopology=0, nbPoints=0, edges=array([], shape=(0, 2), dtype=int32), checkConnexity=0, triangles=array([], shape=(0, 3), dtype=int32), createTriangleArray=0, tetrahedra=array([], shape=(0, 4), dtype=int32), **kwargs):
    """Tetrahedron set topology container


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 filename: Filename of the mesh

		 position: Initial position of points

		 checkTopology: Parameter to activate internal topology checks (might slow down the simulation)

		 nbPoints: Number of points

		 edges: List of edge indices

		 checkConnexity: It true, will check the connexity of the mesh.

		 triangles: List of triangle indices

		 createTriangleArray: Force the creation of a set of triangles associated with each tetrahedron

		 tetrahedra: List of tetrahedron indices


    """
    return attachedTo.createObject("TetrahedronSetTopologyContainer" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, filename=filename, position=position, checkTopology=checkTopology, nbPoints=nbPoints, edges=edges, checkConnexity=checkConnexity, triangles=triangles, createTriangleArray=createTriangleArray, tetrahedra=tetrahedra, **kwargs)
