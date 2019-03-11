class MaxHeap:

    def __init__(self, capacity=10000):
        self.capacity = capacity
        self.__data = [None]

    def __len__(self):
        return len(self.__data) - 1

    def append(self, item):
        self.__data.append(item)
        self.__shift_up(count=len(self))

    def __shift_up(self, count):
        while count > 1 and self.__data[count] > self.__data[count // 2]:
            self.__data[count], self.__data[count // 2] = self.__data[count], self.__data[count // 2]
            count //= 2

    def visible_print(self):
        pass
