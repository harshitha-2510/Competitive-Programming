import heapq
def prim(graph,start,dest):
    mst=[]
    visited=set()
    heap=[(0,start,dest)]
    while heap:
        weight,source,dest=heapq.heappop(heap)
        if dest not in visited:
            visited.add(dest)
            mst.append((weight,source,dest))
            for neighbor,neighbor_weight in graph[dest]:
                if neighbor not in visited:
                    heapq.heappush(heap,(neighbor_weight,dest,neighbor))
    return mst
graph={
    'A':[('B',7),('D',5)],
    'B':[('A',7),('C',8),('D',9),('E',7)],
    'C':[('B',8),('E',5)],
    'D':[('A',5),('B',9),('E',15),('F',6)],
    'E':[('B',7),('C',5),('D',15),('F',8)],
    'F':[('D',6),('E',8)]
    }
start_vertex='A'
mst1=prim(graph,start_vertex,start_vertex)
print("mst:",mst1)
print("minimum spanning tree:")
mst_cost=0
for weight,source,dest in mst1:
    mst_cost+=weight
print("mst cost=",mst_cost)

            
