class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        rev_num = []
        num_str=str(x)
        for item in num_str:
            rev_num.insert(0, item)
        str1 = ''.join(rev_num)
        int_rev = int(str1)
        if int_rev == x:
            return True
        else:
            return False