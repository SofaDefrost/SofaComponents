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

        
def DynamicSparseGridTopologyContainer(attachedTo , name='DynamicSparseGridTopologyContainer', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, fileTopology='', position=[], nbPoints=0, points=[], edges=[], checkConnexity=0, quads=[], createQuadArray=0, hexahedra=[], resolution=[[0, 0, 0]], valuesIndexedInRegularGrid=[], valuesIndexedInTopology=[], idxInRegularGrid=[], idInRegularGrid2IndexInTopo='', voxelSize=[[1.0, 1.0, 1.0]], **kwargs):
    """Hexahedron set topology container


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 fileTopology: Filename of the mesh

		 position: Initial position of points

		 nbPoints: Number of points

		 points: List of point indices

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
    return attachedTo.createObject("DynamicSparseGridTopologyContainer" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, fileTopology=fileTopology, position=position, nbPoints=nbPoints, points=points, edges=edges, checkConnexity=checkConnexity, quads=quads, createQuadArray=createQuadArray, hexahedra=hexahedra, resolution=resolution, valuesIndexedInRegularGrid=valuesIndexedInRegularGrid, valuesIndexedInTopology=valuesIndexedInTopology, idxInRegularGrid=idxInRegularGrid, idInRegularGrid2IndexInTopo=idInRegularGrid2IndexInTopo, voxelSize=voxelSize, **kwargs)
