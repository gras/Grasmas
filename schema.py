from pydantic import BaseModel


class GiftBase(BaseModel):
    giver: str


class GiftCreate(GiftBase):
    gift_desc: str
    receiver: str
    author: str


class Gift(GiftBase):
    id: int

    class Config:
        orm_mode = True
