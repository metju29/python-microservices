import random

from playwright.sync_api import APIRequestContext

import pytest
import logging


logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def product_id_get(api_request_context: APIRequestContext):
    product_list_get = api_request_context.get("/api/products")

    assert product_list_get.ok
    product_list = product_list_get.json()
    product_ids_lists = []
    for product in product_list:
        product_ids_lists.append(product['id'])
    product_id = random.choice(product_ids_lists)
    return product_id


def test_get_products_list(api_request_context: APIRequestContext) -> None:
    products_list_get = api_request_context.get("/api/products")
    assert products_list_get.ok
    logger.info(f"Response_data: {products_list_get.json()}")


def test_take_like(api_request_context: APIRequestContext, product_id_get) -> None:
    product_id = product_id_get
    like_take = api_request_context.post(f"/api/products/{product_id}/like")
    assert like_take.ok
    logger.info(f"Response_data: {like_take.json()}")
