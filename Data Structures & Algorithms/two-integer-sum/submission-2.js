class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        for (const [index1, i] of nums.entries()) {
            for (const [index2, j] of nums.entries()) {
                if (index1 === index2) {
                    continue;
                } else if (j + i === target) {
                    return [index1, index2];
                }
            }
        }

        return false;
    }
}
