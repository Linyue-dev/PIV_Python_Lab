list = ["abc", "ca", "cab"]
def prefixes(list):
    prefix_dict = {}
    prefix_set = set()
    for word in list:
        charactor = ""
        for i in range(len(word)):
            prefix_set.add(word[i])
            if i != 0:
                charactor = word[i-1] + word[i]
                prefix_set.add(charactor)

    return prefix_set
value = prefixes(list)
print(prefixes(list))
