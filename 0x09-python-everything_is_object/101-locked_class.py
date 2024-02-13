#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if not hasattr(self, "first_name") and name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
        super().__setattr__(name, value)

print('lsl')
lc = LockedClass()
print(lc)
lc.first_name = "khaled"
print(lc.first_name)
try:
    lc.last_name = 'hsese'
    print(lc.last_name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
