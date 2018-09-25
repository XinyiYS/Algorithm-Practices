class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        def isvalid(str):
            if len(str) == 0:
                return False
            i = 0
            while i < len(str) and not str[i].isdigit() and not str[i] == '-':
                if not str[i] == ' ':
                    return False
                i += 1
            begin = i
            negsign = True
            while i < len(str) and (str[i].isdigit() or negsign * str[i] == '-'):
                if str[i] == '-':
                    negsign = False
                i += 1
            return str[begin:i]

        def checkRange(number_str):
            result = 0
            if number_str.startswith('-'):
                if len(number_str) > 11:
                    return -2147483648
                elif len(number_str) < 11:
                    for i, digit in enumerate(number_str[1:][::-1]):
                        result -= int(digit) * 10 ** i
                    return result
                else:
                    if all( [ digit <= given for digit,given in zip(number_str[1:],'2147483648')] ):
                        for i, digit in enumerate(number_str[1:][::-1]):
                            result -= int(digit) * 10 ** i
                        return result
                    else:
                        return -2147483648
            else:
                if len(number_str) > 10:
                    return 2147483647
                elif len(number_str) < 10:
                    for i, digit in enumerate(number_str[::-1]):
                        result += int(digit) * 10 ** i
                    return result
                else:
                    if all( [ digit <= given for digit,given in zip(number_str,'2147483647')] ):
                        for i, digit in enumerate(number_str[::-1]):
                            result += int(digit) * 10 ** i
                        return result
                    else:
                        return 2147483647
            return

        number_str = isvalid(str)
        print(number_str)
        if not number_str:
            return 0
        result = checkRange(number_str)
        return result


s = Solution()
inputs = ['0-1','42','-42', '4193 with words','words and 123','-91283472332','2147483648+1']
for input in inputs:
    print(s.myAtoi(input))
