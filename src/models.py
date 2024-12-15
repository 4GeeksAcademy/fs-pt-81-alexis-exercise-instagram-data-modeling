import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
class Followers(Base):
    __tablename__='followers'
    id=Column(Integer, primary_key=True)
    from_id=Column(Integer, ForeignKey('users.id'))
    to_id=Column(Integer, ForeignKey('users.id'))
    user_from_id=relationship('users', foreign_keys=[from_id], backref='Follower')
    user_to_id=relationship('users', foreign_keys=[to_id], backref='Followed')


    
class Users(Base):
    __tablename__='users'
    id= Column(Integer, primary_key=True)
    username=Column(String, nullable=False, unique=True)
    firstname= Column(String, nullable=False, unique=True)
    lastname=Column(String, nullable=False, unique=True)
    email=Column(String, nullable=False, unique=True)
    password=Column(String, nullable=False)
    city=Column(String)



    def to_dict(self):
        return {
            'id':self.id,
            'username':self.username,
            'email':self.email,
            'city':self.city
            
        }

class Posts(Base):
    __tablename__='posts'
    id=Column(Integer, primary_key=True)
    title=Column(String, nullable=False)
    content=Column(String)
    user_id=Column(Integer, ForeignKey('users.id'))
    user=relationship('users', backref='posts')

class Comments(Base):
    __tablename__='comments'
    id=Column(Integer, primary_key=True)
    content=Column(String)
    user_id=Column(Integer, ForeignKey('users.id'))
    user=relationship('user', backref='commments')
    post_id=Column(String, ForeignKey('posts.id'))
    post=relationship('user', backref='comments')

    class Media(Base):
        __tablename__='media'
        id=Column(Integer, primary_key=True)
        src=Column(String, nullable=False)
        post_id=Column(String, ForeignKey('posts.id'))
        post=Column(String, ForeignKey('comments.id'))

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
