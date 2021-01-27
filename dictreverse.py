#program to reverse the key and value in the dictionary
#pls review
dict ={"a":"!","b":"@","c":"#","d":"$","e":"5","f":"^","g":"&","h":"*","i":"(","j":"!)","k":"!@","l":"!#","m":"!$",
    "n":"!%","o":"!^","p":"!&","q":"!*","r":"!(","s":"!)","t":"@@","u":"@#","v":"@%","w":"^y","x":"@^","y":"@&","z":"@("}

rev_dict= {}

def reverse():
    list_keys = list(dict.keys())
    list_val = list(dict.values())
    for i in range(0, len(list_val)):
        value = list_keys[i]
        key = list_val[i]
        rev_dict[key] = value


def find_key_value(str):

    if str in dict:
        return dict[str]
    else:
        reverse()
        return rev_dict[str]

val = input("Enter the key/value to be found:")
print(find_key_value(val))
print(rev_dict)
