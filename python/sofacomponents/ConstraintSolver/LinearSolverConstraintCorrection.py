# -*- coding: utf-8 -*-


"""
Component LinearSolverConstraintCorrection

.. autofunction:: LinearSolverConstraintCorrection

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def LinearSolverConstraintCorrection(attachedTo , name='LinearSolverConstraintCorrection', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, wire_optimization=0, solverName=[], **kwargs):
    """

    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 wire_optimization: constraints are reordered along a wire-like topology (from tip to base)

		 solverName: name of the constraint solver


    """
    return attachedTo.createObject("LinearSolverConstraintCorrection" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, wire_optimization=wire_optimization, solverName=solverName, **kwargs)
