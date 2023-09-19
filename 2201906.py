#Question 1:
def Exercise1(num):
    L=[] #initialize two empty arrays
    R=[]
    ans = [1 for i in range(len(num))]
    L = [1 for i in range(len(num))]     #initialise the elements to the left 
    R = [1 for i in range(len(num))]     #initialise the elements to the right
    for i in range(1,len(L)):
        L[i] = L[i-1]*num[i-1]      #modify left array of the elements
    for i in range(len(L)-2, -1, -1):
        R[i] = R[i+1]*num[i+1]    #modify right array in reverse order of elements
    for i in range(len(num)):
        ans[i] = L[i] * R[i] #result of left and right array
    return ans

#Question 2:
def Exercise2(matrix):
    up = 0      #initialize the top, right, bottom, and left boundaries
    right = len(matrix[0])-1
    down = len(matrix)-1
    left = 0
    result=[]    #initialize the output array
    while left <= right and up <= down:
        for i in range(left, right+1): #Traverse from left boundary to right boundary
            result.append(matrix[up][i])
        for i in range(up+1, down): #Traverse from up boundary to down boundary.
            result.append(matrix[i][right])
        for i in range(left, right+1)[::-1]: #traverse from right to left
            if up < down:
                result.append(matrix[down][i])
        for i in range(up+1, down)[::-1]: #traverse from down to up
            if left < right:
                result.append(matrix[i][left])

        left = left + 1 #move the boundaries by updating left, right, up, and down accordingly
        right = right - 1
        up = up + 1
        down = down - 1
            
    return result

#Question 3:
def Exercise3(nums1, nums2, nums3, nums4):
    result = 0
    d = {}    #initialise d
    for i in nums4 : 
        if i in d:
            d[i] = d[i] + 1
        else :
            d[i] = 1
    for a in range(len(nums1)): #loop iterates through nums1,nums2,nums3. Result value is increased if it is in d.
        for b in range(len(nums2)):
            for c in range(len(nums3)):
                if -(nums1[a] + nums2[b] + nums3[c]) in d:
                    result = result + 1
    return result

#Question 4:
def Exercise4(height):
    start = 0 # initialise start variable to demonstrate the leftt array
    end = len(height) - 1 # initialise end variable to present right array
    maxarea = 0
    while start < end:
        currentarea = (end - start) * min(height[start], height[end]) #calculate current area between 2 lines
        maxarea = max(maxarea, currentarea)  #compare calculated area and assigned maximum of two area to maxarea
        if height[start] < height[end]:
            start = start + 1
        else:
            end = end + 1
    return maxarea

#Question 5:
def Exercise5(nums):
    longest=0
    nums.sort()
    current=1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
          continue
        elif nums[i] == nums[i-1]+1:
          current = current+1
        else:
          longest=max(current, longest)
          current=1
    return max(current, longest)

#Question 6:
def Exercise6(nums):
    nums.sort()   #sort the nums list
    for i in range(1,len(nums)):
        if nums[i]==nums[i-1]:
            return nums[i]

#Question 7:
def Exercise7(s,k):
    left=0 #create left, right, maxlen
    right=0
    maxlen=0
    d={}
    for right in range(len(s)):
        right_character= s[right]
        if right_character not in d:
            d[right_character]=0
        d[right_character] += 1
        while len(d)>k:
            left_character = s[left]
            d[left_character] -= 1
            if d[left_character]==0:
                del d[left_character]
            left+=1
        maxlen=max(maxlen, right-left+1)
    return maxlen

#Question 8:
def Exercise8(nums, k):
    if len(nums) * k == 0:
        return []
    if k == 1:
        return nums
    left = [0] * len(nums)
    left[0] = nums[0]
    right = [0] * len(nums)
    right[len(nums) - 1] = nums[len(nums) - 1]
    for i in range(1, len(nums)):
        if i % k == 0:
            left[i] = nums[i]
        else:
            left[i] = max(left[i - 1], nums[i])
        j = len(nums) - i - 1
        if (j + 1) % k == 0:
            right[j] = nums[j]
        else:
            right[j] = max(right[j + 1], nums[j])
        
    result = []
    for i in range(len(nums) - k + 1):
        result.append(max(left[i + k - 1], right[i]))
            
    return result

#Question 9:
def Exercise9(s, t):
    L=0
    R=0
    minlen = len(s)+1
    d = {}
    result = ""
    if not s or not t: #if no such substring, return ""
        return ""
    for i in t:
        d[i] = d.get(i,0) + 1
        count = 0 
    while R<len(s):    #loop iterate over s
        if s[R] in d:  #if predent in d, decrement d
            d[s[R]] -=1 
            if d[s[R]]>=0:
                count+=1
            while count == len(t): 
                if R - L + 1 < minlen:
                    minlen = R - L + 1 #update min len
                    result = s[L:R+1]
                if s[L] in d: 
                    d[s[L]] +=1
                    if d[s[L]] > 0 :
                        count -=1
                L +=1    #increment start array
        R +=1            #increment end array
    return result

#Question 10:
class Cache:
    def __init__(self, capacity: int):                          

        self.capacity = capacity

        self.d = {}          #key-value pair is stored dictionary

        self.lcache = []                #track item insertion order

    def get(self, key: int) -> int:

        if key not in self.d:               #if key is not in cache, return -1

            return -1

        self.lcache.remove(key)              #If exists, obtain key value and update list

        self.lcache.append(key)

        return self.d[key]

    def put(self, key: int, value: int) -> None:

        if key in self.d:                     #if key is in cache, remove it

             self.lcache.remove(key)

        elif len(self.lcache) >= self.capacity:  #if cache is in its capacity, previous item is removed and new key-value pair is added

            previous = self.lcache.pop(0)

            del self.d[previous]

        self.lcache.append(key)

        self.d[key] = value

C = Cache(2)
