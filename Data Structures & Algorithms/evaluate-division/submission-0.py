class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = {}
        for i in range(len(equations)):
            (var_a,var_b),val=equations[i],values[i]
            if var_a not in adj:
                adj[var_a]=[]
            if var_b not in adj:
                adj[var_b]=[]
            adj[var_a].append((var_b,val))
            adj[var_b].append((var_a,1/val))
        def dfs(s,d, visited):
            if s==d:
                return True, 1
            if s not in adj:
                return False, -1
            visited.add(s)
            for n,val in adj[s]:
                if n in visited:
                    continue
                found, result = dfs(n, d, visited)
                if found:
                    return True, val * result
            return False, -1
        results = []
        for var_a, var_b in queries:
            if var_a not in adj:
                results.append(-1)
                continue
            found, val = dfs(var_a, var_b, set())
            if not found:
                results.append(-1)
            else:
                results.append(val)
        return results

            

