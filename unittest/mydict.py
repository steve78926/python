#coding:utf8

class Dict(dict):
    '''
     Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):       #这里不要写成getter
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)      # r"Dict'     Dict的左侧少个单引号, 'Dict' 与第24行对应，如果第24行Dict没有'', 本行的Dict也不需要''

    def __setattr__(self, key, value):          #这里不要写成setter
        self[key] = value

if __name__ == '__main__':
    import doctest
    doctest.testmod()

