class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []


        events = []
        for s, e in intervals:
            events.append((s, +1))
            events.append((e, -1))

        events.sort(key=lambda x: (x[0], -x[1]))

        active = 0
        start = None
        merged = []

        for x, d in events:
            prev = active
            active += d
            
            if prev == 0 and active == 1:
                start = x
                
            if prev == 1 and active == 0:
                merged.append([start, x])
                
        return merged
