class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums: number[]): number {
        const numSet = new Set(nums);
        let longestStreak = 0;

        for (const num of numSet) {
            if (!numSet.has(num - 1)) {
                let currentNum = num;
                let currentStreak = 1;

                while (numSet.has(currentNum + 1)) {
                    currentNum++;
                    currentStreak++;
                }

                longestStreak = Math.max(longestStreak, currentStreak);
            }
        }

        return longestStreak;
    }
}
