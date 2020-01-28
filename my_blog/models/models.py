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

user_info = {'id': 1, 'user_name': 'Dasha'}
session.add(User(**user_info))
user_info = {'id': 2, 'user_name': 'Masha'}
session.add(User(**user_info))
post_info = {'id': 1, 'user_id': 1, 'title': 'Dasha first post'}
session.add(Post(**post_info))
post_info = {'id': 2, 'user_id': 2, 'title': 'Masha first post'}
session.add(Post(**post_info))
post_info = {'id': 3, 'user_id': 1, 'title': 'Dasha second post'}
session.add(Post(**post_info))
tags_info = {'id': 1, 'name': 'Tag1'}
session.add(Tag(**tags_info))
tags_info = {'id': 2, 'name': 'Tag2'}
session.add(Tag(**tags_info))
# tags_posts_info = {'id': 1, 'tag_id': 1}
# session.add(Tag(**post_info))
# tags_posts_info_2 = {'id': 2, 'tag_id': 2}
# session.add(Post(**post_info))
session.commit()
