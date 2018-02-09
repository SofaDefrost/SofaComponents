# -*- coding: utf-8 -*-


"""
Component HausdorffDistance

.. autofunction:: HausdorffDistance

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def HausdorffDistance(attachedTo , name='HausdorffDistance', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=1, points1=[], points2=[], d12=0.0, d21=0.0, max=0.0, update=0, **kwargs):
    """Compute the Hausdorff distance of two point clouds


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 points1: Points belonging to the first point cloud

		 points2: Points belonging to the second point cloud

		 d12: Distance from point cloud 1 to 2

		 d21: Distance from point cloud 2 to 1

		 max: Symmetrical Hausdorff distance

		 update: Recompute every time step


    """
    return attachedTo.createObject("HausdorffDistance" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, points1=points1, points2=points2, d12=d12, d21=d21, max=max, update=update, **kwargs)
