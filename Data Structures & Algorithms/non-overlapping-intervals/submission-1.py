class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i:i[0])
        prev_start, prev_end = intervals[0]
        res = []
        remove = 0

        for start, end in intervals:
            if start < prev_end:
                if end < prev_end:
                    res.append([start,end])
                    prev_start, prev_end = start, end
                else:
                    res.append([prev_start, prev_end])
                remove += 1
            else:
                res.append([start, end])
                prev_start, prev_end = start, end
        
        return remove-1



            