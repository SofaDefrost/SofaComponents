# -*- coding: utf-8 -*-


"""
Component LineBendingSprings

.. autofunction:: LineBendingSprings

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def LineBendingSprings(attachedTo , name='LineBendingSprings', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, stiffness=100.0, damping=5.0, showArrowSize=0.009999999776482582, drawMode=0, spring='', fileSprings='', **kwargs):
    """Springs added to a polyline to prevent bending


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


    """
    return attachedTo.createObject("LineBendingSprings" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, stiffness=stiffness, damping=damping, showArrowSize=showArrowSize, drawMode=drawMode, spring=spring, fileSprings=fileSprings, **kwargs)
