def freq_character(s):
    freq={}
    s=s.lower().replace(" ","")
    for char in s:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    return freq
print(f"The frequency of each character is {freq_character("hello world")}")
    