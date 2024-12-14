from fastapi import FastAPI
from fastapi import HTTPException
import pytest
from app.controllers.product_controller import (
    get_all_products, 
    create_product, 
    update_product, 
    delete_product, 
    archive_product
    )
from app.schemas.product import (
    ProductCreate, 
    ProductUpdate, 
    ProductBase as Product
    )
from unittest.mock import mock_open, patch

app = FastAPI()

mock_file_data = [
    {"id": 1, "name": "A", "description": "desc_X", "price": 1200, "archived": False},
    {"id": 2, "name": "B", "description": "desc_A", "price": 1250, "archived": False},
    {"id": 3, "name": "C", "description": "desc_C", "price": 1300, "archived": False},
]

def test_get_all_products():
    with patch("app.controllers.product_controller.update_product"):
        with patch("app.controllers.product_controller.__get_all_data", return_value=mock_file_data):
            with patch("app.controllers.product_controller.file_path", "mocked_data.json"):
                #Sort by ascending
                assert [product["price"] for product in 
                    get_all_products("name", False)] == [1200, 1250, 1300]
                assert [product["price"] for product in 
                    get_all_products("description", False)] == [1250, 1300, 1200]
                assert [product["price"] for product in 
                    get_all_products("price", False)] == [1200, 1250, 1300]
                #Sort by descending
                assert [product["price"]  for product in 
                    get_all_products("name", True)] == [1300, 1250, 1200]
                assert [product["price"] for product in 
                    get_all_products("description", True)] == [1200, 1300, 1250]
                assert [product["price"] for product in 
                    get_all_products("price", True)] == [1300, 1250, 1200]

                #Invalide sort
                with pytest.raises(HTTPException) as exc_info:
                    get_all_products("invalid_field", False)
                assert exc_info.value.status_code == 400


def test_create_product():
    with patch("app.controllers.product_controller.update_product"):
        with patch("app.controllers.product_controller.__get_all_data", return_value=mock_file_data):
            with patch("app.controllers.product_controller.file_path", "mocked_data.json"):
                product_to_create =  ProductCreate(name="new", description="desc_z", price=1800)
                assert create_product(product_to_create) == "success"
                assert len(mock_file_data) == 4
                delete_product(3)

def test_update_product():
    with patch("app.controllers.product_controller.update_product"):
        with patch("app.controllers.product_controller.__get_all_data", return_value=mock_file_data):
            with patch("app.controllers.product_controller.file_path", "mocked_data.json"):
                    product_update =  ProductUpdate(name="new", description="desc_z", price=1800)
                    assert update_product(1, product_update) == "success"
                    assert mock_file_data[0]["name"] == "new"

def test_archive_product():
    with patch("app.controllers.product_controller.archive_product"):
        with patch("app.controllers.product_controller.__get_all_data", return_value=mock_file_data):
            with patch("app.controllers.product_controller.file_path", "mocked_data.json"):
                    assert mock_file_data[1]["archived"] == False
                    assert archive_product(2) == "success"
                    assert mock_file_data[1]["archived"] == True
                    
def test_delete_product():
    with patch("app.controllers.product_controller.update_product"):
        with patch("app.controllers.product_controller.__get_all_data", return_value=mock_file_data):
            with patch("app.controllers.product_controller.file_path", "mocked_data.json"):
                assert len(mock_file_data) == 3
                assert delete_product(1) == "success"
                assert len(mock_file_data) == 2

