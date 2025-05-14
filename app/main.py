import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://myuser:mypassword@db:5432/mydb")

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Integer)

def list_items():
    with Session() as session:
        items = session.query(Item).all()
        for item in items:
            print(f"{item.id}: {item.name} (qty: {item.quantity})")

def create_item(name, quantity):
    with Session() as session:
        item = Item(name=name, quantity=quantity)
        session.add(item)
        session.commit()
        print(f"Created: {item.id} - {item.name}")

def update_item(item_id, name=None, quantity=None):
    with Session() as session:
        item = session.query(Item).get(item_id)
        if not item:
            print("Item not found")
            return
        if name:
            item.name = name
        if quantity is not None:
            item.quantity = quantity
        session.commit()
        print(f"Updated: {item.id} - {item.name} (qty: {item.quantity})")

def delete_item(item_id):
    with Session() as session:
        item = session.query(Item).get(item_id)
        if not item:
            print("Item not found")
            return
        session.delete(item)
        session.commit()
        print(f"Deleted item {item_id}")

if __name__ == "__main__":
    # Example usage
    list_items()
    create_item("Orange", 15)
    update_item(1, quantity=99)
    # delete_item(2)
    list_items()
