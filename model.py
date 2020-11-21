from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Gift(Base):
    __tablename__ = "gift"
    id = Column(Integer, primary_key=True, index=True)
    giver = Column(String(15))
    gift_desc = Column(String(150))
    receiver = Column(String(15))
    author = Column(String(15))
