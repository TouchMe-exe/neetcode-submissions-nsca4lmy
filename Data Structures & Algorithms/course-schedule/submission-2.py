class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for course_a, course_b in prerequisites:
            if course_a in adj:
                adj[course_a].append(course_b)
            else:
                adj[course_a] = [course_b]

        def dfs(cur_course, visited):
            if cur_course in visited:
                return False
            visited.add(cur_course)
            if cur_course not in adj:
                visited.remove(cur_course)
                return True
            for course in adj[cur_course]:
                if not dfs(course, visited):
                    return False
                adj[cur_course].remove(course)
            visited.remove(cur_course)
            return True

        for course in range(numCourses):
            if not dfs(course, set()):
                return False
        return True
                

            