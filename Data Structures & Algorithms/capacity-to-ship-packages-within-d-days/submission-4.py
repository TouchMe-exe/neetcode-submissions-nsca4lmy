class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l, r = max(weights), sum(weights)
        res = r

        def count_days(m):
            days = 0
            i = 0
            while i<len(weights):
                capacity = 0
                while i<len(weights) and capacity + weights[i] <= m:
                    capacity += weights[i]
                    i += 1
                days += 1
            
            return days


        while l <= r:
            m = l + (r-l)//2

            m_days = count_days(m)

            if m_days <= days:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1

        return res




        