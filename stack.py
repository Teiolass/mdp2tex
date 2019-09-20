class Symstack:
    def __init__(self):
        self.arr = []
        self.len = 0

    def add(self, el):
        if self.len > 0:
            if el == self.arr[-1]:
                self.arr.pop()
                self.len -= 1
                return el['lat_end']
        self.arr.append(el)
        self.len += 1
        return el['lat_begin']

