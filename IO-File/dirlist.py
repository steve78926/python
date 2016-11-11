#coding:utf8
#author: 李宁
import os
import time
#mydir=input('请输入您想查询的路径: ')
def mytree(mydir,level=1):
	if level == 1:
		print(mydir)
	filelist=os.listdir(mydir)
	#filelist.sort()
	for file in filelist:
		print('%s|-- %s' %('|   '* (level-1),file))
		if os.path.isdir(os.path.join(mydir,file)):
			mytree(os.path.join(mydir,file),level+1)

mytree(".",1)