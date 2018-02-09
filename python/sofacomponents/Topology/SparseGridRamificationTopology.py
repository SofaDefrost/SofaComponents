# -*- coding: utf-8 -*-


"""
Component SparseGridRamificationTopology

.. autofunction:: SparseGridRamificationTopology

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SparseGridRamificationTopology(attachedTo , name='SparseGridRamificationTopology', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, fileTopology='', position=[], edges=[], triangles=[], quads=[], tetrahedra=[], isToPrint=0, hexahedra=[], uv=[], drawEdges=0, drawTriangles=0, drawQuads=0, drawTetrahedra=0, drawHexahedra=0, fillWeighted=1, onlyInsideCells=0, n=[[2, 2, 2]], min=[[0.0, 0.0, 0.0]], max=[[0.0, 0.0, 0.0]], cellWidth=0.0, nbVirtualFinerLevels=0, dataResolution=[[0, 0, 0]], voxelSize=[[1.0, 1.0, 1.0]], marchingCubeStep=1, convolutionSize=0, vertices=[], facets=[], input_triangles=[], input_quads=[], finestConnectivity=1, **kwargs):
    """Sparse grid in 3D (modified)


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 fileTopology: Filename of the mesh

		 position: List of point positions

		 edges: List of edge indices

		 triangles: List of triangle indices

		 quads: List of quad indices

		 tetrahedra: List of tetrahedron indices

		 isToPrint: suppress somes data before using save as function

		 hexahedra: List of hexahedron indices

		 uv: List of uv coordinates

		 drawEdges: if true, draw the topology Edges

		 drawTriangles: if true, draw the topology Triangles

		 drawQuads: if true, draw the topology Quads

		 drawTetrahedra: if true, draw the topology Tetrahedra

		 drawHexahedra: if true, draw the topology hexahedra

		 fillWeighted: Is quantity of matter inside a cell taken into account? (.5 for boundary, 1 for inside)

		 onlyInsideCells: Select only inside cells (exclude boundary cells)

		 n: grid resolution

		 min: Min

		 max: Max

		 cellWidth: if > 0 : dimension of each cell in the created grid

		 nbVirtualFinerLevels: create virtual (not in the animation tree) finer sparse grids in order to dispose of finest information (usefull to compute better mechanical properties for example)

		 dataResolution: Dimension of the voxel File

		 voxelSize: Dimension of one voxel

		 marchingCubeStep: Step of the Marching Cube algorithm

		 convolutionSize: Dimension of the convolution kernel to smooth the voxels. 0 if no smoothing is required.

		 vertices: Input mesh vertices

		 facets: Input mesh facets

		 input_triangles: Input mesh triangles

		 input_quads: Input mesh quads

		 finestConnectivity: Test for connectivity at the finest level? (more precise but slower by testing all intersections between the model mesh and the faces between boundary cubes)


    """
    return attachedTo.createObject("SparseGridRamificationTopology" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, fileTopology=fileTopology, position=position, edges=edges, triangles=triangles, quads=quads, tetrahedra=tetrahedra, isToPrint=isToPrint, hexahedra=hexahedra, uv=uv, drawEdges=drawEdges, drawTriangles=drawTriangles, drawQuads=drawQuads, drawTetrahedra=drawTetrahedra, drawHexahedra=drawHexahedra, fillWeighted=fillWeighted, onlyInsideCells=onlyInsideCells, n=n, min=min, max=max, cellWidth=cellWidth, nbVirtualFinerLevels=nbVirtualFinerLevels, dataResolution=dataResolution, voxelSize=voxelSize, marchingCubeStep=marchingCubeStep, convolutionSize=convolutionSize, vertices=vertices, facets=facets, input_triangles=input_triangles, input_quads=input_quads, finestConnectivity=finestConnectivity, **kwargs)
