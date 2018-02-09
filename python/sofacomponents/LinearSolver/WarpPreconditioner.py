# -*- coding: utf-8 -*-


"""
Component WarpPreconditioner

.. autofunction:: WarpPreconditioner

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def WarpPreconditioner(attachedTo , name='WarpPreconditioner', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, multiGroup=0, solverName='', useRotationFinder=0, **kwargs):
    """Linear system solver wrapping another (precomputed) linear solver by a per-node rotation matrix


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 multiGroup: activate multiple system solve, one for each child node

		 solverName: Name of the solver/preconditioner to warp

		 useRotationFinder: Which rotation Finder to use


    """
    return attachedTo.createObject("WarpPreconditioner" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, multiGroup=multiGroup, solverName=solverName, useRotationFinder=useRotationFinder, **kwargs)
