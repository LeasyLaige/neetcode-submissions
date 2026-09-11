class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs: string[]): string {
        let encoded = "";
        for (const s of strs) {
            encoded += `${s.length}#${s}`;
        }
        return encoded;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str: string): string[] {
        const result: string[] = [];
        let i = 0;

        while (i < str.length) {
            const hashIndex = str.indexOf("#", i);
            const length = parseInt(str.substring(i, hashIndex), 10);

            const start = hashIndex + 1;
            const end = start + length;

            result.push(str.substring(start, end));
            i = end;
        }

        return result;
    }
}
