from sqlalchemy import Column, String, Integer

from base import Base

class Article(Base):
    __tablename__ = 'articles'

    id = Column(String, primary_key= True)
    body = Column(String)
    host = Column(String)
    title = Column(String)
    newspaper_uid = Column(String)
    n_tokensbody = Column(Integer)
    n_tokenstitle = Column(Integer)
    url = Column(String, unique=True)

    def __init__(self, uid, body, host, newspaper_uid, n_tokensbody,n_tokenstitle, title, url):
        self.id = uid
        self.body = body
        self.host = host
        self.newspaper_uid = newspaper_uid
        self.n_tokensbody = n_tokensbody
        self.n_tokenstitle = n_tokenstitle
        self.title = title
        self.url = url
