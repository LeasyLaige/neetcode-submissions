class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board: string[][]): boolean {
        let initialStart = -1;

        for (let i = 0; i < board.length; i++) {
            const rowMap = new Map<string, number>();
            const colMap = new Map<string, number>();
            const boxMap = new Map<string, number>();

            let count: number = 0;

            for (let j = 0; j < board[i].length; j++) {
                let colStart: number = i - (i % 3)
                let colEnd: number = i + (3 - (i % 3))

                if (board[i][j] !== ".") {
                    rowMap.set(board[i][j], (rowMap.get(board[i][j]) || 0) + 1)
                }

                if (board[j][i] !== ".") {
                    colMap.set(board[j][i], (colMap.get(board[j][i]) || 0) + 1)
                }

                if (initialStart !== colStart) {
                    let rowStart: number = 0;
                    let rowEnd: number = 3;

                    while(count < 3) {
                        for (let k = colStart; k < colEnd; k++) {
                            for (let l = rowStart; l < rowEnd; l++) {
                                if (board[k][l] !== ".") {
                                    boxMap.set(board[k][l] ,(boxMap.get(board[k][l]) || 0) + 1)

                                    if (boxMap.get(board[k][l]) > 1) {
                                        return false;
                                    }
                                }
                            }
                        }

                        boxMap.clear();

                        rowStart += 3;
                        rowEnd += 3;
                        count++;
                    }

                    count = 0;
                    initialStart = colStart;
                }

                if (rowMap.get(board[i][j]) > 1 || colMap.get(board[j][i]) > 1) {
                    return false;
                }
            }
        }

        return true;
    }
}
