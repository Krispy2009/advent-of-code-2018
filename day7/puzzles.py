import re
from collections import OrderedDict
RE = re.compile(r'Step (?P<step_1>[A-Z]{1}) .* step (?P<step_2>[A-Z]{1}) .*')
with open('day-7-input') as f:
    data = f.readlines()


class Step:
    def __init__(self, name):
        self.name = name
        self.prerequisites = []
        self.finished = False
        self.next_steps = []

    def add_item(self, attr, step):
        # add item in attr(list) in sorted order
        if attr:
            for idx, item in enumerate(attr):
                if item.name >= step.name:
                    attr.insert(idx, step)
                    break
            attr.append(step)
        else:
            attr.append(step)

    def has_prerequisites(self):
        return self.prerequisites

    def is_ready(self):
        if not self.prerequisites:
            return True
        for step in self.prerequisites:
            if not step.finished:
                return False
        return True

    def __str__(self):
        return f"Step '{self.name}' with prereqs {self.prerequisites}"


def parse_instructions(data):

    steps = OrderedDict()

    for row in data:
        # If current_step has a prerequisite then the prerequisite has a
        #  next_step = current_step
        step = None
        prerequisite, current_step = re.match(RE, row).groups()
        print(prerequisite, current_step)
        if current_step in steps:
            step = steps[current_step]
        else:
            print(f'Creating {current_step}')
            step = Step(current_step)

        if prerequisite in steps:
            prereq = steps[prerequisite]
        else:
            print(f'Creating prereq {prerequisite}')
            prereq = Step(prerequisite)
            if prerequisite not in steps:
                steps[prerequisite] = prereq

        print(f'Appending prereq {prerequisite}')
        step.add_item(step.prerequisites, prereq)
        steps[current_step] = step

    return sorted(steps.items())


steps = parse_instructions(data)
ans = ''
i = 0
print('============================')
while i < len(steps):
    for step in steps:
        if step[1].is_ready() and not step[1].finished:
            ans += step[0]
            step[1].finished = True
            break
        else:
            continue
    i += 1
print(f'Correct order: {ans}')
