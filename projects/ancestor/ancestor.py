

from util import Stack, Queue
"""
Review example of finding 3's oldest ancestor
The tests aren't testing for it.  
What if one is put in to stack before 2...

Put in something that will check the lengths of 
the possible paths against each other,
returns the last node of the longest path
if two paths are tied for longest length, 
it will return the path with the smaller last node 
"""

def get_parents(starting_node, ancestors):
    parents = []
    for i in ancestors:
        if i[1] == starting_node:
            parents.append(i[0])
    return parents



def earliest_ancestor(ancestors, starting_node):
    #ancestors = [(parent, child), (parent, child), etc....]
    #DFT
    if get_parents(starting_node, ancestors) == []:
        return -1
    s = Stack()

    visited = set()

    s.push([starting_node])

    paths_to_ancestors = []

    while s.size() > 0:
        current_path = s.pop()
        current_node = current_path[-1]

        if current_node not in visited:
            visited.add(current_node)

            parents = get_parents(current_node, ancestors)

            if parents == []: #adding and s.size() == 0: to this and returning current node makes test pass, but shoulnt
                paths_to_ancestors.append(current_path)
                continue
                # return current_node
 
            path_container = []
            for i in range(len(parents)):
                path_container.append(current_path.copy())
                path_container[i].append(parents[i])
            
            print('hereeee', path_container)
            for path in path_container:     
                s.push(path)

   #below code is to handle if there are multiple ancestors
   #and how to find which one is oldest
    if len(paths_to_ancestors) == 1:
        return paths_to_ancestors[0][-1] 
    else:
        #find length of longest list(s) in paths to ancestor
        longest = paths_to_ancestors[0]
        longest_length = 0
        for path in paths_to_ancestors:
            if len(path) > len(longest):
                longest = path
        longest_length = len(longest)

        #find the oldest ancestor with the smallest number:
        potential_oldest_ancestors = []
        for path in paths_to_ancestors:
            if len(path) == longest_length:
                potential_oldest_ancestors.append(path[-1])
        return min(potential_oldest_ancestors)








    
   

