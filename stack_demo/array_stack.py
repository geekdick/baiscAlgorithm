class ArrayStack:

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        """如果是空栈返回True"""
        return len(self.data) == 0

    def push(self, e):
        """向栈顶添加一个元素"""
        self.data.append(e)

    def peek(self):
        """返回栈顶元素，保持栈中元素不变"""
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.data[-1]

    def pop(self):
        """弹出栈顶元素，保持栈中元素减一"""
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.data.pop()
