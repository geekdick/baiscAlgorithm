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
                if seqs[j] < seqs[j - 1]:
                    seqs[j ] = seqs[j-1]
                else:
                    seqs[j] = index_j
                    break
        print(seqs)
        return seqs


def test_sorted(sorted_func, seq_len=100):
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
    test_sorted(sim_sorted.selection_sorted)
    test_sorted(sim_sorted.insert_sorted)
