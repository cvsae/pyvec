import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from vector import *




def main():
    v1 = Vector()

    n = 5
    f = [5, 9, 67, 65, 99]

    for x in xrange(0, int(n)):
        v1.push_back(f[x])




    # ================== Show value at position 2 using Reference Operator ===============
    print "\nReference operator v1[2]= %s " %v1[2]

    # ================== Show value at position 3 using at() =======================
    # @ not implemented yet

    # ===================Show the first element of the vector=============================
    print "\nFirst element of the vector is: %s" %v1.front()

    #================Show the last element of the vector==================================
    print "\nLast element of the vector is: %s " %v1.back() 
    
    #================Showing all the elements  using data=================================
    # @ not implemented yet




main() 