class Field():
    def __init__(self,name,value):
        setattr(self,name,value)
    
    @staticmethod
    def from_dict(json):
        return Field(json['name'],json['value'])        

    def __iter__(self):
        yield vars(self)

    def __str__(self):
        return str(vars(self))


