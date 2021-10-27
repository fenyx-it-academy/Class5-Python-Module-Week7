# ## 2. India

# Write a method in Python to read lines from a text file `india.txt`, to find and display the occurrence of the word 'India'. For example, if the content of the file is:

# ```
# India is the fastest-growing economy. India is 
# looking for more investments around the globe. The 
# whole world is looking at India as a great market. 
# Most of the Indians can foresee the heights that 
# India is capable of reaching.
# ```
# The output should be 4.
def count_word(text,special_word):
    with open(text,'r') as f:
        f.seek(0)
        count={special_word:0}
        for line in f:
            line=line.split()
            for word in line:
                if word==special_word:
                    count[special_word]+=1
    return count

print(count_word('india.txt','India'))