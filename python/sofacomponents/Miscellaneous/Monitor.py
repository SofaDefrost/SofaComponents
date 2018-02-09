# -*- coding: utf-8 -*-


"""
Component Monitor

.. autofunction:: Monitor

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def Monitor(attachedTo , name='Monitor', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=1, indices=[], ExportPositions=0, ExportVelocities=0, ExportForces=0, showPositions=0, PositionsColor='1 1 0 1', showVelocities=0, VelocitiesColor='1 1 0 1', showForces=0, ForcesColor='1 1 0 1', showMinThreshold=0.01, showTrajectories=0, TrajectoriesPrecision=0.1, TrajectoriesColor='1 1 0 1', sizeFactor=1.0, fileName='', **kwargs):
    """Monitoring of particles


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 indices: MechanicalObject points indices to monitor

		 ExportPositions: export Monitored positions as gnuplot file

		 ExportVelocities: export Monitored velocities as gnuplot file

		 ExportForces: export Monitored forces as gnuplot file

		 showPositions: see the Monitored positions

		 PositionsColor: define the color of positions

		 showVelocities: see the Monitored velocities

		 VelocitiesColor: define the color of velocities

		 showForces: see the Monitored forces

		 ForcesColor: define the color of forces

		 showMinThreshold: under this value, vectors are not represented

		 showTrajectories: print the trajectory of Monitored particles

		 TrajectoriesPrecision: set the dt between to save of positions

		 TrajectoriesColor: define the color of the trajectories

		 sizeFactor: factor to multiply to arrows

		 fileName: name of the plot files to be generated


    """
    return attachedTo.createObject("Monitor" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, indices=indices, ExportPositions=ExportPositions, ExportVelocities=ExportVelocities, ExportForces=ExportForces, showPositions=showPositions, PositionsColor=PositionsColor, showVelocities=showVelocities, VelocitiesColor=VelocitiesColor, showForces=showForces, ForcesColor=ForcesColor, showMinThreshold=showMinThreshold, showTrajectories=showTrajectories, TrajectoriesPrecision=TrajectoriesPrecision, TrajectoriesColor=TrajectoriesColor, sizeFactor=sizeFactor, fileName=fileName, **kwargs)
