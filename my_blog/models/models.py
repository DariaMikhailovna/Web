import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, scoped_session
from faker import Faker
from random import randint

Base = declarative_base()
engine = sqlalchemy.create_engine('sqlite:///blog.db', echo=False)
Base.metadata.create_all(engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
session = Session()

tags_posts_table = sqlalchemy.Table('tags_posts', Base.metadata,
                                    sqlalchemy.Column('post_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('posts.id')),
                                    sqlalchemy.Column('tag_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('tags.id')),
                                    )


class Post(Base):
    __tablename__ = 'posts'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    title = sqlalchemy.Column(sqlalchemy.String(16))
    text = sqlalchemy.Column(sqlalchemy.Text)
    is_published = sqlalchemy.Column(sqlalchemy.Boolean)
    user = relationship("User", back_populates="posts", lazy='joined')
    tags = relationship("Tag", secondary=tags_posts_table, back_populates="posts")

    # def __repr__(self):
    #     return self.text

    @property
    def short(self):
        return self.text[:30]


class Tag(Base):
    __tablename__ = 'tags'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)

    posts = relationship("Post", secondary=tags_posts_table, back_populates="tags")


class User(Base):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    user_name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)

    posts = relationship("Post", back_populates="user")


def make_content():
    fake = Faker()

    for i in range(20):
        user = User(user_name=fake.name())
        session.add(user)

    for i in range(10):
        post = Post(user_id=randint(0, 19), title=fake.text(10), text=fake.text())
        session.add(post)
    session.commit()

    # tag1 = Tag(name='tag1', posts=[post1])
    # tag2 = Tag(name='tag2', posts=[post2, post3])
    # session.flush()
    # posts = session.query(Post).join(tags_posts_table).filter(tags_posts_table.c.tag_id == 2)
    # print(*posts)


def get_all_posts():
    posts = session.query(Post).all()
    return posts


if __name__ == '__main__':
    make_content()
    print(*get_all_posts())
