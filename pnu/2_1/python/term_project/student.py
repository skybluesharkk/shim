
class student:
    def __init__(self,name,phonenumber,seat,time,is_studycafe):
        self.name = name
        self.phonenumber = phonenumber
        self.seat = seat
        self.time = time
        self.is_studycafe = is_studycafe

class studycafe(student):
    def __init__(self,name,phonenumber,seat,time):
        super().__init__(name,phonenumber,seat,time,True)


class studyroom(student):
    def __init__(self, name, phonenumber, seat, time):
        super().__init__(name, phonenumber, seat, time,False)

shim = student("shim","01091505324",1,"d",True)
print(shim.name)
