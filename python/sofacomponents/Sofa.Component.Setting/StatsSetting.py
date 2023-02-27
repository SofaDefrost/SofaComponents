# -*- coding: utf-8 -*-


"""
Component StatsSetting

.. autofunction:: StatsSetting

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def StatsSetting(attachedTo , name='StatsSetting', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, dumpState=0, logTime=0, exportState=0, **kwargs):
    """Stats settings


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 dumpState: Dump state vectors at each time step of the simulation

		 logTime: Output in the console an average of the time spent during different stages of the simulation

		 exportState: Create GNUPLOT files with the positions, velocities and forces of all the simulated objects of the scene


    """
    return attachedTo.createObject("StatsSetting" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, dumpState=dumpState, logTime=logTime, exportState=exportState, **kwargs)
