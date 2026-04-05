"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        d = defaultdict(int)
        for interval in intervals:
            d[interval.start]+=1
            d[interval.end]-=1

        have,result = 0,0
        for i in sorted(d):
            have += d[i]
            result=max(result,have)
        
        return result


