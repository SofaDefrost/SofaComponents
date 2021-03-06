# -*- coding: utf-8 -*-


"""
Component ProjectToLineConstraint

.. autofunction:: ProjectToLineConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ProjectToLineConstraint(attachedTo , name='ProjectToLineConstraint', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, group=0, endTime=-1.0, indices=[[0]], drawSize=0.0, origin=[[0.0, 0.0, 0.0]], direction=[[0.0, 0.0, 0.0]], **kwargs):
    """Attach given particles to their initial positions


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 group: ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.

		 endTime: The constraint stops acting after the given value.
Use a negative value for infinite constraints

		 indices: Indices of the fixed points

		 drawSize: 0 -> point based rendering, >0 -> radius of spheres

		 origin: A point in the line

		 direction: Direction of the line


    """
    return attachedTo.createObject("ProjectToLineConstraint" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, group=group, endTime=endTime, indices=indices, drawSize=drawSize, origin=origin, direction=direction, **kwargs)
