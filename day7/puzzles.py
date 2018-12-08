import re
from collections import OrderedDict
from string import ascii_uppercase as UP
RE = re.compile(r'Step (?P<step_1>[A-Z]{1}) .* step (?P<step_2>[A-Z]{1}) .*')

with open('day-7-input') as f:
    data = f.readlines()


class Worker:
    working_on = None
    time_remaining = 0

    def __init__(self, name):
        self.name = name + 1

    def is_ready(self):
        return self.working_on is None

    def start_work(self, task):
        self.working_on = task
        self.time_remaining = UP.index(task) + 61

    def working(self):
        if self.time_remaining > 1:
            self.time_remaining -= 1
        elif self.time_remaining == 1:
            self.time_remaining -= 1
            finished = self.working_on
            self.working_on = None
            return finished


class Step:
    def __init__(self, name):
        self.name = name
        self.prerequisites = []
        self.finished = False
        self.next_steps = []
        self.is_being_worked_on = False

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
        if self.is_being_worked_on:
            return False
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
        step = None
        prerequisite, current_step = re.match(RE, row).groups()
        if current_step in steps:
            step = steps[current_step]
        else:
            # print(f'Creating {current_step}')
            step = Step(current_step)

        if prerequisite in steps:
            prereq = steps[prerequisite]
        else:
            # print(f'Creating prereq {prerequisite}')
            prereq = Step(prerequisite)
            if prerequisite not in steps:
                steps[prerequisite] = prereq

        # print(f'Appending prereq {prerequisite}')
        step.add_item(step.prerequisites, prereq)
        steps[current_step] = step

    return sorted([[a, b] for a, b in steps.items()])


steps = parse_instructions(data)


def part_1(steps):
    ans = ''
    i = 0
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


part_1(steps)


def part_2(steps):

    workers = [Worker(i) for i in range(5)]

    def get_free_worker():
        for worker in workers:
            if worker.is_ready():
                return worker
    ans = ''
    time = 0
    # import pudb; pudb.set_trace()
    # not all([i[1].finished for i in steps])
    while not all([i[1].finished for i in steps]):

        for step in steps:
            worker = get_free_worker()
            if worker is not None and step[1].is_ready():
                if step[1].is_ready() and not step[1].finished:
                    # print(f'Worker {worker.name}: Started {step[0]} at {time} ')
                    worker.start_work(step[0])
                    step[1].is_being_worked_on = True
                    continue

        for w in workers:
            completed = w.working()
            if completed:
                # print(f'Worker {w.name}: Completed {completed} at {time}')
                ans += completed
                idx = UP.index(completed)
                steps[idx][1].finished = True
                steps[idx][1].is_being_worked_on = False

        time += 1
    print(f'Time taken: {time}')


steps = parse_instructions(data)
part_2(steps)
