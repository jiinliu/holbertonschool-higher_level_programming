#!/usr/bin/python3
class SwimMixin:
    print("The creature swims!" )
    
    def swim(self):
        print("The creature is swimming!")
        
        
class FlyMixin:
    print("The creature flies!")
    
    def fly(self):
        print("The creature is flyjing!")

        
class Dragon(SwimMixin, FlyMixin):
    """A dragon can swim and fly."""
    def roar(self):
        print("The dragon raors!")
