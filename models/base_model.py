import uuid
from datetime import datetime
 
class BaseModel:
    """defines all common attributes and methods
        for other classes
    """ 
    def __init__(self):        
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    def __str__(self):
        streeng = "[" + str(self.__class__.__name__) + "] (" 
        streeng = streeng + str(self.id) + ") " + str(self.__dict__)
        return streeng
    def save(self):
        self.updated_at = datetime.now()
    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
