class User:
    def __init__(self):
        self.__id: str
        self.__email: str
        self.__password: str
    
    def set_id(self, id: str):
        self.__id = id
        return self
    
    def get_id(self) -> str:
        return self.__id if self.__id else ""
    
    def set_email(self, email: str):
        self.__email = email
        return self

    def get_email(self) -> str:
        return self.__email if self.__email else ""
    
    def set_password(self, password: str):
        self.__password = password
        return self

    def get_password(self) -> str:
        return self.__password if self.__password else ""