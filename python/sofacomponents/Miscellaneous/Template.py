# -*- coding: utf-8 -*-


"""
Component Template

.. autofunction:: Template

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def Template(attachedTo , name='Template', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, psl_source='', **kwargs):
    """An object template encoded as parsed hson-py object.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 psl_source: Current template source


    """
    return attachedTo.createObject("Template" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, psl_source=psl_source, **kwargs)
