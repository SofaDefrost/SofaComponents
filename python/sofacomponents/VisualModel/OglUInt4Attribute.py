# -*- coding: utf-8 -*-


"""
Component OglUInt4Attribute

.. autofunction:: OglUInt4Attribute

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def OglUInt4Attribute(attachedTo , name='OglUInt4Attribute', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, id='', indexShader=0, value=[], handleDynamicTopology=1, **kwargs):
    """OglUInt4Attribute


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 id: Set an ID name

		 indexShader: Set the index of the desired shader you want to apply this parameter

		 value: internal Data

		 handleDynamicTopology: Activate handling of topological changes on the values of this attribute (resizes only)


    """
    return attachedTo.createObject("OglUInt4Attribute" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, id=id, indexShader=indexShader, value=value, handleDynamicTopology=handleDynamicTopology, **kwargs)
