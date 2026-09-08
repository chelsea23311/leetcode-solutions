class Solution(object):
    def exist(self, board, word):
        def backtrack(m,n,index):
            if index==len(word):
                return True
            temp=board[m][n]
            board[m][n]='#'
            if m - 1 >= 0 and board[m-1][n] == word[index]:
                if backtrack(m-1, n, index + 1):
                    return True
            if m + 1 < len(board) and board[m+1][n] == word[index]:
                if backtrack(m+1, n, index + 1):
                    return True
            if n - 1 >= 0 and board[m][n-1] == word[index]:
                if backtrack(m, n-1, index + 1):
                    return True
            if n + 1 < len(board[0]) and board[m][n+1] == word[index]:
                if backtrack(m, n+1, index + 1):
                    return True
            board[m][n]=temp
            return False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==word[0]:
                    if backtrack(i,j,1):
                        return True
        return False
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        