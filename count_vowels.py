def count_vow(s):
    vowels="aeiouAEIOU"
    return sum(ch in vowels for ch in s)
print(count_vow("aeioAAAEEEIIOOUU"))
   