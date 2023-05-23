import pandas as pd

class Store:
    def __init__(self, csv_file):
        self.products = self.load_products(csv_file)

    def load_products(self, csv_file):
        df = pd.read_csv(csv_file)
        return df

    def __str__(self):
        return f"{self.products}"

class Receipt:
    def __init__(self):
        pass

store = Store('articles.csv')
print(store)
