# -*- coding: utf-8 -*-


"""
Component ParticleSink

.. autofunction:: ParticleSink

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ParticleSink(attachedTo , name='ParticleSink', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=1, group=0, endTime=-1.0, normal=[[0.0, 1.0, 0.0]], d0=0.0, d1=0.0, color='0 0.5 0.2 1', showPlane=0, fixed=[], **kwargs):
    """Parametrable particle generator


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 group: ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.

		 endTime: The constraint stops acting after the given value.
Use a negative value for infinite constraints

		 normal: plane normal

		 d0: plane d coef at which particles acceleration is constrained to 0

		 d1: plane d coef at which particles are removed

		 color: plane color. (default=[0.0,0.5,0.2,1.0])

		 showPlane: enable/disable drawing of plane

		 fixed: indices of fixed particles


    """
    return attachedTo.createObject("ParticleSink" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, group=group, endTime=endTime, normal=normal, d0=d0, d1=d1, color=color, showPlane=showPlane, fixed=fixed, **kwargs)
