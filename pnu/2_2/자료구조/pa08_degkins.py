edge = int(input())
first,second = map(str,input().split())
graph=[[first],[second]]

def maxlengh(list):
    count=0
    for k in range(len(list)):
        if len(list[k])>=count:
            count = len(list[k])
    return count


for k in range(edge-1):
    parent, child = map(str, input().split())
    for i in range(len(graph)):
        for j in range(maxlengh(graph)):
            if parent in graph[i]:
                if i != len(graph)-1:
                    graph[i+1].insert(0,child)
                    break
                elif i == len(graph)-1:
                    graph.append([child])
                    break
                else:
                    break
            elif child in graph[i]:
                if i !=0:
                    graph[i-1].insert(0,parent)
                    break
                elif i == 0:
                    graph.insert(0,[parent])
                    break
                else:
                    break
            else:
                break


newgraph=[]
for i in range(len(graph)):
    tmp = list(dict.fromkeys(graph[i]))
    newgraph.append(tmp)

A=str(input())
B=str(input())

x=0
y=0
for i in range(len(newgraph)):
    for j in range(len(newgraph[i])):
        if newgraph[i][j] == A:
            x = i
            break
for i in range(len(newgraph)):
    for j in range(len(newgraph[i])):
        if newgraph[i][j] == B:
            y = i
            break
print(x+y)