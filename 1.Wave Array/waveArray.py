class Solution:
    def convertToWave(n, a):
        for num in  range(int(n/2)):
            a[0 + (num * 2)] , a[1 + (num * 2)] = a[1 + (num * 2)] , a[0 + (num * 2)]
        print(*a, sep=" ")

print(Solution.convertToWave( 10 , [1,2,3,4,5,6,7,8,9,10]))