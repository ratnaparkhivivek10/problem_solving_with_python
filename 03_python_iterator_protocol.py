class Sequence(object):
    def __init__(self, *items):
        self._items = items
        self._cursor = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._items) == self._cursor:
            raise StopIteration

        e = self._items[self._cursor]
        self._cursor += 1

        return e


seq = Sequence(1, 2, 3, 4, 5)
for i in seq:
    print(i)

seq = Sequence(6, 7, 8)
seq_iter = iter(seq)
print(next(seq_iter))



