class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        sort(happiness.begin(), happiness.end(), greater<int>());
        
        long long total = 0;
        
        for (int i = 0; i < k; i++) {
            int contribution = max(0, happiness[i] - i);
            total += contribution;
            
            if (contribution == 0) {
                break;
            }
        }
        
        return total;
    }
};