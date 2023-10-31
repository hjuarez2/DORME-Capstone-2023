# This program will be run to initate total functionality of DORM-E 

import Course_Correction.py as cc
import Path_Selection.py as ps
import sensors as ss
import draft_pathfind.py as pf

if __name__ == "__main__":

    n = len(sys.argv)
    
    path = a_star(sys.argv[1], sys.argv[2], sys.argv[3])
    currentNode=sys.argv[1]

    for i in range(0,len(path)):
        driveto(currentNode,path[i])
    

