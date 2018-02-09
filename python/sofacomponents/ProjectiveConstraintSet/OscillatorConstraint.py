# -*- coding: utf-8 -*-


"""
Component OscillatorConstraint

.. autofunction:: OscillatorConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def OscillatorConstraint(attachedTo , name='OscillatorConstraint', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, group=0, endTime=-1.0, oscillators='', **kwargs):
    """Apply a sinusoidal trajectory to given points


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 group: ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.

		 endTime: The constraint stops acting after the given value.
Use a negative value for infinite constraints

		 oscillators: Define a sequence of oscillating particules: 
[index, mean, amplitude, pulsation, phase]


    """
    return attachedTo.createObject("OscillatorConstraint" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, group=group, endTime=endTime, oscillators=oscillators, **kwargs)
