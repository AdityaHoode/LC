from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key][timestamp]=value

    def get(self, key: str, timestamp: int) -> str:
        if not self.time_map[key]:
            return ""
        else:
            saved_timestamps=list(self.time_map[key].keys())
            target=timestamp
            l,r=0,len(saved_timestamps)-1
            while l<=r:
                m=(l+r)//2
                if target>saved_timestamps[m]:
                    l=m+1
                elif target<saved_timestamps[m]:
                    r=m-1
                else:
                    return self.time_map[key][target]
            if r<0:
                return ""
            else: 
                return self.time_map[key][saved_timestamps[r]] 

# Optimized - used dict of list of tuples instead of dict of dict
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.time_map=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.time_map[key] or timestamp<self.time_map[key][0][0]:
            return ""
        l,r=0,len(self.time_map[key])-1
        while l<=r:
            m=(l+r)//2
            if timestamp>self.time_map[key][m][0]:
                l=m+1
            elif timestamp<self.time_map[key][m][0]:
                r=m-1
            else:
                return self.time_map[key][m][1]
        return self.time_map[key][r][1]

            