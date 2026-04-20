class studentClass:

    def __init__(self, firstName, lastName, studentNumber, year, email, ppsNo, middleName):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__studentNumber = studentNumber
        self.year = year
        self.__email = email

        #private attributes
        self.ppsNo = ppsNo
        self.middleName = middleName


    #private variables cannot be accessed directly outside the class
    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getStudentNumber(self):
        return self.__studentNumber

    def getEmail(self):
        return self.__email

    #setters
    def setFirstName (self, firstName):
        self.__firstName = firstName
        
    def setLastName (self, lastName):
        self.__lastName = lastName

    def setStudentNumber (self, studentNumber):
        self.__studentNumber = studentNumber

    def setEmail (self, email):
        self.__email = email

    

        # creating 4 student objects
s1 = studentClass(
    firstName="Alice",
    lastName="Murphy",
    studentNumber="S1234567",
    year=1,
    email="alice.murphy@example.com",
    ppsNo="1234567A",
    middleName="Rose"
)

s2 = studentClass(
    firstName="Brian",
    lastName="O'Connor",
    studentNumber="S2345678",
    year=2,
    email="brian.oconnor@example.com",
    ppsNo="2345678B",
    middleName="James"
)

s3 = studentClass(
    firstName="Ciara",
    lastName="Kelly",
    studentNumber="S3456789",
    year=3,
    email="ciara.kelly@example.com",
    ppsNo="3456789C",
    middleName="Anne"
)

s4 = studentClass(
    firstName="David",
    lastName="Walsh",
    studentNumber="S4567890",
    year=4,
    email="david.walsh@example.com",
    ppsNo="4567890D",
    middleName="Michael"
)

#getters


print(f"{s1.getFirstName()}'s email is {s1.getEmail()}") 

