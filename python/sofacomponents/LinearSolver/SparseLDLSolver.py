# -*- coding: utf-8 -*-


"""
Component SparseLDLSolver

.. autofunction:: SparseLDLSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SparseLDLSolver(attachedTo , name='SparseLDLSolver', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, multiGroup=0, saveMatrixToFile=0, **kwargs):
    """Direct linear solver based on Sparse LDL^T factorization, implemented with the CSPARSE library


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 multiGroup: activate multiple system solve, one for each child node

		 saveMatrixToFile: save matrix to a text file (can be very slow, as full matrix is stored


    """
    return attachedTo.createObject("SparseLDLSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, multiGroup=multiGroup, saveMatrixToFile=saveMatrixToFile, **kwargs)
