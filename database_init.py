from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from database_setup import *

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete Categories if exisitng.
session.query(Category).delete()
# Delete Items if exisitng.
session.query(Items).delete()
# Delete Users if exisitng.
session.query(User).delete()

# Create fake users
User1 = User(name="Ajinkya Shinde",
              email="ajinkyas420@gmail.com",
              picture='')
session.add(User1)
session.commit()

## User2 = User(name="Ajinkya Shinde",
##               email="rgress1@t.co",
##               picture='http://dummyimage.com/200x200.png/cc0000/ffffff')
## session.add(User2)
## session.commit()

## User3 = User(name="Prasad Patrikar",
##               email="pblakemore2@bluehost.com",
##               picture='http://dummyimage.com/200x200.png/5fa2dd/ffffff')
## session.add(User3)
## session.commit()

## User4 = User(name="Nikhil londhe",
##               email="ebeetham3@google.com.au",
##               picture='http://dummyimage.com/200x200.png/ff4444/ffffff')
## session.add(User4)
## session.commit()

## User5 = User(name="Aniket Tare",
##               email="teyree4@wix.com",
##               picture='http://dummyimage.com/200x200.png/cc0000/ffffff')
## session.add(User5)
## session.commit()

# Create fake categories
Category1 = Category(name="Football",
                      user_id=1)
session.add(Category1)
session.commit()

Category2 = Category(name="Cars",
                      user_id=1)
session.add(Category2)
session.commit

Category3 = Category(name="Cricket",
                      user_id=1)
session.add(Category3)
session.commit()

Category4 = Category(name="Gadgets",
                      user_id=1)
session.add(Category4)
session.commit()

Category5 = Category(name="Food",
                      user_id=1)
session.add(Category5)
session.commit()

# Populate a category with items for testing
# Using different users for items also
Item1 = Items(name="Soccer cleats",
               date=datetime.datetime.now(),
               description="Shoes to play football in.",
               picture="https://images.sportsdirect.com/images/products/20120022_4pl.jpg",
               category_id=1,
               user_id=1)
session.add(Item1)
session.commit()

Item2 = Items(name="Football Shirt",
               date=datetime.datetime.now(),
               description="Shirt to play football in.",
               picture="https://cdn3.volusion.com/goz35.avhz4/v/vspfiles/photos/TT-ADAI5158-2.jpg?1474975984",
               category_id=1,
               user_id=1)
session.add(Item2)
session.commit()

Item3 = Items(name="Football",
               date=datetime.datetime.now(),
               description="A Football.",
               picture="http://bit.ly/2pJSPR1",
               category_id=1,
               user_id=1)
session.add(Item3)
session.commit()

Item1 = Items(name="Lamborghini",
               date=datetime.datetime.now(),
               description="Fastest car",
               picture="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Black_Lamborghini_Aventador%2C_pic1.JPG/220px-Black_Lamborghini_Aventador%2C_pic1.JPG",
               category_id=2,
               user_id=1)
session.add(Item1)
session.commit()

Item1 = Items(name="Bat",
               date=datetime.datetime.now(),
               description="Cricket bat",
               picture="https://www.cricketbazaar.in/wp-content/uploads/2017/07/MRF-Miniature-Autograph-Cricket-Bat-Not-for-Playing-Small-Size.jpg",
               category_id=3,
               user_id=1)
session.add(Item1)
session.commit()

print "Your database has been populated with fake data!"
