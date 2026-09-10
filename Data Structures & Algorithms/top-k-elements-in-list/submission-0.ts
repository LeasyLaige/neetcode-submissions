class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */





    topKFrequent(nums: number[], k: number): number[] {
        const countMap = new Map<number, number>();

        for (const num of nums) {
            countMap.set(num, (countMap.get(num) || 0) + 1);
        }

        const buckets: number[][] = Array.from({ length: nums.length + 1 }, () => []);

        for (const [num, count] of countMap.entries()) {
            buckets[count].push(num);
        }

        const result: number[] = [];

        for (let freq = buckets.length - 1; freq > 0 && result.length < k; freq--) {
            if (buckets[freq].length > 0) {
                for (const num of buckets[freq]) {
                    result.push(num);
                    if (result.length === k) {
                        break;
                    }
                }
            }
        }

        return result;
    }
}
