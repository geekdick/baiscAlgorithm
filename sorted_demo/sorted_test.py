import random
import time
import logging
from collections import Iterable
from contextlib import contextmanager


class SortedTest:
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s\t%(levelname)s %(lineno)s\t%(message)s")

    def __init__(self, length=100):
        self.length = length

    def sorted_test(self, sorted_func):
        for array in self.get_test_array_func():
            test_array = getattr(self, array)
            seqs = test_array()
            with self.time_consume(seqs, test_array.__name__, sorted_func.__name__):
                result = sorted_func(seqs)
                if isinstance(result, Iterable):
                    assert result == sorted(seqs)
                else:
                    assert seqs == sorted(seqs)
        logging.info('')

    def get_test_array_func(self, suffix='_array'):
        return [attr for attr in dir(self) if str(attr).endswith(suffix) and callable(getattr(self, attr))]

    @staticmethod
    def empty_array():
        return []

    @staticmethod
    def single_array():
        return [random.randrange(1, 10)]

    def duplicate_array(self, length=None):
        if not length:
            length = self.length
        return [1] * length

    def sorted_array(self, length=None):
        if not length:
            length = self.length
        return list(range(length))

    def reversed_array(self, length=None):
        if not length:
            length = self.length
        return list(range(length, 0, -1))

    def rand_array(self, length=None, min_num=None, max_num=None):
        if not length:
            length = self.length
        if not min_num:
            min_num = 0
        if not max_num:
            max_num = length
        return [random.randrange(min_num, max_num) for _ in range(length)]

    @contextmanager
    def time_consume(self, seq, seq_type, func_name):
        start_time = time.time()
        try:
            yield
        finally:
            end_time = time.time()
            consume = end_time - start_time
        logging.info("将长度 {} {} 队列，进行 {} 排序 耗费 {}".format(len(seq), seq_type, func_name, consume))


def my_sorted(seqs):
    return sorted(seqs)


if __name__ == '__main__':
    sorted_test = SortedTest(length=100)
    sorted_test.sorted_test(sorted_func=my_sorted)
