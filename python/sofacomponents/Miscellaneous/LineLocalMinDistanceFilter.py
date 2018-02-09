# -*- coding: utf-8 -*-


"""
Component LineLocalMinDistanceFilter

.. autofunction:: LineLocalMinDistanceFilter

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def LineLocalMinDistanceFilter(attachedTo , name='LineLocalMinDistanceFilter', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, coneExtension=0.5, coneMinAngle=0.0, isRigid=0, pointInfo='', lineInfo='', **kwargs):
    """This class manages Line collision models cones filters computations and updates.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 coneExtension: Filtering cone extension angle.

		 coneMinAngle: Minimal filtering cone angle value, independent from geometry.

		 isRigid: filters optimization for rigid case.

		 pointInfo: point filter data

		 lineInfo: line filter data


    """
    return attachedTo.createObject("LineLocalMinDistanceFilter" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, coneExtension=coneExtension, coneMinAngle=coneMinAngle, isRigid=isRigid, pointInfo=pointInfo, lineInfo=lineInfo, **kwargs)
