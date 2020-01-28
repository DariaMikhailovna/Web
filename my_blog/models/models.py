import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()

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

    def __repr__(self):
        return self.text


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


engine = sqlalchemy.create_engine('sqlite:///blog.db', echo=False)
Base.metadata.create_all(engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
session = Session()

user1 = User(user_name='Dasha')
user2 = User(user_name='Masha')
session.add(user1)
session.add(user2)
post1 = Post(user_id=user1.id, title='title1', text='text1')
post2 = Post(user_id=user2.id, title='title2', text='text2')
post3 = Post(user_id=user2.id, title='title3', text='text3')
session.add(post1)
session.add(post2)
session.add(post3)
tag1 = Tag(name='tag1', posts=[post1])
tag2 = Tag(name='tag2', posts=[post2, post3])
session.flush()
posts = session.query(Post).join(tags_posts_table).filter(tags_posts_table.c.tag_id == 2)
print(*posts)
session.commit()
