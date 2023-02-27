# -*- coding: utf-8 -*-


"""
Component MechanicalMatrixMapper

.. autofunction:: MechanicalMatrixMapper

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MechanicalMatrixMapper(attachedTo , name='MechanicalMatrixMapper', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, forceFieldList=[], stopAtNodeToParse=0, skipJ1tKJ1=0, skipJ2tKJ2=0, fastMatrixProduct=1, parallelTasks=1, forceFieldAndMass=0, **kwargs):
    """This component allows to map the stiffness (and mass) matrix through a mapping.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 forceFieldList: List of ForceField Names to work on (by default will take all)

		 stopAtNodeToParse: Boolean to choose whether forceFields in children Nodes of NodeToParse should be considered.

		 skipJ1tKJ1: Boolean to choose whether to skip J1tKJ1 to avoid 2 contributions, in case 2 MechanicalMatrixMapper are used

		 skipJ2tKJ2: Boolean to choose whether to skip J2tKJ2 to avoid 2 contributions, in case 2 MechanicalMatrixMapper are used

		 fastMatrixProduct: If true, an accelerated method to compute matrix products based on the pre-computation of the matrices intersection is used. Regular matrix product otherwise.

		 parallelTasks: Execute some tasks in parallel for better performances

		 forceFieldAndMass: If true, allows forceField and mass to be in the same component.


    """
    return attachedTo.createObject("MechanicalMatrixMapper" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, forceFieldList=forceFieldList, stopAtNodeToParse=stopAtNodeToParse, skipJ1tKJ1=skipJ1tKJ1, skipJ2tKJ2=skipJ2tKJ2, fastMatrixProduct=fastMatrixProduct, parallelTasks=parallelTasks, forceFieldAndMass=forceFieldAndMass, **kwargs)
