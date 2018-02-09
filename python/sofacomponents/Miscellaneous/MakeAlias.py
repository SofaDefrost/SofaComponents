# -*- coding: utf-8 -*-


"""
Component MakeAlias

.. autofunction:: MakeAlias

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MakeAlias(attachedTo , name='MakeAlias', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, targetcomponent='', alias='', **kwargs):
    """This object create an alias to a component name to make the scene more readable. 


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 targetcomponent: The component class for which to create an alias.

		 alias: The new alias of the component.


    """
    return attachedTo.createObject("MakeAlias" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, targetcomponent=targetcomponent, alias=alias, **kwargs)
