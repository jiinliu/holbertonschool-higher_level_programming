#!/usr/bin/python3
class Fish:
    def swim(self):
       print("The fish is swimming.")
    
    def habitat(self):
        print("The fish lives in water.")
        
        
class Bird:
    def fly(self):
        print("The bird is frying.")
        
    def habitat(self):
        print("The bird lives in the sky.")


class FlyingFish(Fish, Bird):
    """Multiple-inheritance demo: combines Fish + Bird."""
    
    def fly(self):
        print("The flying fish is soaring!")
        
    def swim(self):
        print("The flying fish is swimming!")
        
        def habitaat(self):
            print("The flying fish lives both in water and the sky!")
            
    if __name__ == "__main__":
        ff = FlyingFish()
        ff.swim()
        ff.fly()
        ff.habitat()
        print(FlyingFish.mro())
