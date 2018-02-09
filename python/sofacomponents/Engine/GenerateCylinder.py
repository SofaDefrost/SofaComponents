# -*- coding: utf-8 -*-


"""
Component GenerateCylinder

.. autofunction:: GenerateCylinder

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def GenerateCylinder(attachedTo , name='GenerateCylinder', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, output_TetrahedraPosition=[], output_TrianglesPosition=[], tetrahedra=[], triangles=[], BezierTriangleWeights=[], isBezierTriangleRational=[], BezierTriangleDegree=0, BezierTetrahedronWeights=[], isBezierTetrahedronRational=[], BezierTetrahedronDegree=0, radius=0.2, height=1.0, origin=[[0.0, 0.0, 0.0]], openSurface=1, resCircumferential=6, resRadial=3, resHeight=5, **kwargs):
    """Generate a Cylindrical Tetrahedral Mesh


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 output_TetrahedraPosition: output array of 3d points of tetrahedra mesh

		 output_TrianglesPosition: output array of 3d points of triangle mesh

		 tetrahedra: output mesh tetrahedra

		 triangles: output triangular mesh

		 BezierTriangleWeights: weights of rational Bezier triangles

		 isBezierTriangleRational: booleans indicating if each Bezier triangle is rational or integral

		 BezierTriangleDegree: order of Bezier triangles

		 BezierTetrahedronWeights: weights of rational Bezier tetrahedra

		 isBezierTetrahedronRational: booleans indicating if each Bezier tetrahedron is rational or integral

		 BezierTetrahedronDegree: order of Bezier tetrahedra

		 radius: input cylinder radius

		 height: input cylinder height

		 origin: cylinder origin point

		 openSurface: if the cylinder is open at its 2 ends

		 resCircumferential: Resolution in the circumferential direction

		 resRadial: Resolution in the radial direction

		 resHeight: Resolution in the height direction


    """
    return attachedTo.createObject("GenerateCylinder" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, output_TetrahedraPosition=output_TetrahedraPosition, output_TrianglesPosition=output_TrianglesPosition, tetrahedra=tetrahedra, triangles=triangles, BezierTriangleWeights=BezierTriangleWeights, isBezierTriangleRational=isBezierTriangleRational, BezierTriangleDegree=BezierTriangleDegree, BezierTetrahedronWeights=BezierTetrahedronWeights, isBezierTetrahedronRational=isBezierTetrahedronRational, BezierTetrahedronDegree=BezierTetrahedronDegree, radius=radius, height=height, origin=origin, openSurface=openSurface, resCircumferential=resCircumferential, resRadial=resRadial, resHeight=resHeight, **kwargs)
