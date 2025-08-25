# %%
import csv

path_file = "sales.csv"

def read_csv(csv_file_name: str) -> list[dict]:
    data = []
    try:
        with open(csv_file_name, mode="r", encoding="UTF-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row = {key.strip(): value for key, value in row.items()}
                data.append(row)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{csv_file_name}' não foi encontrado.")
    return data

def filter_products_delivered(data: list[dict]) -> list[dict]:
    list_with_filter_products = []
    for product in data:
        delivered_status = product.get("delivered", "").strip().lower()
        if delivered_status == "true":
            list_with_filter_products.append(product)
    return list_with_filter_products

products_list = read_csv(path_file)
delivered_products = filter_products_delivered(products_list)

print(delivered_products)