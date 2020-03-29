# I'm going to need graph and queue boilerplate here, as setup. Then bfs in main function

class Queue():
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    
    def size(self):
        return len(self.queue)

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError("vertex does not exist")
    
    def get_neighbors(self, vertex_id):
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("vertext does not exist")

def earliest_ancestor(ancestors, starting_node):
    # same as yesterday, except we're returning the longest path, not the shortest, and we need to build the graph first, since it's a separate function.
    graph = Graph()

    #looking at the test file, it seems like there are pairs of parent/child relationships - a matrix.
    for pair in ancestors:
        #add each pair 
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # connect the nodes via directed edge, going from child to parent
        graph.add_edge(pair[1], pair[0])

    #bfs with a little tweak. What we did before will return the shortest path, and we want the longest. That means we need to check path lengths against each other, and save the longest. We also need to note the oldest ancestor.
    queue = Queue()
    queue.enqueue([starting_node])
    oldest_ancestor = -1
    longest_path = 1

    while queue.size() > 0:
        path = queue.dequeue()
        current_vertex = path[-1]
        
        if len(path) == longest_path and current_vertex < oldest_ancestor:
            oldest_ancestor = current_vertex
            longest_path = len(path)
        if len(path) > longest_path:
            oldest_ancestor = current_vertex
            longest_path = len(path)
        
        for neighbor in graph.get_neighbors(current_vertex):
            new_path = list(path)
            new_path.append(neighbor)
            queue.enqueue(new_path)
    
    return oldest_ancestor
 

    

