list = ["abc", "ca", "cab"]
# { "ca": 2, "abc": 1, "ab": 1, "cab": 1, "a": 1, "c": 2 }

def prefixes(list) -> dict:
    prefix_dict = {}
    prefix_set = set()
    for word in list:
        charactor = ""
        for i in range(len(word)):
            charactor += word[i]
            prefix_set.add(charactor)
            if charactor in prefix_dict:
                prefix_dict[charactor] += 1
            else:
                prefix_dict[charactor] = 1
    return prefix_dict

def prefixes_set(list) ->set:
    prefix_dict = {}
    prefix_set = set()
    for word in list:
        charactor = ""
        for i in range(len(word)):
            charactor += word[i]
            prefix_set.add(charactor)
    return prefix_set

value_dict = prefixes(list)
value_set = prefixes_set(list)
print(f'set is {value_set}')
print(f'dictionary is {value_dict}')
