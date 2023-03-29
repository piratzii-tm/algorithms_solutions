#include<stdio.h>
#include<stdlib.h>

int ** aloc(int n, int m){
    int **mat = (int**)malloc(sizeof(int*));
    if(mat){
        for(int i=0;i<n;i++){
            mat[i] = (int *)calloc(m,sizeof(int));
        }
    }
    return mat;
}
void citire(int **mat, int n, int m){
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            scanf("%d",&mat[i][j]);
        }
    }
}
void dfs(int **mat, int n, int m, int i, int j){
    if(i<0 || i>=n || j<0 || j>=m || mat[i][j]!=1){return ;}
    mat[i][j] = 0;
    dfs(mat,n,m,i+1,j);
    dfs(mat,n,m,i,j+1);
    dfs(mat,n,m,i-1,j);
    dfs(mat,n,m,i,j-1);

}
int main(){
    int n,m;scanf("%d%d",&n,&m);
    int **mat;
    mat = aloc(n,m);
    citire(mat,n,m);

    int k=0;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(mat[i][j]==1){
                dfs(mat,n,m,i,j);k+=1;
            }
        }
    }

    printf("%d", k);

}