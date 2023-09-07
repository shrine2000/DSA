class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def dfs(idx, path, current_val, prev_num):
            if idx == len(num):
                if current_val == target:
                    res.append(path)
                return
            
            for i in range(idx + 1, len(num) + 1):
                cs = num[idx:i]
                cn = int(cs)
                
                if idx == 0:
                    dfs(i, cs, cn, cn)
                else:
                    dfs(i, path + '+' + cs, current_val + cn, cn)
                    dfs(i, path + '-' + cs, current_val - cn, -cn)
                    dfs(i, path + '*' + cs, current_val - prev_num + (prev_num * cn), prev_num * cn)
                
                if num[idx] == '0':
                    break
        
        res = []
        if num:
            dfs(0, "", 0, 0)
        
        return res