#coding:utf8

class Dict(dict):
    def __init__(self, **kwargs):
        super(Dict, self).__init__(**kwargs)

    def __getattr__(self,key):       #这里不要写成getter
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):          #这里不要写成setter
        self[key] = value

