
# name:shivansh anand 21105125
  branch:ece

# In[22]:


# Python Program to demonstrate working of an algorithm that finds
# an element when size of array is unknown

# Binary search algorithm implementation
def binary_search(arr,l,r,x):

	if r >= l:           # r is high and l is low x is element to be serched
		mid = l+(r-l)//2

		if arr[mid] == x:
			return mid

		if arr[mid] > x:
			return binary_search(arr,l,mid-1,x)

		return binary_search(arr,mid+1,r,x)

	return -1

function takes an infinite size array(as the size is unknown) and a key to be searched and returns its position if found else -1. We don't know size of a[] and we can assume size to be infinite in this function.
 NOTE THAT THIS FUNCTION ASSUMES a[] TO BE OF INFINITE SIZE
Let p be the position of element to be searched. Number of steps for finding high index ‘h’ is O(Log p).
'h’ must be less than 2*p. The number of elements between h/2 and h must be O(p). Therefore, time complexity of Binary Search step is also O(Log p) and overall time complexity is 2*O(Log p) which is O(Log p)

def findPos(a, key):

	l, h, val = 0, 1, arr[0]

	# Find h to do binary search
	while val < key:
		l = h		 #store previous high
		h = 2*h		 #double the range of search, when the condition is satisfies then we call BINARY SEARCH on that range(low to high).
		val = arr[h]	 #update new val

	# at this point we have updated low and high indices,
	# thus use binary search between them
	return binary_search(a, l, h, key)

# Driver function
    

arr = [ 1,2,3,4,5,6,7,8,9,-1,-1,-1,-1,-1 ] #to find the position of the key in   infinte size array as explained earlier in line 29
ans = findPos(arr,8)
if ans == -1:
    print ("Element not found")
else:
    print("Element found at index",ans) 






