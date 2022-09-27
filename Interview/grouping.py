# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# strs = ["eat","tea","tan","ate","nat","bat"]
# [["bat"],["nat","tan"],["ate","eat","tea"]]

def array_grouping(strs):
    d = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key in d:
            d[key].append(s)
        else:
            d[key] = [s]
    return list(d.values())

print(array_grouping(["eat","tea","tan","ate","nat","bat","vma","mva","avm"]))

import cProfile
cProfile.run("array_grouping(['eat','tea','tan','ate','nat','bat','avm','avm','avm'])")