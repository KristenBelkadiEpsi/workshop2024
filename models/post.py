class Post:
    def __init__(self, id, text):
        self.id = id
        self.text = text

    def __str__(self):
        return "(id = %s, text = %s)" % (self.id, self.text)
