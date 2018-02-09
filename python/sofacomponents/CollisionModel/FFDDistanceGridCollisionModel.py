# -*- coding: utf-8 -*-


"""
Component FFDDistanceGridCollisionModel

.. autofunction:: FFDDistanceGridCollisionModel

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def FFDDistanceGridCollisionModel(attachedTo , name='FFDDistanceGridCollisionModel', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, active=1, moving=1, simulated=1, selfCollision=0, proximity=0.0, contactStiffness=10.0, contactFriction=0.0, contactRestitution=0.0, contactResponse='', color='1 0 0 1', group=[], fileFFDDistanceGrid='', scale=1.0, sampling=0.0, box=[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], nx=64, ny=64, nz=64, dumpfilename='', usePoints=1, singleContact=0, **kwargs):
    """Grid-based deformable distance field


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 active: flag indicating if this collision model is active and should be included in default collision detections

		 moving: flag indicating if this object is changing position between iterations

		 simulated: flag indicating if this object is controlled by a simulation

		 selfCollision: flag indication if the object can self collide

		 proximity: Distance to the actual (visual) surface

		 contactStiffness: Contact stiffness

		 contactFriction: Contact friction coefficient (dry or viscous or unused depending on the contact method)

		 contactRestitution: Contact coefficient of restitution

		 contactResponse: if set, indicate to the ContactManager that this model should use the given class of contacts.
Note that this is only indicative, and in particular if both collision models specify a different class it is up to the manager to choose.

		 color: color used to display the collision model if requested

		 group: IDs of the groups containing this model. No collision can occur between collision models included in a common group (e.g. allowing the same object to have multiple collision models)

		 fileFFDDistanceGrid: load distance grid from specified file

		 scale: scaling factor for input file

		 sampling: if not zero: sample the surface with points approximately separated by the given sampling distance (expressed in voxels if the value is negative)

		 box: Field bounding box defined by xmin,ymin,zmin, xmax,ymax,zmax

		 nx: number of values on X axis

		 ny: number of values on Y axis

		 nz: number of values on Z axis

		 dumpfilename: write distance grid to specified file

		 usePoints: use mesh vertices for collision detection

		 singleContact: keep only the deepest contact in each cell


    """
    return attachedTo.createObject("FFDDistanceGridCollisionModel" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, active=active, moving=moving, simulated=simulated, selfCollision=selfCollision, proximity=proximity, contactStiffness=contactStiffness, contactFriction=contactFriction, contactRestitution=contactRestitution, contactResponse=contactResponse, color=color, group=group, fileFFDDistanceGrid=fileFFDDistanceGrid, scale=scale, sampling=sampling, box=box, nx=nx, ny=ny, nz=nz, dumpfilename=dumpfilename, usePoints=usePoints, singleContact=singleContact, **kwargs)
