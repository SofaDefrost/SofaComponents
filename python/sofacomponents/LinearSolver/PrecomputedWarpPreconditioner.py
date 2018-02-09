# -*- coding: utf-8 -*-


"""
Component PrecomputedWarpPreconditioner

.. autofunction:: PrecomputedWarpPreconditioner

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def PrecomputedWarpPreconditioner(attachedTo , name='PrecomputedWarpPreconditioner', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, multiGroup=0, jmjt_twostep=1, verbose=0, use_file=1, share_matrix=1, solverName='', use_rotations=1, draw_rotations_scale=0.0, **kwargs):
    """Linear system solver based on a precomputed inverse matrix, wrapped by a per-node rotation matrix


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 multiGroup: activate multiple system solve, one for each child node

		 jmjt_twostep: Use two step algorithm to compute JMinvJt

		 verbose: Dump system state at each iteration

		 use_file: Dump system matrix in a file

		 share_matrix: Share the compliance matrix in memory if they are related to the same file (WARNING: might require to reload Sofa when opening a new scene...)

		 solverName: Name of the solver to use to precompute the first matrix

		 use_rotations: Use Rotations around the preconditioner

		 draw_rotations_scale: Scale rotations in draw function


    """
    return attachedTo.createObject("PrecomputedWarpPreconditioner" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, multiGroup=multiGroup, jmjt_twostep=jmjt_twostep, verbose=verbose, use_file=use_file, share_matrix=share_matrix, solverName=solverName, use_rotations=use_rotations, draw_rotations_scale=draw_rotations_scale, **kwargs)
