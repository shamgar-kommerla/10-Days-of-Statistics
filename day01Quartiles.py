
def medianFinder(arr):
    arr.sort()
    size = len(arr)
    if size%2 ==0:
        median = ((arr[int(size/2)-1]+arr[int(size/2)])/2)
    else:
        median = (arr[int((size+1)/2)-1])
    return int(median)

def quartiles(arr):
    arr.sort()
    size = len(arr)
    q2 = int(medianFinder(arr))
    
    if size%2 == 0:
        q1MLoc = int(size/2)
        #q1Arr = arr[0,q1MLoc]
        #q3Arr = arr[q1Mloc]
        q1 = medianFinder(arr[0:q1MLoc])
        q3 = medianFinder(arr[q1MLoc:size])
    else:
        q1MLoc = int(size/2)
        q1= int(medianFinder(arr[0:q1MLoc]))
        q3= int(medianFinder(arr[q1MLoc+1:size]))
    #print(q1,q2,q3)
    result = [q1,q2,q3]
    return result

n = int(input().strip())

data = list(map(int, input().rstrip().split()))

res = quartiles(data)
print(res)
