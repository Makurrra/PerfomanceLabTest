import sys


file_path1 = sys.argv[1]

def readFile(file_path1):        
    with open(file_path1) as file:
        nums = list(map(int,file.read().split('\n')))
    return nums

def findMedian(nums):
    count = len(nums)
    median =  round(sum(nums)/count)
    return median

def countSteps(nums):
    median = findMedian(nums)
    count = sum(abs(i-median) for i in nums)
    print(count)
    return count

def main():
    countSteps(readFile(file_path1))

main()
