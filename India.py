'''## 2. India

Write a method in Python to read lines from a text file `india.txt`, to find and display the occurrence of the word 'India'. For example, if the content of the file is:

```
India is the fastest-growing economy. India is 
looking for more investments around the globe. The 
whole world is looking at India as a great market. 
Most of the Indians can foresee the heights that 
India is capable of reaching.
```
The output should be 4.'''

with open("india.txt") as file:
    words = file.read().split()
    dic = dict()
    for i in words:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
print(dic["India"])