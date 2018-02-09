# -*- coding: utf-8 -*-


"""
Component DistanceGridForceField

.. autofunction:: DistanceGridForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def DistanceGridForceField(attachedTo , name='DistanceGridForceField', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, fileDistanceGrid='', scale=1.0, box=[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], nx=64, ny=64, nz=64, stiffnessIn=500.0, stiffnessOut=0.0, damping=0.01, maxdist=1.0, minArea=0.0, stiffnessArea=100.0, minVolume=0.0, stiffnessVolume=0.0, color='0 0.5 0.2 1', draw=0, drawPoints=0, drawSize=10.0, localRange=[[-1, -1]], **kwargs):
    """Force applied by a distancegrid toward the exterior, the interior, or the surface


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 fileDistanceGrid: load distance grid from specified file

		 scale: scaling factor for input file

		 box: Field bounding box defined by xmin,ymin,zmin, xmax,ymax,zmax

		 nx: number of values on X axis

		 ny: number of values on Y axis

		 nz: number of values on Z axis

		 stiffnessIn: force stiffness when inside of the object

		 stiffnessOut: force stiffness when outside of the object

		 damping: force damping coefficient

		 maxdist: max distance of the surface after which no more force is applied

		 minArea: minimal area for each triangle, as seen from the direction of the local surface (i.e. a flipped triangle will have a negative area)

		 stiffnessArea: force stiffness if a triangle have an area less than minArea

		 minVolume: minimal volume for each tetrahedron (a flipped triangle will have a negative volume)

		 stiffnessVolume: force stiffness if a tetrahedron have an volume less than minVolume

		 color: display color.(default=[0.0,0.5,0.2,1.0])

		 draw: enable/disable drawing of distancegrid

		 drawPoints: enable/disable drawing of distancegrid

		 drawSize: display size if draw is enabled

		 localRange: optional range of local DOF indices. Any computation involving only indices outside of this range are discarded (useful for parallelization using mesh partitionning)


    """
    return attachedTo.createObject("DistanceGridForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, fileDistanceGrid=fileDistanceGrid, scale=scale, box=box, nx=nx, ny=ny, nz=nz, stiffnessIn=stiffnessIn, stiffnessOut=stiffnessOut, damping=damping, maxdist=maxdist, minArea=minArea, stiffnessArea=stiffnessArea, minVolume=minVolume, stiffnessVolume=stiffnessVolume, color=color, draw=draw, drawPoints=drawPoints, drawSize=drawSize, localRange=localRange, **kwargs)
