# 3483. Unique 3-Digit Even Numbers - Easy
class Solution(object):
    def totalNumbers(self, d):
        # hashtable and brute force 
        n = len(d)
        seen = set()

        for i in range(n):
            if d[i]==0:
                continue
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k==j or k == i:
                        continue
                    if d[k] % 2 == 1:
                        continue
                    num = d[i] * 100 + d[j] * 10 + d[k]

                    seen.add(num)
        return len(seen)


        

class Solution2(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        freq = [0] * 10
        count = 0

        for i in digits:
            freq[i]+=1
        
        for i in range(1,9):
            if freq[i]==0:
                continue
            freq[i]-=1
            for j in range(9):
                if freq[j]==0:
                    continue
                freq[j]-=1
                for k in range(0,9,2):
                    if freq[k]>0:
                        count+=1
                freq[j]+=1
            freq[i]+=1
        
        return count


        