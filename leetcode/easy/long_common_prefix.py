class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_prefix = []
        if not strs:
            return ''
        for i in range(len(strs[0])):
            i_char = strs[0][i]
            for item in strs:
                try:
                    if not item[i] == i_char:
                        return ''.join(common_prefix)
                except:
                    return ''.join(common_prefix)
            else:
                common_prefix.append(i_char)
        return ''.join(common_prefix)


if __name__ == '__main__':
    solu = Solution()
    print(solu.longestCommonPrefix([""]))
