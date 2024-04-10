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
no_of_nodes=int(input("enter no of nodes:"))
graph={chr(i+65):[]for i in range(no_of_nodes)}
for key in graph.keys():
    no_of_neighbours=int(input(f"no of neighbours of {key}:"))
    while no_of_neighbours>0:
        neighbour_tuple=input("enter weight and destination/neighbours").split()
        neighbour_tuple[0]=int(neighbour_tuple[0])
        graph[key].append((neighbour_tuple[0],neighbour_tuple[1]))
        no_of_neighbours_=1
start_vertex='A'
print(graph)
mst1=prim(graph,start_vertex,start_vertex)
print("mst:",mst1)
print("minimum spanning tree:")
mst_cost=0
for weight,source,dest in mst1:
    mst_cost+=weight
print("mst cost=",mst_cost)
