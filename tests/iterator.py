import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from vector import *

try:
    xrange
except NameError:
    xrange = range


def main():
    v1 = Vector()

    n = 5
    f = [5, 9, 67, 65, 99]

    for x in xrange(0, int(n)):
        v1.push_back(f[x])


    # ================Print all element using begin() & end()==========================
    v = v1.begin()
    while v != v1.end():
        print (v[0])
        v +=1


    # =====================Print all element using cbegin() & cend()======================//
    # @ not implemented yet

    # ====================Print all element using crbegin() & crend()===================//
    # @ not implemented yet

    # =====================Print all element using rbegin() & rend()==========================//
    # @ not implemented yet


main()
