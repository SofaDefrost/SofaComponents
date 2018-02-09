# -*- coding: utf-8 -*-


"""
Component FixedLMConstraint

.. autofunction:: FixedLMConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def FixedLMConstraint(attachedTo , name='FixedLMConstraint', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, group=0, constraintIndex=0, object1='', object2='', indices=[], drawSize=0.0, **kwargs):
    """Maintain a set of particle to a fixed position using LMConstraint


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

		 indices: List of the index of particles to be fixed

		 drawSize: 0 -> point based rendering, >0 -> radius of spheres


    """
    return attachedTo.createObject("FixedLMConstraint" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, group=group, constraintIndex=constraintIndex, object1=object1, object2=object2, indices=indices, drawSize=drawSize, **kwargs)
