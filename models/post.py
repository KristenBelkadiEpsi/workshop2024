class Post:
    def __init__(self, id, text, date_created):
        self.id = id
        self.text = text
        self.date_created = date_created

    def __str__(self):
        return "(id = %s, text = %s, date_created = %s)" % (
            self.id,
            self.text,
            self.date_created,
        )
