# -*- coding: utf-8 -*-


"""
Component RuleBasedContactManager

.. autofunction:: RuleBasedContactManager

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def RuleBasedContactManager(attachedTo , name='RuleBasedContactManager', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, response='default', responseParams='', variables='', rules='', **kwargs):
    """Create different response to the collisions based on a set of rules


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 response: contact response class

		 responseParams: contact response parameters (syntax: name1=value1&name2=value2&...)

		 variables: Define a list of variables to be used inside the rules

		 rules: Ordered list of rules, each with a triplet of strings.
The first two define either the name of the collision model, its group number, or * meaning any model.
The last string define the response algorithm to use for contacts matched by this rule.
Rules are applied in the order they are specified. If none match a given contact, the default response is used.



    """
    return attachedTo.createObject("RuleBasedContactManager" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, response=response, responseParams=responseParams, variables=variables, rules=rules, **kwargs)
