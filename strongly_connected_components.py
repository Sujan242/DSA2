n=0
visited=[]
finish=[]
t=0
num=0
def dfs(g,u):
    global visited
    global finish
    global n
    global t
    global num
    num=num+1
    visited[u]=1
    # start[u]=t
    t=t+1
    
    for v in g[u]:
        if visited[v]==0:
            dfs(g,v)
    t=t+1
    finish.append(u)

def strongly_connected(G):
    global visited
    global finish
    global n
    global num
    
    # n=len(G)
    # print(n)
    visited=[0 for _ in range(n)]
    finish=[]
    g=[[] for i in range(n)]
    for u in range(n):
        for v in G[u]:
            g[v].append(u)
    # print(g)
    
    for u in range(n):
        if visited[u]==0:
            dfs(G,u)
    # print(finish)
    e=0
    o=0
    visited=[0 for _ in range(n)]
    while len(finish)>0:
        u = finish[-1]
        finish.pop()
        if visited[u]==1:
            continue
        
        num=0
        dfs(g,u)
        if (num%2==0):
            e+=num
        else:
            o+=num
            
    print(o-e)
           
def main():
    global n
    l=input().split(" ")
    n=int(l[0])
    m=int(l[1])
    G=[[] for _ in range(n)]
    for i in range(m):
        l=input().split()
        u=int(l[0])
        v=int(l[1])
        
        G[u-1].append(v-1)
        
        
    strongly_connected(G)
 
    
main()