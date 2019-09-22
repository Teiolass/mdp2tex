class Symstack:
    def __init__(self):
        self.arr = []
        self.len = 0

    def add(self, el):
        if el == 'ENDBLOCK':
            assert self.len > 0
            la = self.arr.pop()
            self.len -= 1
            assert la['mode'] == 'block'
            return la['lat_end']
        if self.len > 0:
            if el == self.arr[-1] and not el['mode'] == 'block':
                self.arr.pop()
                self.len -= 1
                # print('Stack dequeue: {}'.format(el['name']))
                return el['lat_end']
        self.arr.append(el)
        # print('Stack enqueue: {}'.format(el['name']))
        self.len += 1
        return el['lat_begin']

