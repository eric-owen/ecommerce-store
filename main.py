import pandas as pd


class Store:
    def __init__(self, csv_file):
        self.products = self.load_products(csv_file)

    def load_products(self, csv_file):
        df = pd.read_csv(csv_file, dtype={"id": str})
        return df

    def find_product(self, material_id):
        product = self.products.loc[self.products['id'] == material_id]
        return product if len(product) > 0 else None

    def purchase(self, material_id, quantity):
        product = self.find_product(material_id)
        if product is None:
            print('Product not found')
            return
        if product.loc[:, 'in stock'].item() < quantity:
            print("insufficient quantity")
            return

        current_stock = product.at[product.index[0], 'in stock']
        updated_stock = current_stock - quantity
        self.products.at[product.index[0], 'in stock'] = updated_stock

        self.products.to_csv('products.csv', index=False)
        print(f"purchased {quantity} units of {product['name']}")

    def __str__(self):
        return str(self.products)


class Receipt:
    def __init__(self):
        pass


store = Store('articles.csv')
print(store)
material_id = input("enter the id of the product you'd like to purchase: ")
quantity = int(input('enter quantity: '))
store.purchase(material_id, quantity)
print(store)
