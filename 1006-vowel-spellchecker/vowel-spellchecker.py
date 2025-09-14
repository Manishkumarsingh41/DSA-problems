class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = "aeiou"
        def devowel(s):
            return ''.join('#' if c in vowels else c for c in s.lower())

        exact = set(wordlist)
        lower_map, devowel_map = {}, {}
        for w in wordlist:
            lw, dv = w.lower(), devowel(w)
            lower_map.setdefault(lw, w)
            devowel_map.setdefault(dv, w)

        ans = []
        for q in queries:
            if q in exact: ans.append(q)
            elif q.lower() in lower_map: ans.append(lower_map[q.lower()])
            elif devowel(q) in devowel_map: ans.append(devowel_map[devowel(q)])
            else: ans.append("")
        return ans
