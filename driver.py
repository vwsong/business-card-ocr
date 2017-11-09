# Unit testing + driver .py file 

import BusinessCardParser
import unittest

test1 = """Foobar Technologies
Analytic Developer
Lisa Haung
1234 Sentry Road
Columbia, MD 12345
Phone: 410-555-1234
Fax: 410-555-4321
lisa.haung@foobartech.com"""

test2 = """
ASYMMETRIK LTD
Mike Smith
Senior Software Engineer
(410)555-1234
msmith@asymmetrik.com
"""

test3 = """
Arthur Wilson
Software Engineer
Decision & Security Technologies
ABC Technologies
123 North 11th Street
Suite 229
Arlington, VA 22209
Tel: +1 (703) 555-1259
Fax: +1 (703) 555-1200
awilson@abctech.com
"""

class TestStringMethods(unittest.TestCase):

    def printAttributes(self, contactInfo):
        return (contactInfo.getName(), contactInfo.getPhoneNumber(), contactInfo.getEmailAddress())

    def test1(self):
        t1 = BusinessCardParser.getContactInfo(test1)
        self.assertEqual(self.printAttributes(t1), ("Lisa Haung", "410-555-1234", "lisa.haung@foobartech.com"))

    def test2(self):
        t2 = BusinessCardParser.getContactInfo(test2)
        self.assertEqual(self.printAttributes(t2), ("Mike Smith", "(410)555-1234", "msmith@asymmetrik.com"))

    def test3(self):
        t3 = BusinessCardParser.getContactInfo(test3)
        self.assertEqual(self.printAttributes(t3), ("Arthur Wilson", "+1 (703) 555-1259", "awilson@abctech.com"))

if __name__ == '__main__':
    unittest.main()
