# -*- coding: utf-8 -*-


"""
Component RandomPointDistributionInSurface

.. autofunction:: RandomPointDistributionInSurface

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def RandomPointDistributionInSurface(attachedTo , name='RandomPointDistributionInSurface', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, randomSeed=0, isVisible=1, drawOutputPoints=0, minDistanceBetweenPoints=0.1, numberOfInPoints=10, numberOfTests=5, vertices=array([], shape=(0, 3), dtype=float64), triangles=array([], shape=(0, 3), dtype=int32), inPoints=array([], shape=(0, 3), dtype=float64), outPoints=array([], shape=(0, 3), dtype=float64), **kwargs):
    """This class truns on spiral any topological model


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 randomSeed: Set a specified seed for random generation (0 for "true pseudo-randomness" 

		 isVisible: is Visible ?

		 drawOutputPoints: Output points visible ?

		 minDistanceBetweenPoints: Min Distance between 2 points (-1 for true randomness)

		 numberOfInPoints: Number of points inside

		 numberOfTests: Number of tests to find if the point is inside or not (odd number)

		 vertices: Vertices

		 triangles: Triangles indices

		 inPoints: Points inside the surface

		 outPoints: Points outside the surface


    """
    return attachedTo.createObject("RandomPointDistributionInSurface" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, randomSeed=randomSeed, isVisible=isVisible, drawOutputPoints=drawOutputPoints, minDistanceBetweenPoints=minDistanceBetweenPoints, numberOfInPoints=numberOfInPoints, numberOfTests=numberOfTests, vertices=vertices, triangles=triangles, inPoints=inPoints, outPoints=outPoints, **kwargs)
