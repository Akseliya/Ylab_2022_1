class CyclicIterator:
    def __init__(self, iter_object):
        self.iter_object = iter_object
        self.iterator = iter(iter_object)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                return next(self.iterator)
            except StopIteration:
                self.iterator = iter(self.iter_object)


cyclic_iterator = CyclicIterator(range(3))
for i in cyclic_iterator:
    print(i)
