import hashlib


def hashme(hash_string):
    return hashlib.sha256(hash_string.encode()).hexdigest()


print(hashme("title" + "desc"))
print(hashme("title" + "desc2"))

import json
dis = ["t1", "t2"]
headers = {"dismmissed" : json.dumps(dis)}
print(headers, type(json.dumps(dis)))
Dictionary ={1:'Welcome', 2:'to',
            3:'Geeks', 4:'for',
            5:'Geeks'}

print(json.dumps(Dictionary))