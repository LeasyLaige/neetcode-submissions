class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        const map = new Map<string, string[]>();
        
        for (const str of strs) {
            const count = new Array(26).fill(0);
            for (let i = 0; i < str.length; i++) {
                count[str.charCodeAt(i) - 97]++; 
            }
            
            const key = count.join('#'); 
            
            if (!map.has(key)) {
                map.set(key, []);
            }
            map.get(key)!.push(str);
        }
        
        return Array.from(map.values());
    }
}