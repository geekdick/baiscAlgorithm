import random

from sorted_demo.sorted_test import SortedTest


class SimSorted:

    # 选择排序
    @staticmethod
    def selection_sorted(seqs):
        last_index = len(seqs)
        for i in range(last_index):
            min_index = i
            # 每一轮找出最小值，进行交换
            for j in range(i + 1, last_index):
                if seqs[j] < seqs[min_index]:
                    min_index = j
            seqs[i], seqs[min_index] = seqs[min_index], seqs[i]

        return seqs

    # 插入排序
    @staticmethod
    def insert_sorted(seqs):
        last_index = len(seqs)
        for i in range(1, last_index):
            index_j = seqs[i]
            for j in range(i, 0, -1):
                if index_j < seqs[j - 1]:
                    seqs[j] = seqs[j - 1]
                else:
                    seqs[j] = index_j
                    break
            else:
                seqs[0] = index_j
        return seqs

    @classmethod
    def merge_sorted(cls, seqs):
        if len(seqs) < 2:
            return seqs

        mid = len(seqs) // 2
        left_parts = cls.merge_sorted(seqs[:mid])
        right_parts = cls.merge_sorted(seqs[mid:])
        return cls.__merge(left_parts, right_parts)

    @staticmethod
    def __merge(left_parts, right_parts):
        if not (left_parts and right_parts):
            return left_parts or right_parts
        len_left_parts = len(left_parts)
        len_right_parts = len(right_parts)
        result = []
        left_index = 0
        right_index = 0
        while 1:
            left_value = left_parts[left_index]
            right_value = right_parts[right_index]
            if left_value < right_value:
                result.append(left_value)
                left_index += 1
            else:
                result.append(right_value)
                right_index += 1
            if (left_index >= len_left_parts) or (right_index >= len_right_parts):
                result.extend(left_parts[left_index:] or right_parts[right_index:])
                break

        return result

    @classmethod
    def quick_sort(cls, seqs, start=None, end=None):
        if start is None:
            start = 0
        if end is None:
            end = len(seqs)
        if start < end:
            pivot = cls.partition(seqs, start, end)
            cls.quick_sort(seqs, start, pivot)
            cls.quick_sort(seqs, pivot + 1, end)
        else:
            return seqs

    @staticmethod
    def partition(seqs, start, end):
        pivot_index = start
        rand_index = random.randrange(start, end)  # 优化，随机取标定点，以解决近乎有序的列表
        seqs[start], seqs[rand_index] = seqs[rand_index], seqs[start]
        pivot_val = seqs[start]
        for index in range(start + 1, end):
            if pivot_val > seqs[index]:
                pivot_index += 1
                seqs[pivot_index], seqs[index] = seqs[index], seqs[pivot_index]

        seqs[pivot_index], seqs[start] = seqs[start], seqs[pivot_index]
        return pivot_index


if __name__ == '__main__':
    sim_sorted = SimSorted()
    sorted_test = SortedTest(length=10000).sorted_test
    # sorted_test.(sim_sorted.selection_sorted)
    # sorted_test(sim_sorted.insert_sorted)
    # sorted_test(sim_sorted.merge_sorted)
    sorted_test(sim_sorted.quick_sort)
