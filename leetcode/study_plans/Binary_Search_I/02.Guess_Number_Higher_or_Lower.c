int guessNumber(int n){
	long start = 1, end = n, m;
    while(start<=end){
        m = (start+end)/2;
        if(guess(m)==0){return m;}
        else if(guess(m)==-1){
            end=m-1;
        }else if(guess(m)==1){
            start=m+1;
        }
    }
    return -1;
}