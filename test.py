import random as rd


class Test:
    def __init__(self, row=10, col=10, min_=0, max_=100):
        self.row = row
        self.col = col
        self.min_ = min_
        self.max_ = max_

    def test_data(self):
        res = []
        for _ in range(self.row):
            tmp = []
            for _ in range(self.col):
                tmp.append(rd.randint(self.min_, self.max_))
            res.append(tmp)
        return res
