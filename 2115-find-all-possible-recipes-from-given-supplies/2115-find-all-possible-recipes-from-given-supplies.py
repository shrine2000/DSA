class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        available = set(supplies)
        
        for recipe, ingrs in zip(recipes, ingredients):
            for ing in ingrs:
                if ing not in available:
                    graph[ing].append(recipe)
                    in_degree[recipe] += 1
        
        queue = deque([recipe for recipe in recipes if in_degree[recipe] == 0])
        result = []

        while queue:
            recipe = queue.popleft()
            result.append(recipe)
            available.add(recipe)
            
            for neighbor in graph[recipe]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result