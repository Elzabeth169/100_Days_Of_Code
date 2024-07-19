class Solution:
    def groupAnagrams(self, strs):
        d={}
        for s in strs:
            ss=''.join(sorted(s))
            if ss in d:
                d[ss].append(s)
            else:
                d[ss]=[s]
        return list(d.values())