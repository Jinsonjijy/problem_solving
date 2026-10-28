"""
297. Capacity to Ship Packages Within D Days
You are given an array weights where weights[i] represents the weight of the i-th package on a conveyor belt. All the packages must be shipped in the order given from one port to another within days days.

Each day, the ship can carry a contiguous sequence of packages, as long as the total weight does not exceed its maximum capacity.

Your task is to find the minimum possible capacity of the ship so that all packages can be shipped within the given number of days.

Example 1:
Input: weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days = 5

Output: 15

Explanation:

Minimum ship capacity = 15. One way to ship in 5 days:

Day 1: 1 + 2 + 3 + 4 + 5 = 15
Day 2: 6 + 7 = 13
Day 3: 8
Day 4: 9
Day 5: 10
No day exceeds capacity 15 and all packages are shipped in order in 5 days.

Example 2:
Input: weights = [3, 2, 2, 4, 1, 4], days = 3

Output: 6

Explanation:

One possible division with capacity 6:

Day 1: 3 + 2 = 5
Day 2: 2 + 4 = 6
Day 3: 1 + 4 = 5
All packages shipped in order within 3 days
"""
def find_minimum_capacity(weights,days):
    l=max(weights)
    r=sum(weights)
    ans=r
    while l<=r:
        mid=(l+r)//2
        day_needed=1
        current_weight=0
        for weight in weights:
            if current_weight+weight<=mid:
                current_weight=current_weight+weight
            else:
                day_needed+=1
                current_weight=weight
        if day_needed<=days:
            ans=mid
            r=mid-1
        else:
            l=mid+1
    return ans


if __name__=="__main__":
    weights=list(map(int,input().split(" ")))
    days=int(input(""))
    print(find_minimum_capacity(weights,days))