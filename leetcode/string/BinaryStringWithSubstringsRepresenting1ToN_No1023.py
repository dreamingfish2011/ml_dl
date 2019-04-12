class Solution:
    def queryString(self, S, N):
        for every in range(N, int(N / 2), -1):
            if self.checkNIfSSubstr(S, every):
                continue
            else:
                return False
        return True

    def checkNIfSSubstr(self, S, N):
        bin_str = format(N, 'b')
        partial_match_table = []
        pre_set = set()
        postfix_set = set()
        for i in range(0, len(bin_str)):
            if i >= 1:
                pre_set.add(bin_str[0:i])
                for j in range(1, i + 1):
                    postfix_set.add(bin_str[j:i + 1])
            inter_set = pre_set.intersection(postfix_set)
            partial_match_table.append(len(inter_set))
        print(partial_match_table)
        already_match = 0
        i = 0
        while (i < len(S)):
            if already_match == len(partial_match_table):
                return True
            if S[i] == bin_str[already_match]:
                already_match = already_match + 1
                i = i + 1
            else:
                if already_match > 0:
                    ##起始匹配位置加偏移量
                    i = i  - partial_match_table[already_match]
                    already_match = 0
                else:
                    already_match = 0
                    i = i + 1
        if already_match == len(partial_match_table):
            return True
        else:
            return False


t = Solution()
S = "0110"
N = 3
print(t.queryString(S, N))
