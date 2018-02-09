# -*- coding: utf-8 -*-


"""
Component TriangularBendingSprings

.. autofunction:: TriangularBendingSprings

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TriangularBendingSprings(attachedTo , name='TriangularBendingSprings', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, edgeInfo='', stiffness=100000.0, damping=1.0, **kwargs):
    """Springs added to a triangular mesh to prevent bending


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 edgeInfo: Internal edge data

		 stiffness: uniform stiffness for the all springs

		 damping: uniform damping for the all springs


    """
    return attachedTo.createObject("TriangularBendingSprings" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, edgeInfo=edgeInfo, stiffness=stiffness, damping=damping, **kwargs)
