int singleNumber(int* nums, int numsSize) {
    if(1 == numsSize)
    {
        return nums[0];
    }

    while(1 != numsSize)
    {
        nums[0] ^= nums[numsSize - 1];
        numsSize--;
    }
    
    return nums[0];
}
