class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(board, word, i, j):
                    return True
        return False

    def dfs(self, board, word, i, j):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        c = board[i][j]
        board[i][j] = ''
        found = self.dfs(board, word[1:], i+1, j) or self.dfs(board, word[1:], i, j+1) \
                or self.dfs(board, word[1:], i-1, j) or self.dfs(board, word[1:], i, j-1)
        board[i][j] = c
        return found

if __name__ == '__main__':
    board = [list('ABCE'), list('SFES'), list('ADEE')]
    word = 'ABCESEEEFS'
    print Solution().exist(board, word)