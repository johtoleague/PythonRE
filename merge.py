
def merge(nums1:list[int], m: int, nums2: list[int], n: int) -> None:
    p1 = m - 1 # gives len of list 1
    p2 = n - 1 # gives leng of list 2
    p = m + n - 1 #len of combined list
    
    while p1 >= 0 and p2 >=0:
        if nums1[p1] <= nums2[p2]: # check to which list is higher
            nums1[p] = nums2[p2] # if list 2 is greater or equal put that value in that higher pointer location in the highest indexed loc of p (the combined index)
            p2 -= 1 # since p2 was assigned, we subtract one from the list
        else: 
            nums1[p] = nums1[p1] # since p1 is greater we assign it into the highest indexed location in the combined index of p
            p1 -= 1 # decrement p1, since we've assigned it
        p -= 1 # decrement p

    while p2 >=0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
        
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)
print(nums1) 


