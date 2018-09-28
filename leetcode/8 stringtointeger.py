class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        def get_trimmed(str):

            negsign = True

            for i,c in enumerate(str):
                if c ==' ' or c.isdigit() or negsign * c=='-':
                    if c.isdigit() or c=='-':
                        negsign = False



            return



        def isvalid(str):
            if len(str) == 0:
                return False
            i = 0
            left_trimmed = ''
            while i < len(str) and str[i]==' ':
                i+=1
            left_trimmed = str[i:]
            if len(left_trimmed) ==0:
                return False
            str = left_trimmed
            while i < len(str) and not str[i].isdigit() and not str[i] == '-':
                if not str[i] == ' ':
                    return False
                i += 1
            print(str)
            begin = i
            print(begin)

            if  str[begin] != '-':
                negsign =False
            else:
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
        if not number_str:
            return 0
        result = checkRange(number_str)
        return result


s = Solution()
inputs = ['42','-42', '4193 with words','words and 123','-91283472332','21474836489']
for input in inputs:
    print(s.myAtoi(input))
