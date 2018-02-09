# -*- coding: utf-8 -*-


"""
Component GenerateRigidMass

.. autofunction:: GenerateRigidMass

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def GenerateRigidMass(attachedTo , name='GenerateRigidMass', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, density=1000.0, position=[], triangles=[], quads=[], polygons=[], rigidMass='1 1 [1 0 0,0 1 0,0 0 1]', mass=0.0, volume=0.0, inertiaMatrix=[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], massCenter=[[0.0, 0.0, 0.0]], centerToOrigin=[[0.0, 0.0, 0.0]], **kwargs):
    """An engine computing the RigidMass of a mesh : mass, volume and inertia matrix.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 density: input: Density of the object

		 position: input: positions of the vertices

		 triangles: input: triangles of the mesh

		 quads: input: quads of the mesh

		 polygons: input: polygons of the mesh

		 rigidMass: output: rigid mass computed

		 mass: output: mass of the mesh

		 volume: output: volume of the mesh

		 inertiaMatrix: output: the inertia matrix of the mesh

		 massCenter: output: the gravity center of the mesh

		 centerToOrigin: output: vector going from the mass center to the space origin


    """
    return attachedTo.createObject("GenerateRigidMass" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, density=density, position=position, triangles=triangles, quads=quads, polygons=polygons, rigidMass=rigidMass, mass=mass, volume=volume, inertiaMatrix=inertiaMatrix, massCenter=massCenter, centerToOrigin=centerToOrigin, **kwargs)
