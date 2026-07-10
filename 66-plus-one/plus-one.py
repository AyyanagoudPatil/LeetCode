class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(-1,-len(digits)-1,-1):
            if i!=(-len(digits)):
                if digits[i]<9:
                    digits[i]+=1
                    break
                else:
                    digits[i]=0
            else:
                if digits[i]<9:
                    digits[i]+=1
                else:    
                    digits[i]=0
                    digits.insert(0,1)
        return digits