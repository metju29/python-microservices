from playwright.sync_api import APIRequestContext

import pytest
import logging


logger = logging.getLogger(__name__)


def test_get_products_list(api_request_context: APIRequestContext) -> None:
    get_products_list = api_request_context.get("/api/products")
    assert get_products_list.ok
    logger.info(f"Response_data: {get_products_list.json()}")
