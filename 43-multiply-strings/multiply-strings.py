class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        A=0
        B=0
        p=1
        q=1
        for i in range(-1,-len(num1)-1,-1):
            A+=(ord(num1[i])-48)*p
            p*=10
        for j in range(-1,-len(num2)-1,-1):
            B+=(ord(num2[j])-48)*q
            q*=10
        return str(A*B)