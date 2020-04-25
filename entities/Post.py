class Post(object):

    def __init__(self, id, author_id, title, body, comments=None):
        self.id = id
        self.author_id = author_id
        self.title = title
        self.body = body
        self.comments = comments

    @classmethod
    def from_dict(cls, adict):
        if "comments" in adict:
            post = Post(
                id=adict['id'],
                author_id=adict['author_id'],
                title=adict['title'],
                body=adict['body'],
                comments=adict['comments']
            )
        else:
            post = Post(
                id=adict['id'],
                author_id=adict['author_id'],
                title=adict['title'],
                body=adict['body']
            )

        return post

    def to_dict(self):
        return {
            'id': self.id,
            'author_id': self.author_id,
            'title': self.title,
            'body': self.body,
            'comments': self.comments
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

    def __repr__(self):
        return "%r" % (self.__dict__)

    def __getitem__(self,item):
        return self.item

