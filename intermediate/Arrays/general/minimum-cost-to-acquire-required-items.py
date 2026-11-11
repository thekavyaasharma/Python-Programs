# 3789. Minimum Cost to Acquire Required Items - Medium
class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        all_sep = (need1 * cost1) + (need2*cost2)

        common = min(need1, need2)
        rem1 = need1-common
        rem2 = need2- common

        comb_plus_sep = (costBoth * common) + (rem1*cost1) + (rem2*cost2)

        all_combos = max(need1,need2)*costBoth

        return min(all_sep, comb_plus_sep, all_combos)        