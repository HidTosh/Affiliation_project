import requests
import random

BASE_URL = "http://127.0.0.1:8000"
#BASE_URL = "http://ww_api:8000" #if docker is set in same network as ww_api
def main():
    
    product = get_random_product(get_products_list())
    purchase_product(product["base_url"])

def get_products_list():
    try:
        response = requests.get(f"{BASE_URL}/products")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Erreur : {response.status_code} - {response.text}")
    except Exception as e:
        print(f"error : {e}")

def purchase_product(base_url):
    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            print(response.json)
            return response.json()
        else:
            print(f"Erreur : {response.status_code} - {response.text}")
    except Exception as e:
        print(f"error : {e}")


def get_random_product(products):
    probabilities = [10, 5, 2.5]
    print(products)
    while len(probabilities) < len(products):
        probabilities.append(random.choice(probabilities))
    total_probability = sum(probabilities)
    probabilities = [p / total_probability for p in probabilities]

    return random.choices(products, weights=probabilities, k=1)[0]

if __name__ == "__main__":
    main()