"""2115. Find All Possible Recipes from Given Supplies"""

from typing import List


class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        mapping: dict[str, list[str]] = dict(zip(recipes, ingredients, strict=True))
        recipes_set: set[str] = set(recipes)
        supplies_set: set[str] = set(supplies)

        while recipes_set:
            recipe_to_add: set[str] = set()

            for recipe in recipes_set:
                if set(mapping[recipe]).issubset(supplies_set):
                    recipe_to_add.add(recipe)

            if not recipe_to_add:
                break

            supplies_set |= recipe_to_add

            recipes_set -= recipe_to_add

        return list(supplies_set - set(supplies))
