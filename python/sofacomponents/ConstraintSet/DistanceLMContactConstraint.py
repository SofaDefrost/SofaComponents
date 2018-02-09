# -*- coding: utf-8 -*-


"""
Component DistanceLMContactConstraint

.. autofunction:: DistanceLMContactConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def DistanceLMContactConstraint(attachedTo , name='DistanceLMContactConstraint', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, group=0, constraintIndex=0, object1='', object2='', pointPairs=[], contactFriction=0.0, **kwargs):
    """Maintain a minimum contact distance between two objects


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 group: ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.

		 constraintIndex: Constraint index (first index in the right hand term resolution vector)

		 object1: First Object to constrain

		 object2: Second Object to constrain

		 pointPairs: List of the edges to constrain

		 contactFriction: Coulomb friction coefficient (same for all)


    """
    return attachedTo.createObject("DistanceLMContactConstraint" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, group=group, constraintIndex=constraintIndex, object1=object1, object2=object2, pointPairs=pointPairs, contactFriction=contactFriction, **kwargs)
