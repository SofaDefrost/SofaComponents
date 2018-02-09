# -*- coding: utf-8 -*-


"""
Component DOFBlockerLMConstraint

.. autofunction:: DOFBlockerLMConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def DOFBlockerLMConstraint(attachedTo , name='DOFBlockerLMConstraint', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, group=0, constraintIndex=0, object1='', object2='', rotationAxis=[], factorAxis=[], indices=[], showSizeAxis=1.0, **kwargs):
    """Constrain the rotation of a given set of Rigid Bodies


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

		 rotationAxis: List of rotation axis to constrain

		 factorAxis: Factor to apply in order to block only a certain amount of rotation along the axis

		 indices: List of the index of particles to be fixed

		 showSizeAxis: size of the vector used to display the constrained axis


    """
    return attachedTo.createObject("DOFBlockerLMConstraint" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, group=group, constraintIndex=constraintIndex, object1=object1, object2=object2, rotationAxis=rotationAxis, factorAxis=factorAxis, indices=indices, showSizeAxis=showSizeAxis, **kwargs)
