# -*- coding: utf-8 -*-


"""
Component ParticleSource

.. autofunction:: ParticleSource

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ParticleSource(attachedTo , name='ParticleSource', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=1, group=0, endTime=-1.0, translation=[[0.0, 0.0, 0.0]], scale=1.0, center=[[0.0, 0.0, 0.0]], radius=[[0.0, 0.0, 0.0]], velocity=[[0.0, 0.0, 0.0]], delay=0.01, start=0.0, stop=10000000000.0, canHaveEmptyVector=0, lastparticles=[], **kwargs):
    """Parametrable particle generator


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 group: ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.

		 endTime: The constraint stops acting after the given value.
Use a negative value for infinite constraints

		 translation: translation applied to center(s)

		 scale: scale applied to center(s)

		 center: Source center(s)

		 radius: Source radius

		 velocity: Particle initial velocity

		 delay: Delay between particles creation

		 start: Source starting time

		 stop: Source stopping time

		 canHaveEmptyVector: 

		 lastparticles: lastparticles indices


    """
    return attachedTo.createObject("ParticleSource" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, group=group, endTime=endTime, translation=translation, scale=scale, center=center, radius=radius, velocity=velocity, delay=delay, start=start, stop=stop, canHaveEmptyVector=canHaveEmptyVector, lastparticles=lastparticles, **kwargs)
