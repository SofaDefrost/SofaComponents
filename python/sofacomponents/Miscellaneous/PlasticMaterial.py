# -*- coding: utf-8 -*-


"""
Component PlasticMaterial

.. autofunction:: PlasticMaterial

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def PlasticMaterial(attachedTo , name='PlasticMaterial', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, poissonRatio=0.45, youngModulus=3000.0, **kwargs):
    """Plastic material


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 poissonRatio: Poisson ratio in Hooke's law

		 youngModulus: Young modulus in Hooke's law


    """
    return attachedTo.createObject("PlasticMaterial" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, poissonRatio=poissonRatio, youngModulus=youngModulus, **kwargs)
