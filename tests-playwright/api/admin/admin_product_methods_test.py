from playwright.sync_api import APIRequestContext

import pytest
import logging


logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def new_product_prepare(api_request_context: APIRequestContext):
    create_data = {
        "title": "title",
        "image": "image"
    }
    create_new_product = api_request_context.post("/api/products", data=create_data)
    assert create_new_product.status == 201
    product_id = create_new_product.json()['id']
    return product_id


def test_get_products_list(api_request_context: APIRequestContext) -> None:
    get_products_list = api_request_context.get("/api/products")
    assert get_products_list.status == 200
    logger.info(f"Response_data: {get_products_list.json()}")


def test_create_new_product(api_request_context: APIRequestContext) -> None:
    data = {
        "title": "title",
        "image": "image"
    }
    create_new_product = api_request_context.post("/api/products", data=data)
    assert create_new_product.status == 201
    logger.info(f"Response_data: {create_new_product.json()}")


def test_retrieve_product(api_request_context: APIRequestContext, new_product_prepare) -> None:
    product_id = new_product_prepare

    retrieve_product = api_request_context.get(f"/api/products/{product_id}")
    assert retrieve_product.status == 200
    logger.info(f"Response_data: {retrieve_product.json()}")


def test_update_product(api_request_context: APIRequestContext, new_product_prepare) -> None:
    product_id = new_product_prepare

    update_data = {
        "title": "new title",
        "image": "new image"
    }
    update_product = api_request_context.put(f"/api/products/{product_id}", data=update_data)
    assert update_product.status == 202
    logger.info(f"Response_data: {update_product.json()}")


def test_destroy_product(api_request_context: APIRequestContext, new_product_prepare) -> None:
    product_id = new_product_prepare

    # Delete product
    destroy_product = api_request_context.delete(f"/api/products/{product_id}")
    assert destroy_product.status == 204

    # Checking product doesn't exist
    retrieve_product = api_request_context.get(f"/api/products/{product_id}")
    # assert retrieve_product.ok
    assert retrieve_product.status == 204
