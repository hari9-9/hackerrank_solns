class Solution:

    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        #code here
        l1 = list(s1)
        l2 = list(s2)
        l1.sort()
        l2.sort()
        return l1 ==l2
