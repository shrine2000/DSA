from collections import defaultdict, deque
from typing import List


class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
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


if __name__ == "__main__":
    solution = Solution()

    recipes1 = ["bread"]
    ingredients1 = [["yeast", "flour"]]
    supplies1 = ["yeast", "flour", "corn"]
    print(
        solution.findAllRecipes(recipes1, ingredients1, supplies1)
    )  # Output: ["bread"]

    recipes2 = ["bread", "sandwich"]
    ingredients2 = [["yeast", "flour"], ["bread", "meat"]]
    supplies2 = ["yeast", "flour", "meat"]
    print(
        solution.findAllRecipes(recipes2, ingredients2, supplies2)
    )  # Output: ["bread", "sandwich"]

    recipes3 = ["bread", "sandwich", "burger"]
    ingredients3 = [
        ["yeast", "flour"],
        ["bread", "meat"],
        ["sandwich", "meat", "bread"],
    ]
    supplies3 = ["yeast", "flour", "meat"]
    print(solution.findAllRecipes(recipes3, ingredients3, supplies3))
