class MyHashSet {
    private capacity: number;
    private buckets: number[][];

    constructor() {
        this.capacity = 769; 
        this.buckets = Array.from({ length: this.capacity }, () => []);
    }

    private hash(key: number): number {
        return key % this.capacity;
    }

    add(key: number): void {
        const bucket = this.buckets[this.hash(key)];
        if (!bucket.includes(key)) {
            bucket.push(key);
        }
    }

    remove(key: number): void {
        const bucket = this.buckets[this.hash(key)];
        const index = bucket.indexOf(key);
        if (index !== -1) {
            bucket[index] = bucket[bucket.length - 1];
            bucket.pop();
        }
    }

    contains(key: number): boolean {
        const bucket = this.buckets[this.hash(key)];
        return bucket.includes(key);
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = new MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */
