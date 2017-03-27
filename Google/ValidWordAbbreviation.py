class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue
            if not abbr[j].isdigit():
                return False
            start = j
            while j < len(abbr) and abbr[j].isdigit():
                j += 1
            i += int(abbr[start:j])
        print i, j
        return i == len(word) and j == len(abbr)


if __name__ == '__main__':
    word = 'internationalization'
    abbr = 'i12iz4n'
    print Solution().validWordAbbreviation(word, abbr)