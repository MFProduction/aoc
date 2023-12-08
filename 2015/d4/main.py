#!usr/bin/env python
import hashlib

def hashmap(key,num):
    count = 1
    while True:
        result = hashlib.md5(f"{key}{count}".encode()).hexdigest()[:num]
        if result == "0"*num:
            return count
        count+=1

key = "bgvyzdsv"
print(hashmap(key,5))
print(hashmap(key,6))