# -*- coding: utf-8 -*-


"""
Component LennardJonesForceField

.. autofunction:: LennardJonesForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def LennardJonesForceField(attachedTo , name='LennardJonesForceField', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, aInit=0.0, alpha=6.0, beta=12.0, dmax=2.0, fmax=1.0, d0=1.0, p0=1.0, damping=0.0, **kwargs):
    """Lennard-Jones forces for fluids


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 aInit: a for Gravitational FF which corresponds to G*m1*m2 alpha should be equal to 1 and beta to 0.

		 alpha: Alpha

		 beta: Beta

		 dmax: DMax

		 fmax: FMax

		 d0: d0

		 p0: p0

		 damping: Damping


    """
    return attachedTo.createObject("LennardJonesForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, aInit=aInit, alpha=alpha, beta=beta, dmax=dmax, fmax=fmax, d0=d0, p0=p0, damping=damping, **kwargs)
