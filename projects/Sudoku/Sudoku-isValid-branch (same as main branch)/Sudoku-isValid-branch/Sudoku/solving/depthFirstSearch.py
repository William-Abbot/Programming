#python3!
#depthFirstSearch.py
#William Abbot

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
#Python, please allow implicit references again!!

from functions import isValid


'''
DFS(G):
    for each vertex u in G.V
        u.color = white
        u.pi = NULL
    time = 0
    for each vertex u in G.V
        if u.color == white
            DFS-Visit(G, u)

DFS-Visit(G, u):
    time += 1
    u.d = time
    u.color = gray
    for ech v in G.adj[u]
        if v.color == white
            v.pi = u
            DFS-Visit(G, v)
    u.color = black
    time += 1
    u.f = time

u.d = used to resord when DFS discovers vertex u
u.f = used to resord when DFS finds vertex u
'''

#skeleton
def DFS():
    return True
    
