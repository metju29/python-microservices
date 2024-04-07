from playwright.sync_api import APIRequestContext

import logging


logger = logging.getLogger(__name__)


def test_user_get(api_request_context: APIRequestContext) -> None:
    get_user = api_request_context.get(f"/api/user")
    assert get_user.ok
    logger.info(f"Response_data: {get_user.json()}")
