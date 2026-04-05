"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        points = []
        for i in intervals:
            points.append((i.start, 1))
            points.append((i.end, -1))
        
        points.sort()

        overlap = 0
        res = 0
        for point,val in points:
            if overlap > 0:
                res = max(res, overlap)

            overlap += val

        return res

                 




