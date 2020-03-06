# In python, heap is represented by list [ ]

# let's say the list is arr

# it also has moudule heapq, the main functions are:

heapify(iterable)

heappop(arr): only pop the smallest item

heappush(arr,val): push the val into the heap

heappushpop(arr, val)：push the val in the heap and pop the samllest one

heapreplace(arr, val)：pop the samllest first and push the new val

nlargest(k, iterable, key = fun): pop the kth largest val

nsmallest(k, iterable, key = fun) : pop the kth smallest val

# heapify: given node with val, find children nodes: 

# left node：2*i+1, right node: 2*i+2

# given node with val, find parent node: (2i-2)/2

# According to the example from the documentation, you can use tuples, and it will sort by the first element of the tuple, Note that if the first elements in a pair of tuples are equal, further elements will be compared. If this is not what you want, you need to ensure that each first element is unique.

import heapq

heap = []
heapq.heappush(heap, (0,'one', 1))
heapq.heappush(heap, (1,'two', 11))
heapq.heappush(heap, (1, 'two', 2))
heapq.heappush(heap, (1, 'one', 3))
heapq.heappush(heap, (1,'two', 3))
heapq.heappush(heap, (1,'one', 4))
heapq.heappush(heap, (1,'two', 5))
heapq.heappush(heap, (1,'one', 1))

show_tree(heap)
output:

#                                       (0, 'one', 1)                                       
#                 (1, 'one', 1)                                (1, 'one', 4)                
#     (1, 'one', 3)         (1, 'two', 3)         (1, 'two', 2)         (1, 'two', 5)     
# (1, 'two', 11)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.defaultdict(int)# defaultdict with int means when have dict[val] but val doesn't exits, it just create a new val with o as default
        heap = []
        if not nums:
            return []
        for i in nums:
            counter[i]+=1
        for key,value in counter.items():
            heapq.heappush(heap,(value,key)) # collections.heapq has all the functions of head like: heapify,push, pop, nlargest,nsmallest
            while len(heap)>k:
                heapq.heappop(heap)
        res=[]
        while len(heap) > 0:
            res.append(heapq.heappop(heap)[1])
        return res