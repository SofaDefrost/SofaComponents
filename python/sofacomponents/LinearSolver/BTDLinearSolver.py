# -*- coding: utf-8 -*-


"""
Component BTDLinearSolver

.. autofunction:: BTDLinearSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def BTDLinearSolver(attachedTo , name='BTDLinearSolver', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, multiGroup=0, verbose=0, showProblem=0, subpartSolve=0, verification=0, test_perf=0, blockSize=6, **kwargs):
    """Linear system solver using Thomas Algorithm for Block Tridiagonal matrices


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 multiGroup: activate multiple system solve, one for each child node

		 verbose: Dump system state at each iteration

		 showProblem: display debug informations about subpartSolve computation

		 subpartSolve: Allows for the computation of a subpart of the system

		 verification: verification of the subpartSolve

		 test_perf: verification of performance

		 blockSize: dimension of the blocks in the matrix


    """
    return attachedTo.createObject("BTDLinearSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, multiGroup=multiGroup, verbose=verbose, showProblem=showProblem, subpartSolve=subpartSolve, verification=verification, test_perf=test_perf, blockSize=blockSize, **kwargs)
