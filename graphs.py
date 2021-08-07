'''DIrected graphs 
def depth_first_iterative(graph,s):
    bucket = [s]
    while bucket:
        current = bucket.pop()
        print(current,end=" ")
        for neighbour in graph[current]:
            bucket.append(neighbour)

def depth_first_recurrsive(graph,s):
    print(s,end =" ")            #pritinting current node
    neighbours = graph[s]   #getting neighbours
    for neighbour in neighbours:         # iterating each neighbour
        depth_first_recurrsive(graph,neighbour)

def breadth_first(graph,s):
    queue=[s]
    while len(queue)>0:
        current=queue.pop(0)
        print(current,end=" ")
        for neighbour in graph[current]:
            queue.append(neighbour)


def has_path(graph,src,dest):  #to check if there exist a path between src and dest
    """ we will simply traverse the graph using bfs or dfs and cover each ndde from src"""
    if src == dest:
        return True
    neighbours = graph[src]
    for neighbour in neighbours:
        if has_path(graph,neighbour,dest):
            return True
        
    return False


graph = {
    'a':["b","c"],
    'b':["d"],
    'c':["e"],
    'd':["f"],
    'e':[],
    'f':[]
}
starting_node = 'a'
#depth_first_iterative(graph,starting_node)
#depth_first_recurrsive(graph,starting_node)
#breadth_first(graph,starting_node)
print(has_path(graph,"a","f"))
'''
#############################################################################################################
'''Undirected graphs

def undirectedPath(edge_list,src,dest):
    """this function will check for path between src and dest"""
    graph = buildGraph(edge_list) #used to convert edgelist to graph
    return hasPathQueue(graph,src,dest)


def buildGraph(edge_list):
    graph = {}
    for node in edge_list:

        #print(graph)
        if node[0] not in graph:  #if node not in graph then add node and set array of neighbors
            graph[node[0]] = [node[1]]
        else:                           #else append that neighbour
            graph[node[0]].append(node[1])
        
        if node[1] not in graph:
            graph[node[1]] = [node[0]]
        else:
            graph[node[1]].append(node[0])
    
    return graph

def hasPathQueue(graph,src,dest):
    queue=[src]
    visited = set()
    while queue:
        current = queue.pop(0)
        visited.add(current)  #adding current in visited to avoid loop codition
        if current == dest:
            return True
        for neighbour in graph[current] :  #appending neighbours in queue
            if neighbour not in visited:
                queue.append(neighbour)

    return False



edge_list =[
    ["i","j"],
    ["k","i"],
    ["m","k"],
    ["k","l"],
    ["o","n"],
]
print(undirectedPath(edge_list,"i","k"))
'''
##########################################################################################################
'''Connected Components

def connected_components(graph):
    visited = set()
    count=0
    for node in graph:
        if explore(graph,node,visited):     #traversing every node in graph
            count+=1
        
    return count


def explore(graph,s,visited):
    if s in visited:
        return False

    visited.add(s)  #if not visited then add
    for neighbour in graph[s]:
        explore(graph,neighbour,visited)
    
    return True  #when all the neighbours have been explored


graph = {
    0: [8,1,5],
    1: [0],
    5: [0,8],
    8: [0,5],
    2: [3,4],
    3: [2,4],
    4: [3,2]
}
print(connected_components(graph))
'''
############################################################################################
'''Getting Largest connected Component
def connected_components_max(graph):
    visited = set()
    largest=0
    
    for node in graph:
        size= explore(graph,node,visited)     #traversing every node in graph
        if size:
            largest = max(largest,size)
        
    return largest


def explore(graph,s,visited):
    if s in visited:
        return 0

    visited.add(s)  #if not visited then add
    size=1
    for neighbour in graph[s]:
        size += explore(graph,neighbour,visited)
    
    return size  #when all the neighbours have been explored


graph = {
    0: [8,1,5],
    1: [0],
    5: [0,8],
    8: [0,5],
    2: [3,4],
    3: [2,4],
    4: [3,2]
}
print(connected_components_max(graph))
'''
#############################################################################################################
''' SHORTEST PATH 
def shortest_path(edge_list,src,dest):
    """basically returns the count of edges between src and dest"""
    graph = buildGraph(edge_list)

    """ starting simple BFS algorithm with minor changes"""
    queue=[(src,0)]   #0 is distance of that node from source
    visited = set()
    while queue:
        current = queue.pop(0)      #current[0]->node / current[1]-> dist from src
        visited.add(current[0])
        if current[0] == dest:
            return current[1]    #return distance

        for neighbour in graph[current[0]]:
            if not neighbour in visited:
                distance_of_neighbour = current[1] + 1   #updating distance for the neighbour of current
                queue.append([neighbour,distance_of_neighbour])

    return -1 #when no path exist

def buildGraph(edge_list):
    graph = {}
    for node in edge_list:
        if node[0] not in graph:  
            graph[node[0]] = [node[1]]
        else:                           
            graph[node[0]].append(node[1])
        
        if node[1] not in graph:
            graph[node[1]] = [node[0]]
        else:
            graph[node[1]].append(node[0])
    
    return graph


edge_list = [
    ["w","x"],
    ["x","y"],
    ["z","y"],
    ["z","v"],
    ["w","v"],
]
print(shortest_path(edge_list,"w","y"))
'''
#######################################################################################################################
'''ISLAND GRAPH PROBLEM  '''
""" We are given a grid with water and island positions and have to calculate no. of island"""
"""Solved using connected component problem"""

def island_count(grid):
    visited=set()
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if explore(grid,row,col,visited):
                count+=1
    return count

def explore(grid,r,c,visited):
    inBoundRow = r>=0 and r<len(grid)    #for checking row and col 
    inBoundCol = c>=0 and c<len(grid[0])

    if inBoundRow==False or inBoundCol==False:
        return False                #simply return when not in bound

    if grid[r][c]=="w":
        return False                  #simply return if it is water

    if (r,c) in visited:              #simply return if r,c is visited
        return False                 

    #if all the base checks are passed, simply visit r,c and explore neighbours via DFS
    visited.add((r,c))

    explore(grid,r-1,c,visited)   #exploring north
    explore(grid,r,c-1,visited)    #exploring west
    explore(grid,r,c+1,visited)    #exploring east
    explore(grid,r+1,c,visited)   #exploring south
    """No need to worry about corner elements, inBound checks handles that efficiently"""

    return True        #return True when explored fully

grid = [
    ["w","l","w","w","w"],
    ["w","l","w","w","w"],
    ["w","w","w","l","w"],
    ["w","w","l","l","w"],
    ["l","w","w","l","l"],
    ["l","l","w","w","w"],
]

print(island_count(grid))


