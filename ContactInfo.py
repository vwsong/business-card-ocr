# Class definition for contacts.

class ContactInfo:

    def __init__(self, name, phoneNumber, emailAddress):
        self.name = name
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress

    def getName(self):
        return self.name

    def getPhoneNumber(self):
        return self.phoneNumber

    def getEmailAddress(self):
        return self.emailAddress
