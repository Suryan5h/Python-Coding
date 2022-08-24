# input: adca3rtyy2uid3
# Expected output:
# aaadddcccaaa
# rrttyyyy
# uuuiiiddd

input = "adca3rtyy2uid3"
temp=""

def output(temp,count):
    temp_str=""
    for ch in temp:
        t = ch*count
        temp_str+=t
    return temp_str
    
for i in input:
    if i.isalpha():
        temp+=i
    else:
        count=int(i)
        print(output(temp,count))
        temp=""
