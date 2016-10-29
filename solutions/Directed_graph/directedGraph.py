import sys

def isCyclicUtil(edgeList, u, visited, trace):
    if (visited[u] == False):
        visited[u] = True
        trace[u] = True
        for i in range(len(edgeList[u])):
            v = edgeList[u][i]
            if ((visited[v] == False) and (isCyclicUtil(edgeList, v, visited, trace))):
                return True
            elif (trace[v]):
                return True
    trace[u] = False
    return False

def isCyclic(edgeList, V):
    visited = [False] * V
    trace = [False] * V

    for each in range(V):
        if (isCyclicUtil(edgeList, each, visited, trace)):
            return True
    return False

def main():
    T = input()
    while T:
        (V, M) = map(int, raw_input().split())
        temp = map(int, raw_input().split())
        edgeList = [[] for i in range(V)]

        j = 0
        while j < len(temp):
            u = temp[j]
            v = temp[j+1]
            edgeList[u].append(v)
            j += 2

        if (isCyclic(edgeList, V)):
            print("1")
        else:
            print("0")
        T -= 1

if __name__ == "__main__":
    main()
