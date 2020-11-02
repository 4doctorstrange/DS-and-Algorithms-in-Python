#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#define MAX 100
#define initial 1
#define waiting 2
#define visited 3
int adj[MAX][MAX];
int n;// number of vertices;
int state[MAX];  //can be initial,waiting or visited
void create_graph();
void BF_Traversal();
void BFS(int v);
int queue[MAX],front=-1,rear=-1;
void insert_queue();
int delete_queue();
int isEmpty_queue();  
int  main(){
    create_graph();
    BF_Traversal();
    
    return 0;
}

void BF_Traversal(){
    int v;
    for(v=0;v<n;v++){
        state[v]=initial;
        printf("enter starting vertex for BFS: \n");
        scanf("%d ",&v);
        BFS(v);
        for(v=0;v<n;v++){
            if(state[v]==initial){
                BFS(v);           // to ensure every vertex is explored
            }
            
        }
    }
}

void BFS(int v){
    int i;
    insert_queue(v);
    state[v]=waiting;
    while(!isEmpty_queue()){
        v=delete_queue();
        printf("%d ",v);
        state[v]=visited;
        for(i=0;i<n;i++){
            if(adj[v][i]==1 && state[i]==initial){
                insert_queue(i);
                state[i]=waiting;
            }
        }
    }
    printf("\n");

}

void insert_queue(int vertex){
    if(rear==MAX-1){
        printf("Overflow \n");
    }
    else{
        if(front==-1){
            front=0;  ///queue is empty
        }
        rear=rear+1;
        queue[rear]=vertex;
    }
}
int isEmpty_queue(){
    if(front==-1||front>rear){
        return 1;
    }
    else{
        return 0;
    }
}

int delete_queue(){
    int del;
    if(front==-1 ||front>rear){
        printf("underflow\n");
        exit(1);
    }
    del=queue[front];
    front=front+1;
    return del;
}

void create_graph(){
    int max_edges,i,j,origin,destn;
    int graphtype;
    printf("1 for undirected or 2 for directed\n");
    scanf("%d",&graphtype);
    printf("enter number of vertices: ");
    scanf("%d",&n);
    if(graphtype==1){
        max_edges=n*(n-1)/2;
    }
    else{
        max_edges=n*(n-1);
    }
    for(i=0;i<max_edges;i++){
        printf("enter edge \n");
        scanf("%d %d ",&origin,&destn);
        //check for boundary condition is not mentioned

        adj[origin][destn]=1;
        if (graphtype==1){
            adj[destn][origin]=1;   //undirected is unsymmetric
        }
    }
    printf("The adjeaceny matrix is :\n");
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            printf("%d",adj[i][j]);
        }
        printf("\n");

    }

}