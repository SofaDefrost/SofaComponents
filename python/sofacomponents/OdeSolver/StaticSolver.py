# -*- coding: utf-8 -*-


"""
Component StaticSolver

.. autofunction:: StaticSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def StaticSolver(attachedTo , name='StaticSolver', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, massCoef=0.0, dampingCoef=0.0, stiffnessCoef=1.0, applyIncrementFactor=0, **kwargs):
    """A solver which seeks the static equilibrium of the scene it monitors


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 massCoef: factor associated with the mass matrix in the equation system

		 dampingCoef: factor associated with the mass matrix in the equation system

		 stiffnessCoef: factor associated with the mass matrix in the equation system

		 applyIncrementFactor: multiply the solution by dt before adding it to the current state


    """
    return attachedTo.createObject("StaticSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, massCoef=massCoef, dampingCoef=dampingCoef, stiffnessCoef=stiffnessCoef, applyIncrementFactor=applyIncrementFactor, **kwargs)
