#1. Utopian Tree: https://www.hackerrank.com/challenges/utopian-tree/problem

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    if n==0:
        n=1
        return n
    else:
        a=1
        for i in range(1,n+1):
            if i%2==1:
                a*=2
            else:
                a+=1
        return a
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
#####################################################################################
#2. Picking Numbers: https://www.hackerrank.com/challenges/picking-numbers/problem
import math
import os
import random
import re
import sys
def pickingNumbers(a):
    maximum=0 
    for i in a:
        c=a.count(i)
        d=a.count(i-1)
        c=c+d
        if c > maximum:
            maximum=c
    return maximum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
#3. Validating and Parsing Email Addresses: https://www.hackerrank.com/challenges/validating-named-email-addresses/problem

import re
n=int(input(""))
for i in range(n):
    user,mail=input("").split(" ")
    if re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>',mail):
        print(user, mail)

#4. Mini-Max Sum: https://www.hackerrank.com/challenges/mini-max-sum/problem
import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    arr=sorted(arr)
    min=sum([i for i in arr[:len(arr)-1]])
    max=sum([i for i in arr[1:]])
    print(min,max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
