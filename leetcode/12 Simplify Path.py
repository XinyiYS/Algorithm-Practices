# https://leetcode.com/problems/simplify-path/description/
class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        result = []
        ignore_ = set(['',".",".."])
        dir_stack = path.split('/')
        for dir in dir_stack:
            if dir == '..' and len(result)!=0:
                result.pop()
            elif dir not in ignore_:
                result.append(dir)

        return "/" + '/'.join(result) if len(result) > 0 else '/'
