# Solution 1 

from collections import Counter
def optimize_coins(coins):
    while True:
        # Step 1: Count the occurrences of each denomination
        count = Counter(coins)
        
        # Step 2: Filter denominations with at least two coins
        candidates = [x for x in count if count[x] >= 2]
        
        # Break if no candidates remain
        if not candidates:
            break
        
        # Step 3: Find the smallest denomination with at least two coins
        x = min(candidates)
        
        # Step 4: Find positions of the first two coins with denomination x
        positions = [i for i, coin in enumerate(coins) if coin == x]
        i, j = positions[0], positions[1]
        
        # Step 5: Replace coins at positions i and j with a coin of denomination 2 * x at position j
        coins[j] = 2 * x
        del coins[i]  # Remove the coin at the earlier position

    return coins

# Solution 2 

import collections
import heapq
def merge_denominations(nums):
    # Count occurrences of each denomination
    count = collections.Counter(nums)
    
    # Initialize a min-heap with unique denominations
    minheap = list(count.keys())
    heapq.heapify(minheap)
    
    res = []
    
    # Process until all values in the heap are processed
    while minheap:
        pop = heapq.heappop(minheap)
        
        if count[pop] < 2:
            # If there’s less than two occurrences, add it to the result
            res.append(pop)
        else:
            # Calculate pairs and remove them from the count
            pairs = count[pop] // 2
            count[pop] -= pairs * 2
            
            # Add the new merged denomination to the counter
            merged_value = pop * 2
            count[merged_value] += pairs
            
            # Only push the merged value if it's new or needs to be processed further
            if merged_value not in minheap:
                heapq.heappush(minheap, merged_value)
                
            # If an unpaired coin remains, add it to the result
            if count[pop] > 0:
                res.append(pop)
    
    return res
