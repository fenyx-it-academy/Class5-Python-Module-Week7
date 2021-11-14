import string

def word_counting(indiaa,india):
    word_count = {}
    with open (indiaa, "r") as f:
        for line in f:
            line = line.strip()
            words = line.strip()
            for india in words:
                if not india in word_count:
                    word_count[india] = 1
                else:
                    word_count[india] += 1
    return word_count
print(word_counting("indiaa.txt","india"))