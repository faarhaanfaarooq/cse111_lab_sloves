class Product:
    def __init__(self,id, title, price):
        self.__id = id
        self. __title = title
        self. __price = price
    def get_id_title_price(self):
        return "ID: "+str(self.__id)+" Title:"+self.__title+ "Price: "+str(self.__price)

#write your code here
class Book(Product):
    def __init__(self, id, title, price, isbn, publisher):
        super().__init__(id, title, price)
        self.__isbn = isbn
        self.__publisher = publisher
    def printDetail(self):
        return super().get_id_title_price()+" ISBN: "\
            +str(self.__isbn)+" Publisher: "+self.__publisher

class CD(Product):
    def __init__(self, id, title,price, band, duration, genre):
        super().__init__(id, title, price)
        self.__band = band
        self.__duration = duration
        self.__genre = genre
    def printDetail(self):
        return super().get_id_title_price() + " Band: "+self.__band+" Duration: "\
            +str(self.__duration)+"minutes Genre: "+self.__genre

book = Book(1,"The Alchemist",500,"97806","HarperCollins")
print(book.printDetail())
print("-----------------------")
cd = CD(2,"Shotto",300,"Warfaze",50,"Hard Rock")
print(cd.printDetail())