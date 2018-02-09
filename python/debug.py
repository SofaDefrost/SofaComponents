import sofacomponents as Sofa
import codecs 

for j in Sofa.__all__:
    for k in Sofa.__dict__[j].__all__:
        print("Print: "+k)
        codecs.utf_8_decode( Sofa.__dict__[j].__dict__[k].__dict__[k].__doc__ )
