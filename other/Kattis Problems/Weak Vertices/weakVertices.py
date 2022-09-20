#To solve this problem, I need to find all of the verticies that aren't
#   apart of a triangle. We’ll say vertex i is part of a triangle if i 
#   has two different neighbors j and k such that j and k are neighbors
#   of each other. Which means, a triangle is a k3 complete graph. At 
#   least one unique pair of neighbors of i must be connected (by an edge)
#   inorder for i to be a non-weak vertex.

'''
Sample input
0 1 1 1 0 0 0 0 0
1 0 0 0 0 0 1 0 0
1 0 0 1 0 1 0 0 0
1 0 1 0 0 1 1 0 0
0 0 0 0 0 0 1 1 0
0 0 1 1 0 0 0 0 0
0 1 0 1 1 0 0 1 0
0 0 0 0 1 0 1 0 1
0 0 0 0 0 0 0 1 0
'''

