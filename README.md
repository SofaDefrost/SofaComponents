# SofaComponent
This library contains only auto-generated wrapper around Sofa component so they can be used 
in an easy way in our plugins. 

Eg: 
```python
from sofacomponents.ForceField import TetrahedronFEMForceFIeld

def createScene(rootNode):
    TetrahedronFEMForceField(rootNode)
```

A very usefull side effect of this library is that there is also an auto-generated documentation on [readthedocs](http://sofacomponents.readthedocs.io/en/latest/index.html)

