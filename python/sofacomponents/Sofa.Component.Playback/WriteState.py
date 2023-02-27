# -*- coding: utf-8 -*-


"""
Component WriteState

.. autofunction:: WriteState

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def WriteState(attachedTo , name='WriteState', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=1, filename='', writeX=1, writeX0=0, writeV=0, writeF=0, time=array([], dtype=float64), period=0.0, DOFsX=array([], dtype=int32), DOFsV=array([], dtype=int32), stopAt=0.0, keperiod=0.0, **kwargs):
    """Write State vectors to file at each timestep


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 filename: output file name

		 writeX: flag enabling output of X vector

		 writeX0: flag enabling output of X0 vector

		 writeV: flag enabling output of V vector

		 writeF: flag enabling output of F vector

		 time: set time to write outputs (by default export at t=0)

		 period: period between outputs

		 DOFsX: set the position DOFs to write

		 DOFsV: set the velocity DOFs to write

		 stopAt: stop the simulation when the given threshold is reached

		 keperiod: set the period to measure the kinetic energy increase


    """
    return attachedTo.createObject("WriteState" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, filename=filename, writeX=writeX, writeX0=writeX0, writeV=writeV, writeF=writeF, time=time, period=period, DOFsX=DOFsX, DOFsV=DOFsV, stopAt=stopAt, keperiod=keperiod, **kwargs)
