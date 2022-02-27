class Solution:
    def isAnagram(self, s, t):
        m1, m2 = {}, {}
        for i in set(s):
            m1[i] = s.count(i)
        for j in set(t):
            m2[j] = t.count(j)
        return m1 == m2
    