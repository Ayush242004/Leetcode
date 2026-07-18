class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        miprice=float("inf")
        mxprofit=0
        for p in prices:
            miprice=min(miprice,p)
            mxprofit=max(mxprofit,p-miprice)
        return mxprofit