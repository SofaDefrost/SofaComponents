# -*- coding: utf-8 -*-


"""
Component VariationalSymplecticSolver

.. autofunction:: VariationalSymplecticSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def VariationalSymplecticSolver(attachedTo , name='VariationalSymplecticSolver', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, newtonError=0.01, steps=5, rayleighStiffness=0.0, rayleighMass=0.0, verbose=0, saveEnergyInFile=0, explicitIntegration=0, file='', computeHamiltonian=1, hamiltonianEnergy=0.0, **kwargs):
    """Implicit time integrator which conserves linear momentum and mechanical energy


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 newtonError: Error tolerance for Newton iterations

		 steps: Maximum number of Newton steps

		 rayleighStiffness: Rayleigh damping coefficient related to stiffness, > 0

		 rayleighMass: Rayleigh damping coefficient related to mass, > 0

		 verbose: Dump information on the residual errors and number of Newton iterations

		 saveEnergyInFile: If kinetic and potential energies should be dumped in a CSV file at each iteration

		 explicitIntegration: Use explicit integration scheme

		 file: File name where kinetic and potential energies are saved in a CSV file

		 computeHamiltonian: Compute hamiltonian

		 hamiltonianEnergy: hamiltonian energy


    """
    return attachedTo.createObject("VariationalSymplecticSolver" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, newtonError=newtonError, steps=steps, rayleighStiffness=rayleighStiffness, rayleighMass=rayleighMass, verbose=verbose, saveEnergyInFile=saveEnergyInFile, explicitIntegration=explicitIntegration, file=file, computeHamiltonian=computeHamiltonian, hamiltonianEnergy=hamiltonianEnergy, **kwargs)
