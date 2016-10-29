def main():
	t=int(raw_input())
	while(t>0):
		t-=1
		n,m=map(int,raw_input().split())					#Input N and M
		edges=map(int,raw_input().split())					#Input M pairs of u and v (the edges)
		myGraph={}
		for i in range(m):
			if edges[2*i] not in myGraph:
				myGraph[edges[2*i]]=[]
			myGraph[edges[2*i]].append(edges[2*i+1])		#construct graph in from of a distionary of lists
		print graphChk(myGraph)								#call function to check for cycle

def graphChk(myGraph):	

	stack = [iter(myGraph)]									#stack to iterate through keys(nodes) of myGraph
	path = [object()]
	recPath = set(path)								
	visited = set()
	while stack:
		for node in stack[0]:								#iterate through stack
			if node in recPath:								#same node found again in current path, so there is a cycle
				return 1
			elif node not in visited:
				recPath.add(node)
				visited.add(node)
				path.append(node)
				stack.append(iter(myGraph.get(node, ())))	#add unvisited element in stack (kind of recursion)
				break
		else:
			ele=path.pop()
			recPath.remove(ele)
			stack.pop()
	return 0												#no cycle found

if __name__=='__main__':
	main()
