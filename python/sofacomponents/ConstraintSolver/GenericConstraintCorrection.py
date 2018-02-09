# -*- coding: utf-8 -*-


"""
Component GenericConstraintCorrection

.. autofunction:: GenericConstraintCorrection

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def GenericConstraintCorrection(attachedTo , name='GenericConstraintCorrection', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, solverName=[], ODESolverName='', **kwargs):
    """

    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 solverName: name of the constraint solver

		 ODESolverName: name of the ode solver


    """
    return attachedTo.createObject("GenericConstraintCorrection" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, solverName=solverName, ODESolverName=ODESolverName, **kwargs)
