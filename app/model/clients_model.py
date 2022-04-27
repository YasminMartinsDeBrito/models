
# branch = feature/model-clients

#  precisa fazer = pip install -r requirements.txt
from app.model.boxes_model import BoxesModel
from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref, validates
from dataclasses import dataclass
import re

# exc.py
# from app.model.exc import CpfInvalid
class CpfInvalid(Exception):
    ...



@dataclass
class ClientsModel(db.Model):
   
    id = int
    cpf = str
    name = str
    email = str
    total_points = int
    boxe = BoxesModel


    __tablename__ = "clients"   

    id = Column(Integer, primary_key=True)
    cpf = Column(String(11), nullable=False, unique=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    total_points = Column(Integer)
    box_flag = Column(String, ForeignKey("boxes.flag"))
    boxe = relationship("BoxesModel", backref=backref("client", uselist=False))



    @validates("cpf")
    def validate_cpf(self, key, cpf):
        if  key == "cpf" and len(cpf) != 11:
            raise CpfInvalid(description={"error":"Key `cpf` invalid, valid format ex: xxx.xxx.xxx-xx"})
        
        return cpf.isnumeric()



