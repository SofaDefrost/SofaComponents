# -*- coding: utf-8 -*-


"""
Component GroupFilterYoungModulus

.. autofunction:: GroupFilterYoungModulus

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def GroupFilterYoungModulus(attachedTo , name='GroupFilterYoungModulus', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, groups='', primitives=[], elementsGroup=[], youngModulus=[], mapGroupModulus='', defaultYoungModulus=10000.0, groupModulus=[], **kwargs):
    """This class gives a vector of young modulus according of a list of defined groups


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 groups: Groups

		 primitives: Vector of primitives (indices)

		 elementsGroup: Vector of groups (each element gives its group

		 youngModulus: Vector of young modulus for each primitive

		 mapGroupModulus: Mapping between groups and modulus

		 defaultYoungModulus: Default value if the primitive is not in a group

		 groupModulus: list of young modulus for each group


    """
    return attachedTo.createObject("GroupFilterYoungModulus" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, groups=groups, primitives=primitives, elementsGroup=elementsGroup, youngModulus=youngModulus, mapGroupModulus=mapGroupModulus, defaultYoungModulus=defaultYoungModulus, groupModulus=groupModulus, **kwargs)
