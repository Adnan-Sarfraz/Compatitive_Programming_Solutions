print("--------------------------------------PALINDROM FOR STRING-------------------------------------")
def palindrom(s):
    s=s.lower()
    reversed_s=s[::-1]
    if reversed_s==s:
        return True
    else:
        return False
    
word="ADnan"
if(palindrom(word)):
    print(f"{word} is palindrom")
else:
    print(f"{word} is not palindrom")

print("\n\n\n--------------------------------------PALINDROM FOR NUMBERS-------------------------------------")

def palindrom_num(ss):
    ss=str(ss)
    reversed_ss=ss[::-1]
    if reversed_ss==ss:
        return True
    else:
        return False
    
num=123210
if(palindrom_num(num)):
    print(f"{num} is palindrom")
else:
    print(f"{num} is not a palindrom")