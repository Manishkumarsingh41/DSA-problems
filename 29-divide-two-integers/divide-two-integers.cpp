class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == INT_MIN && divisor == -1) return INT_MAX;
        long a = abs((long)dividend), b = abs((long)divisor), res = 0;
        for (int i = 31; i >= 0; i--)
            if (a >> i >= b) {
                a -= b << i;
                res += 1LL << i;
            }
        return ((dividend > 0) ^ (divisor > 0)) ? -res : res;
    }
};
