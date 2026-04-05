class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda e:e[0])
        merged_start, merged_end = intervals[0]
        res = []

        for start, end in intervals[1:]:
            if start <= merged_end:
                merged_end = max(end, merged_end)
                merger_start = min(start, merged_start)
            
            else:
                res.append([merged_start, merged_end])
                merged_start, merged_end = start, end

        res.append([merged_start, merged_end])

        return res

                

        


                