from .database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, func
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key = True, autoincrement=True, nullable = False)
    title = Column(String(200) , nullable = False)
    content = Column(String(3000), nullable = False)
    published = Column(Boolean, server_default ='1', nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), nullable = False, server_default=func.now())
    user_id = Column(Integer, ForeignKey("users.id", ondelete = "CASCADE"), nullable = False)

    #this provides a relationship between two map classes
    owner = relationship("User")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True, autoincrement=True, nullable = False)
    email = Column(String(50), nullable = False, unique = True)
    password = Column(String(400), nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), nullable = False, server_default=func.now())

#two primary keys in this class make a composite key
class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey("users.id", ondelete = "CASCADE"), primary_key = True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete = "CASCADE"), primary_key = True)