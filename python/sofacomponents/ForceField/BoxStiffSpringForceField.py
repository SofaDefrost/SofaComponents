# -*- coding: utf-8 -*-


"""
Component BoxStiffSpringForceField

.. autofunction:: BoxStiffSpringForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def BoxStiffSpringForceField(attachedTo , name='BoxStiffSpringForceField', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, stiffness=100.0, damping=5.0, showArrowSize=0.009999999776482582, drawMode=0, spring='', fileSprings='', box_object1=[[0.0, 0.0, 0.0, 1.0, 1.0, 1.0]], box_object2=[[0.0, 0.0, 0.0, 1.0, 1.0, 1.0]], factorRestLength=1.0, forceOldBehavior=1, **kwargs):
    """Set Spring between the points inside a given box


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 stiffness: uniform stiffness for the all springs

		 damping: uniform damping for the all springs

		 showArrowSize: size of the axis

		 drawMode: The way springs will be drawn:
- 0: Line
- 1:Cylinder
- 2: Arrow

		 spring: pairs of indices, stiffness, damping, rest length

		 fileSprings: File describing the springs

		 box_object1: Box for the object1 where springs will be attached

		 box_object2: Box for the object2 where springs will be attached

		 factorRestLength: Factor used to compute the rest length of the springs generated

		 forceOldBehavior: Keep using the old behavior


    """
    return attachedTo.createObject("BoxStiffSpringForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, stiffness=stiffness, damping=damping, showArrowSize=showArrowSize, drawMode=drawMode, spring=spring, fileSprings=fileSprings, box_object1=box_object1, box_object2=box_object2, factorRestLength=factorRestLength, forceOldBehavior=forceOldBehavior, **kwargs)
