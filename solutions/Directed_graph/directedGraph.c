//C Program to check if there is any cycle in the given directed graph.
//If yes output is 1. Else it is 0

#include <stdio.h>
#include <stdlib.h>

typedef struct node{
	int vertex;
	struct node* next;
}node;

int flag;
node * head[10000];

//Function to insert elements in linked list
void insert(int a,int b)
{
	node *temp=(node*)malloc(sizeof(node));
	temp->vertex=b;
	temp->next=NULL;
	
	//If head is null insert it in the first
	if(head[a]==NULL)
		head[a]=temp;
	else
	{
		temp->next=head[a];
		head[a]=temp;
	}
}

//Function which checks cycle by dfs
void dfs(int i,int visited[],int stack[])
{
	if(!flag)
	{
		visited[i]=1;
		struct node* temp;
		temp=head[i];
		stack[i]=2;
		while(temp!=NULL)
		{
			int k=temp->vertex;
			//Cycle exists if stack[k]=2
			if(stack[k]==2)
			{
				flag=1;
				break;
			}
			else if(visited[k]==0)
				dfs(k,visited,stack);
			temp=temp->next;
		}
		stack[i]=1;
	}
}

int main()
{
	int t;
	scanf("%d",&t);
	while(t--)
	{
		int n,m;
		scanf("%d %d",&n,&m);

		//Visited array used in dfs.Set to 1 on visiting every child of the element
		//Stack array used in dfs to detect cycle.Set to 2 on visting the element.Then set to 1 after visiting every child
		int i,stack[n],visited[n];
		
		//Flag is 1 if there is a cycle
		flag=0;

		for(i=0;i<n;i++)
		{
			head[i]=NULL;
			stack[i]=0;
			visited[i]=0;
		}
		for(i=1;i<=m;i++)
		{
			int a,b;
			scanf("%d %d",&a,&b);
			insert(a,b);
		}
		for(i=0;i<n;i++)
		{
			if(!flag)
				dfs(i,visited,stack);
			else
				break;
		}
		if(flag)
			printf("1\n");
		else
			printf("0\n");
	}
	return 0;
}
