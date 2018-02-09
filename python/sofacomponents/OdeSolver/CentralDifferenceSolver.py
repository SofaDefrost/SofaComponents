# -*- coding: utf-8 -*-


"""
Component CentralDifferenceSolver

.. autofunction:: CentralDifferenceSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def CentralDifferenceSolver(attachedTo , name='CentralDifferenceSolver', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, rayleighMass=0.0, **kwargs):
    """Explicit time integrator using central difference (also known as Verlet of Leap-frop)


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 rayleighMass: Rayleigh damping coefficient related to mass


    """
    return attachedTo.createObject("CentralDifferenceSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, rayleighMass=rayleighMass, **kwargs)
