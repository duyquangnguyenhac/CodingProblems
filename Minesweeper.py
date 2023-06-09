# LC 529 - Minesweeper
# https://leetcode.com/problems/minesweeper/description/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1)]
        r_len = len(board)
        c_len = len(board[0])

        def check_adj_bombs(cur_r, cur_c):
            cnt = 0
            for dir_r, dir_c in directions:
                adj_r, adj_c = cur_r + dir_r, cur_c + dir_c
                if adj_r < 0 or adj_r >= r_len or adj_c < 0 or adj_c >= c_len:
                    continue
                if board[adj_r][adj_c] == "M" or board[adj_r][adj_c] == "X":
                    cnt += 1
            return cnt

        visited = set()
        def dfs(cur_r, cur_c):
            visited.add((cur_r, cur_c))
            cnt = check_adj_bombs(cur_r, cur_c)
            if cnt != 0:
                board[cur_r][cur_c] = cnt
            
            if cnt == 0:
                board[cur_r][cur_c] = "B"
            else:
                board[cur_r][cur_c] = str(cnt)
                return

            for dir_r, dir_c in directions:
                adj_r, adj_c = cur_r + dir_r, cur_c + dir_c
                if adj_r < 0 or adj_r >= r_len or adj_c < 0 or adj_c >= c_len:
                    continue
                if (adj_r, adj_c) in visited:
                    continue
                elif board[adj_r][adj_c] == "E":
                    dfs(adj_r, adj_c)

        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
        else:
            dfs(click[0], click[1])
        return board
                
testA = [
    ["E", "E", "E"],
    ["E", "E", "E"],
    ["E", "E", "E"]
]
testAclick = (0,0)
