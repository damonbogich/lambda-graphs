"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        visited = set()
        q.enqueue(starting_vertex)

        while q.size() > 0:
            removed_vertex = q.dequeue()
            
            if removed_vertex not in visited:
                visited.add(removed_vertex)
                print(removed_vertex)
                neighbors = self.get_neighbors(removed_vertex)

                for neighbor in neighbors:
                    q.enqueue(neighbor)



    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        visited = set()
        s.push(starting_vertex)

        while s.size() > 0:
            removed_vertex = s.pop()
            
            if removed_vertex not in visited:
                visited.add(removed_vertex)
                print(removed_vertex)
                neighbors = self.get_neighbors(removed_vertex)

                for neighbor in neighbors:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited == None:
            visited = set()
        
        print(starting_vertex)
        #add starting vertex to set
        visited.add(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex): #{2,3} {1,3}
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        visited = set()
        q.enqueue([starting_vertex])

        while q.size() > 0:
            removed_path = q.dequeue()
            current_vertex = removed_path[-1]

            if current_vertex == destination_vertex:
                return removed_path
            
            if current_vertex not in visited:
                if current_vertex == destination_vertex:
                    return removed_path

                visited.add(current_vertex)
                neighbors = list(self.get_neighbors(current_vertex))

                #we need to get copies of the path that was removed,
                neighbor_paths_container = []
                for i in range(len(neighbors)):
                    neighbor_paths_container.append(removed_path.copy())
                    neighbor_paths_container[i].append(neighbors[i])
                
                for path in neighbor_paths_container:
                    q.enqueue(path)
                #put them into a list
                #then add a neighbor to each one


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        visited = set()
        s.push([starting_vertex])

        while s.size() > 0:
            removed_path = s.pop()
            current_vertex = removed_path[-1]

            if current_vertex == destination_vertex:
                return removed_path
            
            if current_vertex not in visited:
                if current_vertex == destination_vertex:
                    return removed_path

                visited.add(current_vertex)
                neighbors = list(self.get_neighbors(current_vertex))

                #we need to get copies of the path that was removed,
                neighbor_paths_container = []
                for i in range(len(neighbors)):
                    neighbor_paths_container.append(removed_path.copy())
                    neighbor_paths_container[i].append(neighbors[i])
                
                for path in neighbor_paths_container:
                    s.push(path)

    def dfs_recursive(self, starting_vertex, destination_vertex, path = [], visited = set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        path = path + [starting_vertex]

        # if you have reached the destination return the current path
        if starting_vertex == destination_vertex:
            return path
       
        # loop through each neighbor of the current vertex
        for neighbor in self.get_neighbors(starting_vertex):
            # if you haven't visited the neighbor
            if neighbor not in visited:
                # vadd the neighbor to visited
                visited.add(neighbor)
                # recursively call the function to get a path from the neighbor to the end
                neighborpath = self.dfs_recursive(neighbor, destination_vertex, path.copy())
                # if the call of this function on the current neighbor found a path to the end
                if neighborpath is not None:
                    # return that path
                    return neighborpath
        # if no path to the end was found in any recursive calls we return None
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
