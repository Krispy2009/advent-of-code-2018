NUM_RECIPES = 380621

class Recipe:
    score = None
    prev = None
    next = None

    def __init__(self, score):
        self.score = score

    def __repr__(self):
        return f'{self.score}'



class Recipes:

    def __init__(self):
        self.recipes = []
        self._last = None
        self._first = None
        self.index = None

    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, recipe):
        self._last = recipe

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, recipe):
        self._first = recipe

    def add_to_end(self, recipe):
        if isinstance(recipe, int):
            recipe = Recipe(recipe)

        if len(self.recipes):
            recipe.next = self.first
            recipe.prev = self.last
            self.last.next = recipe
            self.first.prev = recipe
            recipe.index = self.last.index + 1
        else:
            # add first element
            self.first = recipe
            self.first.index = 0
        self.last = recipe
        self.recipes.append(recipe)

    def __len__(self):
        return len(self.recipes)

    def __getitem__(self, idx):
        if isinstance(idx, int):
            return self.recipes[idx % (len(self.recipes))]
        elif isinstance(idx, slice):
            return self.recipes[idx]
        else:
            return None


    def __repr__(self):
        return ' '.join([str(rcp) for rcp in self.recipes])


class Elf:
    def __init__(self, curr_recipe):
        self.recipe = curr_recipe
        self.index = self.recipe.index


recipes = Recipes()
recipes.add_to_end(Recipe(3))
recipes.add_to_end(Recipe(7))

elves = [Elf(recipes[0]), Elf(recipes[1])]

while len(recipes) < NUM_RECIPES+10:
    new_recipe = 0
    for elf in elves:
        new_recipe += elf.recipe.score

    new_recipe = list(str(new_recipe))

    for score in new_recipe:
        recipes.add_to_end(Recipe(int(score)))

    for elf in elves:
        new_idx = elf.index + 1 + elf.recipe.score
        elf.recipe = recipes[new_idx]
        elf.index = elf.recipe.index



print('==========')
last_10 = recipes[NUM_RECIPES:NUM_RECIPES+10]
print(''.join(str(l) for l in last_10))
