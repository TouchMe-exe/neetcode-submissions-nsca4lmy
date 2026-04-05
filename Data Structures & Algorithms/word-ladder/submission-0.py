class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def is_neighbour(node1, node2):
            count = 0

            for i in range(len(node1)):
                if node1[i] != node2[i]:
                    count += 1
            
            if count == 1:
                return True
            else:
                return False
        
        wordList.append(beginWord)
        adj_list = defaultdict(list)

        for word1 in wordList:
            for word2 in wordList:
                if is_neighbour(word1, word2):
                    adj_list[word1].append(word2)
        
        q = deque()
        q.append(beginWord)
        visited = set()
        depth = 0

        def bfs(node):
            if node in visited:
                return

            visited.add(node)

            for word in adj_list[node]:
                 q.append(word)
            
            return 
        
        while q:

            for i in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return depth + 1
                else:
                    bfs(node)
            
            depth += 1
        
        return 0

                
            
                