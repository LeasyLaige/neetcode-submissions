class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false;

        let smap = new Map();

        for (const char of s) {
            smap.set(char, (smap.get(char) || 0) + 1);
        }

        for (const char of t) {
            if (!smap.has(char) || smap.get(char) === 0) {
                return false;
            }
            smap.set(char, smap.get(char) - 1);
        }

        return true;
    }
}
