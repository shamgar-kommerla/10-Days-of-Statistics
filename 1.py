#No. of Elements
x = int(input())

#taking inputs
myList = list(map(int,input().split()))[:x]

#sorting
myList.sort()

#Mean
mean = 0
for num in myList:
  mean = mean + num
mean = mean/x
print(round(mean,1))

#median
#numOfElem = x
if x%2 == 0:
    med_loc = int(x/2)
    median = (myList[med_loc-1] + myList[med_loc])/2 
    """Accepted by HackerRank. 
    But don't know why it showed "List index out of range" on test case3" 
    in my terminal at this statement
    """
else:
    med_loc = int((x + 1)/2)
    median = myList[med_loc-1]
print(round(median,1))


#mode
mode = 0;
for num in myList:
    if myList.count(num)> myList.count(mode):
        mode = num

print(mode)
