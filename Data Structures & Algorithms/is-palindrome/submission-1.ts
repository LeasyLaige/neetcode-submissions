class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s: string): boolean {
        const str = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
        const reversedStr = str.split('').reverse().join('');

        if (str === reversedStr) {
            return true;
        }

        return false;
    }
}
