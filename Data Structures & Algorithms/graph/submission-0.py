class Graph:
    
    def __init__(self):
        self.adj_list = {} # src -> Set() of neighbors

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj_list:
            self.adj_list[src] = set()
        if dst not in self.adj_list:
            self.adj_list[dst] = set()
        self.adj_list[src].add(dst)   

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list[src]:
            return False
        self.adj_list[src].remove(dst)
        return True 


    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        return self.dfs(src,dst,visited)


    def dfs(self, src, dst, visited):
        if src == dst:
            return True
        
        visited.add(src)
        for neighbor in self.adj_list.get(src, set()):
            if neighbor not in visited:
                if self.dfs(neighbor, dst, visited):
                    return True
        return False 