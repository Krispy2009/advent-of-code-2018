
def get_data(filename):
    with open(filename) as f:
        data = f.readline()
    return data.split()


def process_data(data):
    children = int(data.pop(0))
    meta = int(data.pop(0))
    node = Node(children, meta, data)
    print(f'Sum of all meta: {node.sum_meta}')
    print(f'Value of root node: {node.value}')


class Node:
    def __init__(self, num_children, num_meta, data):
        self.num_children = num_children
        self.num_meta = num_meta
        self.data = data
        self.children = []
        self.meta = []
        self.sum_meta = 0
        self.value = 0

        self.populate_children()
        self.caluclate_child_meta()

    def populate_children(self):
        if self.data:
            children = self.num_children
            for child in range(children):
                c = int(self.data.pop(0))
                m = int(self.data.pop(0))
                self.children.append(Node(c, m, self.data))
                children -= 1
            if children == 0:
                for i in range(self.num_meta):
                    self.meta.append(int(self.data.pop(0)))
                self.sum_meta += sum(self.meta)

            if self.num_children == 0:
                self.value = self.sum_meta
            else:
                for idx in self.meta:
                    # print(f'Trying idx {idx}')
                    try:
                        self.value += self.children[idx-1].value
                    except IndexError:
                        # print(f'No idx {idx} exists')
                        continue

    def caluclate_child_meta(self):
        for i in range(self.num_children):
            self.sum_meta += self.children[i].sum_meta

if __name__ == '__main__':
    data = get_data('day-8-input')
    process_data(data)
