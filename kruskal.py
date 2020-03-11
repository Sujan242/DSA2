from disjointsets import DisjointSets, Node

def kruskal(G):

    G=sorted(G)
    # print(G)
    ds = DisjointSets()
    
    nodes = []
    for i in range(len(G)):
        node = ds.makeset(i)
        nodes.append(node)


    wt=0
    for w,u,v in G:

        if ds.findset(nodes[u]) != ds.findset(nodes[v]):
            wt+=w
            ds.union(nodes[u],nodes[v])
    print(wt)

def main():
    ''' Adjacency List representation. G is a list of lists. '''
    G = [] 

    file=open('input1.txt','r')
    k=-1
    for line in file:
        k+=1
        line=line.strip()
        adjacentVertices = []
        first=True
        for edge in line.split(' '):
            if first:
                first=False

                continue
            node,weight = edge.split(',')
            # adjacentVertices.append((int(node),int(weight)))
            G.append([int(weight),k,int(node)])
        # G.append(adjacentVertices)

    file.close()

    # print(G)
    kruskal(G)

if __name__ == '__main__':
    main()
