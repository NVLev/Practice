class Stack(list):
    def append(self, x):
        idx = 0
        for i, w in enumerate(self[::-1]):
            if w[1] >= x[1]:
                idx = len(self) - i
                break
        self.insert(idx, x)


class TaskManager:
    def __init__(self):
        self.stack = Stack()

    def new_task(self, task, priority):
        self.stack.append((task, priority))

    def __str__(self):
        d, res = {}, []
        for t, p in self.stack[::-1]:
            if p in d:
                d[p].insert(0, t)
            else:
                d[p] = [t]
        for p in d.keys():
            res.append(f'{p} -- {";".join(d[p])}')
        return "\n".join(res)

manager = TaskManager()

manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать ДЗ", 2)

print(manager)

#manager.remove_task("помыть посуду")

print(manager)