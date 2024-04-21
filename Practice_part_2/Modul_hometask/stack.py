class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)





class TaskManager:
    def __init__(self):
        self.tasks = Stack()

    def new_task(self, task, priority):
        self.tasks.push((task, priority))

    def remove_task(self, task):
        temp_stack = Stack()
        removed = False

        while not self.tasks.is_empty():
            current_task = self.tasks.pop()
            if current_task[0] != task:
                temp_stack.push(current_task)
            else:
                removed = True

        while not temp_stack.is_empty():
            self.tasks.push(temp_stack.pop())

        if not removed:
            print("Task not found.")

    def __str__(self):
        temp_stack = Stack()
        result = ""

        while not self.tasks.is_empty():
            temp_stack.push(self.tasks.pop())

        self.sorted_tasks = sorted(temp_stack.stack, key=lambda x: x[1])
        print(self.sorted_tasks)
       # task, priority = sorted_tasks.pop()
       #      result += f"{priority} - {task}\n"

        return result


# Теперь можете использовать этот код для создания объекта TaskManager
# и выполнения операций добавления и удаления задач.

manager = TaskManager()

manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать ДЗ", 2)

print(manager)

manager.remove_task("помыть посуду")

print(manager)