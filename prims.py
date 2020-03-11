
import heapq
def dj(G):

    n=len(G)
    labels=[1000000 for _ in range(n)]
    finished=[0 for _ in range(n)]
    labels[0]=0
    h=[[0,0]]
    heapq.heapify(h)
    # heapq.heappush(h,[1,2])
    # print(h)
    # d,u=heapq.heappop(h)
    # print(d,u)
    wt=0
    while len(h)>0:


        d,u=heapq.heappop(h)

        if finished[u]==1:
            continue
        finished[u]=1
        # print(u,d)
        wt+=d
        # print(d,u)
        # print(G[u])
        for v,w in G[u]:
            if labels[v]>w:
                labels[v]=w
                heapq.heappush(h,[w,v])
        # print(h)

    print(labels)
    print(wt)


def main():
    ''' Adjacency List representation. G is a list of lists. '''
    G = [] 

    file=open('input1.txt','r')
    for line in file:
        line=line.strip()
        adjacentVertices = []
        first=True
        for edge in line.split(' '):
            if first:
                first=False
                continue
            node,weight = edge.split(',')
            adjacentVertices.append((int(node),int(weight)))
        G.append(adjacentVertices)

    file.close()

    dj(G)

if __name__ == '__main__':
    main()
