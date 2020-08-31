class our_range():

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration

        cur = self.start
        self.start += 1
        return cur


my_range = our_range(1, 10)
