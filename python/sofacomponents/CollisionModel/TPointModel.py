# -*- coding: utf-8 -*-


"""
Component TPointModel

.. autofunction:: TPointModel

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TPointModel(attachedTo , name='TPointModel', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, active=1, moving=1, simulated=1, selfCollision=0, proximity=0.0, contactStiffness=10.0, contactFriction=0.0, contactRestitution=0.0, contactResponse='', color='1 0 0 1', group=[], bothSide=0, computeNormals=0, PointActiverPath='', displayFreePosition=0, **kwargs):
    """Collision model which represents a set of points


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

		 bothSide: activate collision on both side of the point model (when surface normals are defined on these points)

		 computeNormals: activate computation of normal vectors (required for some collision detection algorithms)

		 PointActiverPath: path of a component PointActiver that activate or deactivate collision point during execution

		 displayFreePosition: Display Collision Model Points free position(in green)


    """
    return attachedTo.createObject("TPointModel" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, active=active, moving=moving, simulated=simulated, selfCollision=selfCollision, proximity=proximity, contactStiffness=contactStiffness, contactFriction=contactFriction, contactRestitution=contactRestitution, contactResponse=contactResponse, color=color, group=group, bothSide=bothSide, computeNormals=computeNormals, PointActiverPath=PointActiverPath, displayFreePosition=displayFreePosition, **kwargs)
