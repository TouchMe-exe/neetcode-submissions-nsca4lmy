"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        points = []
        for i in intervals:
            points.append((i.start, 1))
            points.append((i.end, -1))
        
        points.sort()
        overlap = 0

        for point,val in points:
            overlap += val
            if overlap > 1:
                return False

        return True