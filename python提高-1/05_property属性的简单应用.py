class Page(object):
    def __init__(self, cur_page):
        self.cur_page = cur_page
        self.items = 100

    @property
    def start(self):
        val = (self.cur_page - 1) * self.items + 1
        return val

    @property
    def end(self):
        val = self.cur_page * self.items
        return val

p = Page(20)
print(p.start)
print(p.end)

