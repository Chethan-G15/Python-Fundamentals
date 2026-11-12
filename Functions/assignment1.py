"""1)maximum of three numbers """
def maxOfThree(*num):
    result=sorted(num,reverse=True)
    print(result[0])

maxOfThree(3,4,20,18,108)