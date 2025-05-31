#!/usr/bin/python3
class VerboseList(list):
 """A short, chatty list."""
 

 def apppend(self, item):
     super().append(item)
     print(f"Added [{item}] to the list.")
     
     
     def extend(self, iterable):
         items = list(iterable)
         super().extend(items)
         print(f"Extended the list with [{len(items)}] items.")
         
         
         def remove(self, item):
             print(f"Removing [{item}] from the list.")
             super().remove(item)
             
             
def ppop(self, index=-1):
    item = super().pop(index)
    print(f"Popped [{item}] from the list.")
    return item
 