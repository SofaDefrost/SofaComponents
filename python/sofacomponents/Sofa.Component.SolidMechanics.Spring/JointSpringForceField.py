# -*- coding: utf-8 -*-


"""
Component JointSpringForceField

.. autofunction:: JointSpringForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def JointSpringForceField(attachedTo , name='JointSpringForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, outfile='', infile='', period=0.0, reinit=0, spring=[], showLawfulTorsion=0, showExtraTorsion=0, showFactorSize=1.0, **kwargs):
    """Springs for Rigids


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 outfile: output file name

		 infile: input file containing constant joint force

		 period: period between outputs

		 reinit: flag enabling reinitialization of the output file at each timestep

		 spring: pairs of indices, stiffness, damping, rest length

		 showLawfulTorsion: display the lawful part of the joint rotation

		 showExtraTorsion: display the illicit part of the joint rotation

		 showFactorSize: modify the size of the debug information of a given factor


    """
    return attachedTo.createObject("JointSpringForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, outfile=outfile, infile=infile, period=period, reinit=reinit, spring=spring, showLawfulTorsion=showLawfulTorsion, showExtraTorsion=showExtraTorsion, showFactorSize=showFactorSize, **kwargs)
