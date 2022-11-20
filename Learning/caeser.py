import string

def lett(letter, amount):
    if letter not in string.ascii_lowercase:
        return letter
    new_letter = ord(letter) + amount;
    while(new_letter > ord('z')):
        new_letter -= 26
    # while(new_letter < ord('a')):
    #     new_letter += 26
    return chr(new_letter)

def mess(message, amount):
    s = [lett(letter, amount) for letter in message]
    return "".join(s)

a = input("enter a string: ");
sh = int(input("enter a value for shifting: "))
print(mess(a, sh))