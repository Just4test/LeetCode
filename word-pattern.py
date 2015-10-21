class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        strs = str.split(" ", len(str))
        if len(strs) != len(pattern):
            return False
        map = {}
        map2 = {}
        for i, ch in enumerate(pattern):
            if not map.get(ch) and not map2.get(strs[i]):
                
                map[ch] = strs[i]
                map2[strs[i]] = ch
            else:
                if map.get(ch) != strs[i] or map2.get(strs[i]) != ch:
                    return False
        
        return True
        