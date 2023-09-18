print('danar')


def getsum(arr, n):
   if n % 2 == 0:
      return 0
   Sum = 0
   for i in range(n):
      Sum += arr[i]
   return Sum
