# -*- coding: utf-8 -*-


"""
Component DynamicSparseGridTopologyContainer

.. autofunction:: DynamicSparseGridTopologyContainer

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def DynamicSparseGridTopologyContainer(attachedTo , name='DynamicSparseGridTopologyContainer', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, filename='', position=array([], shape=(0, 3), dtype=float64), checkTopology=0, nbPoints=0, edges=array([], shape=(0, 2), dtype=int32), checkConnexity=0, quads=array([], shape=(0, 4), dtype=int32), createQuadArray=0, hexahedra=array([], shape=(0, 8), dtype=int32), resolution=array([0, 0, 0], dtype=int32), valuesIndexedInRegularGrid=array([], dtype=int8), valuesIndexedInTopology=array([], dtype=int8), idxInRegularGrid=array([], dtype=int32), idInRegularGrid2IndexInTopo='', voxelSize=array([1., 1., 1.]), **kwargs):
    """Hexahedron set topology container


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

		 quads: List of quad indices

		 createQuadArray: Force the creation of a set of quads associated with the hexahedra

		 hexahedra: List of hexahedron indices

		 resolution: voxel grid resolution

		 valuesIndexedInRegularGrid: values indexed in the Regular Grid

		 valuesIndexedInTopology: values indexed in the topology

		 idxInRegularGrid: indices in the Regular Grid

		 idInRegularGrid2IndexInTopo: map between id in the Regular Grid and index in the topology

		 voxelSize: Size of the Voxels


    """
    return attachedTo.createObject("DynamicSparseGridTopologyContainer" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, filename=filename, position=position, checkTopology=checkTopology, nbPoints=nbPoints, edges=edges, checkConnexity=checkConnexity, quads=quads, createQuadArray=createQuadArray, hexahedra=hexahedra, resolution=resolution, valuesIndexedInRegularGrid=valuesIndexedInRegularGrid, valuesIndexedInTopology=valuesIndexedInTopology, idxInRegularGrid=idxInRegularGrid, idInRegularGrid2IndexInTopo=idInRegularGrid2IndexInTopo, voxelSize=voxelSize, **kwargs)
