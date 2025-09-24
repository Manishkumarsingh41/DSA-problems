class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return "0"
        res = ["-" if numerator*denominator<0 else ""]
        n, d = abs(numerator), abs(denominator)
        res.append(str(n//d))
        r = n % d
        if not r: return "".join(res)
        res.append(".")
        seen = {}
        while r:
            if r in seen:
                res.insert(seen[r], "(")
                res.append(")")
                break
            seen[r] = len(res)
            r *= 10
            res.append(str(r//d))
            r %= d
        return "".join(res)
