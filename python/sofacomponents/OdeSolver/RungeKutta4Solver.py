# -*- coding: utf-8 -*-


"""
Component RungeKutta4Solver

.. autofunction:: RungeKutta4Solver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def RungeKutta4Solver(attachedTo , name='RungeKutta4Solver', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, **kwargs):
    """A popular explicit time integrator


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events


    """
    return attachedTo.createObject("RungeKutta4Solver" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, **kwargs)
