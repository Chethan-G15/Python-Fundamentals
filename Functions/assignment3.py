"""# 3)Count vowels in a string using a function"""
txt= input("Enter the Text ")
def countVowel(txt):
    cnt =0
    for i in txt:
        if i in 'aeiouAEIOU':
            cnt+=1
    return cnt

print("No of Vowels present in Give Text is",countVowel(txt))