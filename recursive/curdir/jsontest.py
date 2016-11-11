

import json

class student(object):
    def __init__(self,name,age,score):
        self.name= name
        self.age = age
        self.score = score

    def func(self):
        print "%s age: %d, score:%d" % (self.name,self.age,self.score)

s = student('bob', 20, 80)
json_str = json.dumps(s,default=lambda obj : obj.__dict__)
print json.loads(json_str)
