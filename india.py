def halit(hedef_kelime,text):
    with open(text,'r') as file:
        count={hedef_kelime:0}
        lines = file.readlines()
        for line in lines:
            line=line.split(" ")
            for word in line:
                if word==hedef_kelime:
                    count[hedef_kelime]+=1
    return count
