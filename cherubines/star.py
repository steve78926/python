#!/usr/bin/env python
#-*- coding: utf-8 -*-

nspace = 10
nstar = 1

while nspace >0:
    spaces = ' ' * nspace
    stars = '*' * nstar
    print spaces + stars
    nspace -= 1
    nstar += 2

#print 'nspace:',nspace
#print 'nstar:',nstar
mspace = nspace +1
mstar = nstar - 1

while mstar > 0:
    spaces = ' ' * mspace
    starts = '*' * mstar
    print spaces + starts
    mstar -= 2
    mspace += 1

