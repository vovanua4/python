import shelve , peopleClass


class book():
    """
    telefonnaya kniga
    na shelve
    """
    openFile=''
    fail = ''
    people = list()

    def __init__(self):
        self.fail = 'www'
        self.load()


    def __del__(self):
        self.save()


    def save(self):
        openFail = shelve.open(self.openFile)
        openFail['people'] = self.people
        openFail.close()

    def load(self):
        openFail= shelve.open(self.fail)
        self.people =  openFail ['people']
        openFail.close()

    def add(self,secondName ='None', firstname = 'none' , age ='0', sity = 'None', company ='None'):
        personal = peopleClass.People()
        personal.firstname = firstname
        personal.secondName = secondName
        personal.city = sity
        personal.age = age
        personal.company = company


        self.people.append(personal)

    def __str__(self):
        peoplList = list()
        for peopl in self.people:
            strPeopl = str(peopl)
            peoplList.append(strPeopl)
        return str(peoplList)
















