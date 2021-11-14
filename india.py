india = "India"
count = 0
with open('india.txt','r',encoding='utf8') as f:
    datafile = f.readlines()
for line in datafile:
    if india in line:
        count+=1
print(count)