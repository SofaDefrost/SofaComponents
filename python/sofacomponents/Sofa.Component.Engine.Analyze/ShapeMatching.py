# -*- coding: utf-8 -*-


"""
Component ShapeMatching

.. autofunction:: ShapeMatching

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ShapeMatching(attachedTo , name='ShapeMatching', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, iterations=1, affineRatio=0.0, fixedweight=1.0, fixedPosition0=array([], shape=(0, 3), dtype=float64), fixedPosition=array([], shape=(0, 3), dtype=float64), position=array([], shape=(0, 3), dtype=float64), cluster=array([], shape=(0, 1), dtype=int32), targetPosition=array([], shape=(0, 3), dtype=float64), **kwargs):
    """Compute target positions using shape matching deformation method by Mueller et al.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 iterations: Number of iterations.

		 affineRatio: Blending between affine and rigid.

		 fixedweight: weight of fixed particles.

		 fixedPosition0: rest positions of non mechanical particles.

		 fixedPosition: current (fixed) positions of non mechanical particles.

		 position: Input positions.

		 cluster: Input clusters.

		 targetPosition: Computed target positions.


    """
    return attachedTo.createObject("ShapeMatching" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, iterations=iterations, affineRatio=affineRatio, fixedweight=fixedweight, fixedPosition0=fixedPosition0, fixedPosition=fixedPosition, position=position, cluster=cluster, targetPosition=targetPosition, **kwargs)
