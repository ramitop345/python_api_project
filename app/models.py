from .database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, func
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import TIMESTAMP

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key = True, autoincrement=True, nullable = False)
    title = Column(String(200) , nullable = False)
    content = Column(String(3000), nullable = False)
    published = Column(Boolean, server_default ='1', nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), nullable = False, server_default=func.now())
    user_id = Column(Integer, ForeignKey("users.id", ondelete = "CASCADE"), nullable = False)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True, autoincrement=True, nullable = False)
    email = Column(String(50), nullable = False, unique = True)
    password = Column(String(400), nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), nullable = False, server_default=func.now())