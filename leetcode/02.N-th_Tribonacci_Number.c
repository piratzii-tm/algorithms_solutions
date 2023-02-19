int tribonacci(int n){
    if(n==0){return 0;}
    else if(n==1 || n==2){return 1;}
    else if(n==3){
        return 2;
    }
    
    int t1 = tribonacci(n-1);
    int t2 = tribonacci(n-4);

    return t1-t2+t1;
}