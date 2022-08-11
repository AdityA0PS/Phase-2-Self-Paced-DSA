class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        length = len(graph)
        visited = [False for i in range(length)]
        color = [None for i in range(length)]
        
        def recurse(index, prev_color=0):
            visited[index] = True
            color[index] = prev_color
            for i in graph[index]:
                if visited[i]:
                    if color[index] == color[i]:
                        return False
                else:
                    if not recurse(i,(prev_color+1) % 2):
                        return False
            return True
            
        for i in range(length):
            if not visited[i]:
                if not recurse(i):
                    return False
        
        return True