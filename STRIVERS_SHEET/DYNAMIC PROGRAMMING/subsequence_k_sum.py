"""
this is leetcode problem 560:


example:
    arr=[1,2,3]
    k=3
    output:2
    explanation: the [1,2] and [3] have sum 3 then return the number of subbarray

    arr=[1,5,11,5]
    k=11
    we get  subarray [1,5,5] and [11]
    in this approach i use a prefix sum and hashmap
    if the prefix - target in the hashmap then increament the count variable 
        
"""
if __name__=="__main__":
    arr=list(map(int,input().split(" ")))
    k=int(input("enter the sum :"))
    count=0
    prefix_sum=0
    freq={0:1}
    for num in arr:
        prefix_sum+=num
        if prefix_sum-k in freq:
            count+=freq[prefix_sum-k]
        freq[prefix_sum]=freq.get(prefix_sum,0)+1
    print(count)