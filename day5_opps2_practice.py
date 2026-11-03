'''Level 1

Make a class called Book. Its __init__ takes a title and a number of pages, and
stores both on the object. Add a method called show that prints the title and pages in one line.'''
class Book:
    def __init__(self,title,no_of_page):
        self.title=title
        self.no_of_page=no_of_page
        self.current_page=0
    def show(self):
        print(self.title,self.no_of_page)


    def get_pages(self):
        return self.no_of_page
    def is_long(self):
        if self.no_of_page>=100:
            return True
        else:
            return False

    def read(self,n):
        self.current_page=self.current_page+n
        if self.current_page>self.no_of_page:
            self.current_page=self.no_of_page
    def page_left(self):
        return self.no_of_page-self.current_page

        
        
b1=Book("oo",88)
b2=Book("pp",103)
b3=Book("gg",99)
book=[b1,b2,b3]
for s in book:
    s.show()