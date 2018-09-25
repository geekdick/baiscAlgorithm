from collections import Iterable
from random import randint


class BasicSort(object):
    def __init__(self, seq):
        self.seq = seq

    # 冒泡排序
    def bubbleSort(self, seq=None, reversed=False):
        if isinstance(seq, Iterable):
            # 函数可以接受传来的sequence
            self.seq = seq
        lens = len(self.seq)
        for i in range(lens):
            for j in range(lens - i - 1):
                if (self.seq[j] < self.seq[j + 1] if reversed else self.seq[i] > self.seq[j]):
                    self.seq[j], self.seq[j + 1] = self.seq[j + 1], self.seq[j]
        return self.seq

    # 选择排序
    def selection_sort(self, seq=None, reversed=False):
        if isinstance(seq, Iterable):
            # 函数可以接受传来的sequence
            self.seq = seq
        lens = len(self.seq)
        for i in range(lens):
            min_index = i
            for j in range(i + 1, lens):
                if (self.seq[min_index] < self.seq[j] if reversed else self.seq[i] > self.seq[j]):
                    min_index = j
            self.seq[i], self.seq[min_index] = self.seq[min_index], self.seq[i]

        return self.seq

    # 插入排序
    def insertion_sort(self, seq=None, reversed=False):
        if isinstance(seq, Iterable):
            # 函数可以接受传来的sequence
            self.seq = seq
        lens = len(self.seq)
        for i in range(1, lens):
            key = self.seq[i]
            j = i
            while j > 0 and (self.seq[j - 1] < self.seq[j] if reversed else self.seq[j - 1] > self.seq[j]):
                self.seq[j], self.seq[j - 1] = self.seq[j - 1], self.seq[j]
                j -= 1

        return self.seq

    # 归并排序(分）
    def merge_sort(self, seq):
        if len(seq) < 2:
            return seq
        mid = len(seq) // 2
        left = self.mergeSort(seq[:mid])
        right = self.mergeSort(seq[mid:])
        return self.merge(left, right)

    # 归并排序（治）
    def merge(self, left, right):
        if not len(left) or not len(right):
            return left or right
        result = []
        i, j = 0, 0

        while (len(result) < len(left) + len(right)):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            if i == len(left) or j == len(right):
                result.extend(left[i:] or right[j:])
                break
        return result

    # 快速排序
    def quick_sort(self, seq, start, end):
        if start < end:
            split = self.partition(seq, start, end)
            self.quickSort(seq, start, split - 1)
            self.quickSort(seq, split + 1, end)
        return seq

    @classmethod
    def partition(cls, seq, start, end):
        pivot_index = start - 1
        for i in range(start, end):
            # 选择最右边的为pivot
            if seq[i] < seq[end]:
                pivot_index += 1
                seq[pivot_index], seq[i] = seq[i], seq[pivot_index]
        seq[end], seq[pivot_index + 1] = seq[pivot_index + 1], seq[end]
        return pivot_index + 1


if __name__ == "__main__":
    basicSort = BasicSort([10, 1, 3, 5, 7, 9, 2, 4, 6, 8, 11, 15, 0, 12, 14, 13])
    # print(basicSort.bubbleSort(reversed=True))
    # print(basicSort.selectionSort(reversed=False))
    print(basicSort.insertion_sort(reversed=True))
    # print(basicSort.mergeSort([10, 1, 3, 5, 7, 9, 2, 4, 6, 8, 11, 15, 0, 12, 14, 13]))
    # print(basicSort.quickSort([10, 1, 3, 5, 7, 9, 2, 4, 6, 8, 11, 15, 0, 12, 14, 13],0,15))
