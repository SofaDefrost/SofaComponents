# -*- coding: utf-8 -*-


"""
Component TopologicalChangeProcessor

.. autofunction:: TopologicalChangeProcessor

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TopologicalChangeProcessor(attachedTo , name='TopologicalChangeProcessor', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=1, filename='', listChanges=array([], shape=(0, 1), dtype=int32), interval=0.0, shift=0.0, loop=0, useDataInputs=0, timeToRemove=0.0, pointsToRemove=array([], dtype=int32), edgesToRemove=array([], dtype=int32), trianglesToRemove=array([], dtype=int32), quadsToRemove=array([], dtype=int32), tetrahedraToRemove=array([], dtype=int32), hexahedraToRemove=array([], dtype=int32), saveIndicesAtInit=0, epsilonSnapPath=0.1, epsilonSnapBorder=0.25, draw=0, **kwargs):
    """Read topological Changes and process them.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 filename: input file name for topological changes.

		 listChanges: 0 for adding, 1 for removing, 2 for cutting and associated indices.

		 interval: time duration between 2 actions

		 shift: shift between times in the file and times when they will be read

		 loop: set to 'true' to re-read the file when reaching the end

		 useDataInputs: If true, will perform operation using Data input lists rather than text file.

		 timeToRemove: If using option useDataInputs, time at which will be done the operations. Possibility to use the interval Data also.

		 pointsToRemove: List of point IDs to be removed.

		 edgesToRemove: List of edge IDs to be removed.

		 trianglesToRemove: List of triangle IDs to be removed.

		 quadsToRemove: List of quad IDs to be removed.

		 tetrahedraToRemove: List of tetrahedron IDs to be removed.

		 hexahedraToRemove: List of hexahedron IDs to be removed.

		 saveIndicesAtInit: set to 'true' to save the incision to do in the init to incise even after a movement

		 epsilonSnapPath: epsilon snap path

		 epsilonSnapBorder: epsilon snap path

		 draw: draw information


    """
    return attachedTo.createObject("TopologicalChangeProcessor" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, filename=filename, listChanges=listChanges, interval=interval, shift=shift, loop=loop, useDataInputs=useDataInputs, timeToRemove=timeToRemove, pointsToRemove=pointsToRemove, edgesToRemove=edgesToRemove, trianglesToRemove=trianglesToRemove, quadsToRemove=quadsToRemove, tetrahedraToRemove=tetrahedraToRemove, hexahedraToRemove=hexahedraToRemove, saveIndicesAtInit=saveIndicesAtInit, epsilonSnapPath=epsilonSnapPath, epsilonSnapBorder=epsilonSnapBorder, draw=draw, **kwargs)
