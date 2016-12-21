#!/usr/bin/env python
#-*- coding:utf8 -*-

import yaml, pprint

dd = {'age': 18, 'name': 'steve', 'work': 'IT'}
with open('yamltest.yaml','w') as yaml_file:
    yaml_file.write(yaml.dump(dd,default_flow_style=False))

with open('yamltest.yaml','r') as yaml_file:
    d1 = yaml.load(yaml_file)

print d1
pprint.pprint(d1)