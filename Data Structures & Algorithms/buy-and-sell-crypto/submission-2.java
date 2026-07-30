class Solution {
    public int maxProfit(int[] prices) {
        int currLow = prices[0];
        int res = 0;

        for(int i = 1; i < prices.length; i++){

            res = Math.max(res, prices[i] - currLow);
            if(prices[i] < currLow){
                currLow = prices[i];
            }
        }

        return res;
    }
}
