# "Учёт товаров"

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop():
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products_str = file.read()
        file.close()
        return products_str

    def add(self, *products):
        file = open(self.__file_name, 'a+')
        file.seek(0) # устанавливаем курсор в начало файла, чтобы считать содержимое
        str_from_file = file.read()

        str_to_add = ''
        for product in products:
            if str(product) not in str_from_file:
                str_to_add += f'{str(product)}\n'
            else:
                print(f'Продукт {str(product)} уже есть в магазине')

        file.write(str_to_add)
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())
