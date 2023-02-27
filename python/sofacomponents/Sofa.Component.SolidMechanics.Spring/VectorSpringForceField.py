# -*- coding: utf-8 -*-


"""
Component VectorSpringForceField

.. autofunction:: VectorSpringForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def VectorSpringForceField(attachedTo , name='VectorSpringForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, springs=[], filename='', stiffness=1.0, viscosity=1.0, useTopology=0, **kwargs):
    """Spring force field acting along the edges of a mesh


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 springs: springs data

		 filename: File name from which the spring informations are loaded

		 stiffness: Default edge stiffness used in absence of file information

		 viscosity: Default edge viscosity used in absence of file information

		 useTopology: Activate/Desactivate topology mode of the component (springs on each edge)


    """
    return attachedTo.createObject("VectorSpringForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, springs=springs, filename=filename, stiffness=stiffness, viscosity=viscosity, useTopology=useTopology, **kwargs)
