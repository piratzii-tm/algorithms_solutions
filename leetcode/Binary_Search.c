int search(int* nums, int numsSize, int target){
    int start=0, end=numsSize-1,m;
    while(start<=end){
        m=(start+end)/2;
        if(target == nums[m]){return m;}
        else if(target > nums[m]){
            start = m+1;
        }else if(target < nums[m]){
            end = m-1;
        }
    }
    return -1;
}