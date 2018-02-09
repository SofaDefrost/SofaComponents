# -*- coding: utf-8 -*-


"""
Component MeshGenerationFromPolyhedron

.. autofunction:: MeshGenerationFromPolyhedron

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MeshGenerationFromPolyhedron(attachedTo , name='MeshGenerationFromPolyhedron', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, inputPoints=[], inputTriangles=[], inputQuads=[], outputPoints=[], outputTetras=[], frozen=0, facetAngle=25.0, facetSize=0.15, facetApproximation=0.008, cellRatio=4.0, cellSize=0.2, sharpEdgeAngle=120.0, sharpEdgeSize=0.0, odt=0, lloyd=0, perturb=0, exude=0, odt_max_it=200, lloyd_max_it=200, perturb_max_time=20.0, exude_max_time=20.0, ordering=0, constantMeshProcess=0, meshingSeed=0, drawTetras=0, drawSurface=0, **kwargs):
    """Generate tetrahedral mesh from triangular mesh


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 inputPoints: Rest position coordinates of the degrees of freedom

		 inputTriangles: List of triangles

		 inputQuads: List of quads (if no triangles) 

		 outputPoints: New Rest position coordinates from the tetrahedral generation

		 outputTetras: List of tetrahedra

		 frozen: true to prohibit recomputations of the mesh

		 facetAngle: Lower bound for the angle in degrees of the surface mesh facets

		 facetSize: Uniform upper bound for the radius of the surface Delaunay balls

		 facetApproximation: Upper bound for the center-center distances of the surface mesh facets

		 cellRatio: Upper bound for the radius-edge ratio of the tetrahedra

		 cellSize: Uniform upper bound for the circumradii of the tetrahedra in the mesh

		 sharpEdgeAngle: Threshold angle to detect sharp edges in input surface (activated with CGAL 3.8+ if sharpEdgeSize > 0)

		 sharpEdgeSize: Meshing size for sharp feature edges (activated with CGAL 3.8+ if sharpEdgeSize > 0)

		 odt: activate odt optimization

		 lloyd: activate lloyd optimization

		 perturb: activate perturb optimization

		 exude: activate exude optimization

		 odt_max_it: odt max iteration number

		 lloyd_max_it: lloyd max iteration number

		 perturb_max_time: perturb maxtime

		 exude_max_time: exude max time

		 ordering: output points and elements ordering (0 = none, 1 = longest bbox axis)

		 constantMeshProcess: deterministic choice of first point used in meshing process (true = constant output / false = variable output)

		 meshingSeed: seed used when picking first point in meshing process

		 drawTetras: display generated tetra mesh

		 drawSurface: display input surface mesh


    """
    return attachedTo.createObject("MeshGenerationFromPolyhedron" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, inputPoints=inputPoints, inputTriangles=inputTriangles, inputQuads=inputQuads, outputPoints=outputPoints, outputTetras=outputTetras, frozen=frozen, facetAngle=facetAngle, facetSize=facetSize, facetApproximation=facetApproximation, cellRatio=cellRatio, cellSize=cellSize, sharpEdgeAngle=sharpEdgeAngle, sharpEdgeSize=sharpEdgeSize, odt=odt, lloyd=lloyd, perturb=perturb, exude=exude, odt_max_it=odt_max_it, lloyd_max_it=lloyd_max_it, perturb_max_time=perturb_max_time, exude_max_time=exude_max_time, ordering=ordering, constantMeshProcess=constantMeshProcess, meshingSeed=meshingSeed, drawTetras=drawTetras, drawSurface=drawSurface, **kwargs)
