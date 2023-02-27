# -*- coding: utf-8 -*-


"""
Component TetrahedronCollisionModel

.. autofunction:: TetrahedronCollisionModel

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TetrahedronCollisionModel(attachedTo , name='TetrahedronCollisionModel', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, active=1, moving=1, simulated=1, selfCollision=0, proximity=0.0, contactStiffness=10.0, contactFriction=0.0, contactRestitution=0.0, contactResponse='', color=array([1., 0., 0., 1.], dtype=float32), group=[], numberOfContacts=0, **kwargs):
    """collision model using a tetrahedral mesh, as described in BaseMeshTopology


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

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

		 numberOfContacts: Number of collision models this collision model is currently attached to


    """
    return attachedTo.createObject("TetrahedronCollisionModel" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, active=active, moving=moving, simulated=simulated, selfCollision=selfCollision, proximity=proximity, contactStiffness=contactStiffness, contactFriction=contactFriction, contactRestitution=contactRestitution, contactResponse=contactResponse, color=color, group=group, numberOfContacts=numberOfContacts, **kwargs)
