def get_list() -> list:
    return list(range(0, 1_000_000, 2))


lst = get_list()


class Solution:

    def int(self):
        ...

    def find_target(self, lst, target):
        l = 0
        r = 999999
        m = (l + r) // 2
        if target % 2 == 1:
            return f"Такого числа нет!!!"
        while lst[m] != target:
            if target > lst[m]:
                l = m
                m = (l + r) // 2
            elif target < lst[m]:
                r = m
                m = (l + r) // 2
        return m


d = 0
sol = Solution()
print(sol.find_target(lst, 5000))
#hghj
