class Locator:
    a = ""
    def __init__(self):
        self.a = "С"
    def __napravo__(self):
        if self.a == "С":
            self.a = "В"
        elif self.a == "В":
            self.a = "Ю"
        elif self.a == "Ю":
            self.a = "З"
        elif self.a == "З":
            self.a = "С"
    def __nalevo__(self):
        if self.a == "С":
            self.a = "З"
        elif self.a == "З":
            self.a = "Ю"
        elif self.a == "Ю":
            self.a = "В"
        elif self.a == "В":
            self.a = "С"
    def __na180__(self):
        if self.a == "С":
            self.a = "Ю"
        elif self.a == "Ю":
            self.a = "С"
        elif self.a == "З":
            self.a = "В"
        elif self.a == "В":
            self.a = "З"
        
    def current_pos(self):
        return self.a
    def povorot(self, storona):
        if storona == 1:
            self.__napravo__()
        elif storona == 2:
            self.__nalevo__()
        elif storona == 3:
            self.__na180__()