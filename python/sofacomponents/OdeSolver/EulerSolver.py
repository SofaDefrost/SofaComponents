# -*- coding: utf-8 -*-


"""
Component EulerSolver

.. autofunction:: EulerSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def EulerSolver(attachedTo , name='EulerSolver', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, symplectic=1, **kwargs):
    """A simple explicit time integrator


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 symplectic: If true, the velocities are updated before the positions and the method is symplectic (more robust). If false, the positions are updated before the velocities (standard Euler, less robust).


    """
    return attachedTo.createObject("EulerSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, symplectic=symplectic, **kwargs)
