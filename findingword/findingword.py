with open("india.txt") as file:
    words = file.read().split()
    countwords = dict()
    for word in words:
        if word not in countwords.keys():
            countwords[word] = 1
        else:
            countwords[word] += 1
print(countwords["India"])
