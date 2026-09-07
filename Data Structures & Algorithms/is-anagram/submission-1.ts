class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if (s.length !== t.length) {
            return false;
        }

        const charCounts = new Int32Array(26);
        const baseCode = 97; // 'a'.charCodeAt(0)

        for (let i = 0; i < s.length; i++) {
            charCounts[s.charCodeAt(i) - baseCode]++;
            charCounts[t.charCodeAt(i) - baseCode]--;
        }

        for (let i = 0; i < 26; i++) {
            if (charCounts[i] !== 0) {
                return false;
            }
        }

        return true;
    }
}
