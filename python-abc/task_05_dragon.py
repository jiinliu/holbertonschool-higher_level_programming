#!/usr/bin/python3
class SwimMixin:
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """A dragon can swim and fly."""
    def roar(self):
        print("The dragon raors!")
