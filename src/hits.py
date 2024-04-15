class hits:
    def __init__(self):
        self.count=0
        if cursor_hit:
            self.count+=1
    def hits(self):
        return self.count