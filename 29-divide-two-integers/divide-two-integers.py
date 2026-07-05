class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign1=1
        sign2=1
        if dividend<0 :
            sign1=-1
        if divisor<0:
            sign2=-1
        val=abs(dividend)//abs(divisor)
        if val*sign1*sign2>2**31-1:
            return 2**31-1
        elif val*sign1*sign2<-(2**31):
            return -(2**31)
        else:
            return val*sign1*sign2