class Comment(object):

    def __init__(self, id, post_id, title, body):
        self.id = id
        self.post_id = post_id
        self.title = title
        self.body = body

    @classmethod
    def from_dict(cls, adict):
        user = User(
            id=adict['id'],
            post_id=adict['post_id'],
            title=adict['title'],
            body=adict['body']
        )

        return user

    def to_dict(self):
        return {
            'id': self.id,
            'post_id': self.post_id,
            'title': self.title,
            'body': self.body
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

    def __repr__(self):
        return "%r" % (self.__dict__)

