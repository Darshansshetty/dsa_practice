def long_sub(s):
    left=0
    max_len=0
    char=set()
    start_index=0
    for right in range(len(s)):
        while s[right] in char:
            char.remove(s[left])
            left+=1
        char.add(s[right])
        if right-left+1>max_len:
            max_len=right-left+1
            start_index=left
    longest_substr=s[start_index:start_index+max_len]
    return longest_substr,max_len
s="abbcbabshddaaa"
print(long_sub(s))
        
    
    
        