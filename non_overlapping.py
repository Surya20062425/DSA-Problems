class Solution:
    def eraseOverlapIntervals(self, intervals):

        if len(intervals) <= 1:
            return 0

        intervals.sort()

        removed = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:

            if start < prevEnd:
                removed += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end

        return removed
