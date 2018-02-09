# -*- coding: utf-8 -*-


"""
Component RestShapeSpringsForceField

.. autofunction:: RestShapeSpringsForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def RestShapeSpringsForceField(attachedTo , name='RestShapeSpringsForceField', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, points=[], stiffness=[], angularStiffness=[], pivot_points=[], external_points=[], recompute_indices=1, drawSpring=0, springColor='0 1 0 1', **kwargs):
    """Simple elastic springs applied to given degrees of freedom between their current and rest shape position


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 points: points controlled by the rest shape springs

		 stiffness: stiffness values between the actual position and the rest shape position

		 angularStiffness: angularStiffness assigned when controlling the rotation of the points

		 pivot_points: global pivot points used when translations instead of the rigid mass centers

		 external_points: points from the external Mechancial State that define the rest shape springs

		 recompute_indices: Recompute indices (should be false for BBOX)

		 drawSpring: draw Spring

		 springColor: spring color. (default=[0.0,1.0,0.0,1.0])


    """
    return attachedTo.createObject("RestShapeSpringsForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, points=points, stiffness=stiffness, angularStiffness=angularStiffness, pivot_points=pivot_points, external_points=external_points, recompute_indices=recompute_indices, drawSpring=drawSpring, springColor=springColor, **kwargs)
