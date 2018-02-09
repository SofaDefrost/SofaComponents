# -*- coding: utf-8 -*-


"""
Component MakeDataAlias

.. autofunction:: MakeDataAlias

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MakeDataAlias(attachedTo , name='MakeDataAlias', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, componentname='', dataname='', alias='', **kwargs):
    """This object create an alias to a data field. 


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 componentname: The component class for which to create an alias.

		 dataname: The data field for which to create an alias.

		 alias: The alias of the data field.


    """
    return attachedTo.createObject("MakeDataAlias" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, componentname=componentname, dataname=dataname, alias=alias, **kwargs)
