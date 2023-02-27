# -*- coding: utf-8 -*-


"""
Component WriteTopology

.. autofunction:: WriteTopology

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def WriteTopology(attachedTo , name='WriteTopology', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=1, filename='', writeContainers=1, writeShellContainers=0, interval=0.0, time=array([], dtype=float64), period=0.0, **kwargs):
    """Write topology containers informations to file at each timestep


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 filename: output file name

		 writeContainers: flag enabling output of common topology containers.

		 writeShellContainers: flag enabling output of specific shell topology containers.

		 interval: time duration between outputs

		 time: set time to write outputs

		 period: period between outputs


    """
    return attachedTo.createObject("WriteTopology" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, filename=filename, writeContainers=writeContainers, writeShellContainers=writeShellContainers, interval=interval, time=time, period=period, **kwargs)
