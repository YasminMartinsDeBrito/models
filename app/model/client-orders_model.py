
from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship, backref
from dataclasses import dataclass
from app.model.clients_model import ClientsModel
from app.model.order_model import OrderModel


@dataclass
class ClientModel(db.Model):

    order_id = OrderModel
    client_id = ClientsModel

    __tablename__ = "client_orders"

    order_id = Column(Integer, ForeignKey("orders.id"))
    client_id = Column(Integer, ForeignKey("clients.id"))
    orderId = relationship("OrderModel", backref=backref("order", uselist=False))
    clientId = relationship("ClientsModel",backref=backref("client", uselist=False))



