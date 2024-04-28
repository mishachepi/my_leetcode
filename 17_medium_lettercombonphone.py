"""
my backtracking - bicycle
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        phone_keys = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
        }

        def recrusive_number_comb(res_lst, res_index, letters, letters_i):
            res_tmp = res_lst[res_index]
            for i in range(len(letters[letters_i])):
                if letters_i > 0:
                    res_lst[res_index] = res_tmp + letters[letters_i][i]
                    recrusive_number_comb(res_lst, len(res_lst) - 1 , letters, letters_i - 1)
                    res_index = len(res_lst) - 1
                    if i == len(letters[letters_i]) - 1:
                        return 0
                if letters_i == 0:
                    res_lst[res_index] = res_tmp + letters[letters_i][i]
                    res_index += 1
                    if i == len(letters[letters_i]) - 1:
                        res_lst.append('')
                        return 0
                    res_lst.append(res_tmp)
                    continue

        letters = []
        for d in digits:
            letters.append(phone_keys[d])
        letters.reverse()
        res = ['']
        if letters:
            recrusive_number_comb(res, 0, letters, len(letters) - 1)
        res.pop()
        return res
