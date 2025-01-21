def dfs(graph, root):
    visited = []
    stack = [root]
    
    while(stack):
        node = stack.pop() 
       
        if(node not in visited):
            visited.append(node)
            stack.extend(graph[node])
    return visited

ans = dict()

n = int(input())

m = int(input())
tmp = []
for i in range(n+1):
    tmp.append([])

for j in range(m):
    a,b = map(int,input().split())
    tmp[a].append(b)
    tmp[b].append(a)

for k in range(1,len(tmp)):
    if tmp[k]==[]:
        ans[k]=[]
    else:
        ans[k]=tmp[k]

print(len(dfs(ans,1))-1)