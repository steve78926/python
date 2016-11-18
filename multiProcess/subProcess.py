#coding:utf8
#coding:gbk

import subprocess

print ('$ ping -n 100 www.python.org')
r = subprocess.call(['ping','www.python.org','-n','100',])
print ('exit code:', r)