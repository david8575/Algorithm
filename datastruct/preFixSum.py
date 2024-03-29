import sys
input = sys.stdin.readline
def preFix(nums):
    preFixSum = [0]
    for num in nums:
        preFixSum.append(preFixSum[-1] + num)
    return preFixSum