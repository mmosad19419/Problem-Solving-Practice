def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        indx = 0
        for element in nums:
            if element != val:
                nums[indx] = element
                indx +=1
        return indx, nums