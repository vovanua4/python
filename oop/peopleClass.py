
class People:
    secondName='None'
    firstName='None'
    age='0'
    city='0'

    def __str__(self):
        strReturn = str(self.secondName.capitalize()) + ' ' +  str( self.firstName.capitalize())
        return strReturn

