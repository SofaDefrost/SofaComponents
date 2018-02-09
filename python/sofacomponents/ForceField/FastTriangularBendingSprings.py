# -*- coding: utf-8 -*-


"""
Component FastTriangularBendingSprings

.. autofunction:: FastTriangularBendingSprings

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def FastTriangularBendingSprings(attachedTo , name='FastTriangularBendingSprings', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, bendingStiffness=1.0, minDistValidity=1e-06, edgeInfo='', **kwargs):
    """Springs added to a triangular mesh to prevent bending


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 bendingStiffness: bending stiffness of the material

		 minDistValidity: Distance under which a spring is not valid

		 edgeInfo: Internal edge data


    """
    return attachedTo.createObject("FastTriangularBendingSprings" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, bendingStiffness=bendingStiffness, minDistValidity=minDistValidity, edgeInfo=edgeInfo, **kwargs)
