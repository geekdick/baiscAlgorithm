import random
import time
from contextlib import contextmanager


class SimSorted:

    def __init__(self):
        pass

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


def test_sorted(sorted_func, seq_len=10000):
    large_seq = rand_array(seq_len)
    with time_consume(large_seq, sorted_func.__name__):
        sim_seq = sorted_func(large_seq)
    assert sim_seq == sorted(large_seq)


def rand_array(length, min_num=None, max_num=None):
    if not min_num:
        min_num = 0
    if not max_num:
        max_num = length
    return [random.randrange(min_num, max_num) for _ in range(length)]


@contextmanager
def time_consume(seq, func_name):
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        consume = end_time - start_time
    print("将长度 {} 进行 {} 排序 耗费 {}".format(len(seq), func_name, consume))


if __name__ == '__main__':
    sim_sorted = SimSorted()
    # test_sorted(sim_sorted.selection_sorted)
    # test_sorted(sim_sorted.insert_sorted)
    test_sorted(sim_sorted.merge_sorted)
