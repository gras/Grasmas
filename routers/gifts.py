from fastapi import APIRouter
from fastapi_sqlalchemy import db

# the following line of code are to import the gift in our model and schema
from model import Gift as ModelGift
from schema import GiftCreate as SchemaGift
from schema import Gift as Gifts

router = APIRouter()


@router.post("/register", response_model=Gifts)
async def create_gift(gift: SchemaGift):
    Gift = ModelGift(giver=gift.giver, gift_desc=gift.gift_desc, receiver=gift.receiver, author=gift.author)
    db.session.add(Gift)
    db.session.commit()
    db.session.refresh(Gift)
    return Gift


@router.get("/test", response_model=Gifts)
async def list_all_gifts():
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM gifts")
    myresult = mycursor.fetchall()
    return myresult
