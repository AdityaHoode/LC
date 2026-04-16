from typing import List


class SummaryRanges:

    def __init__(self):
        self.nums = []

    def addNum(self, value: int) -> None:
        self.nums.append(value)
        self.nums = sorted(self.nums)

    def getIntervals(self) -> List[List[int]]:
        output=[]
        if not self.nums:
            return [[]]
        elif len(self.nums)==1:
            return [[self.nums[0], self.nums[0]]]
        i,j=0,1
        while(j<len(self.nums)):
            if self.nums[j]-self.nums[j-1]==1:
                j+=1
            else:
                output.append([self.nums[i], self.nums[j-1]])
                i=j
                j+=1
            if j==len(self.nums) and self.nums[j-1]-self.nums[j-2]==1:
                output.append([self.nums[i], self.nums[j-1]])
                return output
            elif j==len(self.nums) and self.nums[j-1]-self.nums[j-2]!=1:
                output.append([self.nums[j-1], self.nums[j-1]])
                return output
        return output

# Your SummaryRanges object will be instantiated and called as such:
summaryRanges = SummaryRanges()
summaryRanges.addNum(1)      # arr = [1]
print(summaryRanges.getIntervals()) # return [[1, 1]]
summaryRanges.addNum(3)      # arr = [1, 3]
print(summaryRanges.getIntervals()) # return [[1, 1], [3, 3]]
summaryRanges.addNum(7)      # arr = [1, 3, 7]
print(summaryRanges.getIntervals()) # return [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2)      # arr = [1, 2, 3, 7]
print(summaryRanges.getIntervals()) # return [[1, 3], [7, 7]]
summaryRanges.addNum(6)      # arr = [1, 2, 3, 6, 7]
print(summaryRanges.getIntervals()) # return [[1, 3], [6, 7]]