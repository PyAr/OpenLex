# Playwright video recording original implementation:
#   https://github.com/alethcoe/playwright_recording_pytest

from typing import Any, Dict, Generator, List

import pytest
from playwright.sync_api import (
    Browser,
    BrowserContext,
    Page,
)

import os
import shutil


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, video_path):
    return {
        **browser_context_args,
        "record_video_dir": video_path,
        "viewport": {"width": 1920, "height": 1080},
    }


@pytest.fixture(scope="session")
def video_path():
    return "./videos"


def pytest_sessionstart(session):
    """
    Called before test run starts
    """
    if os.path.exists("./videos"):
        for filename in os.listdir("./videos"):
            filepath = os.path.join("./videos", filename)
            try:
                shutil.rmtree(filepath)
            except OSError:
                os.remove(filepath)


@pytest.fixture
def page(context: BrowserContext, base_url: str) -> Generator[Page, None, None]:
    page = context.new_page()
    page._goto = page.goto  # type: ignore
    page.goto = lambda *args, **kwargs: _handle_page_goto(  # type: ignore
        page, list(args), kwargs, base_url
    )
    yield page

    # save off the test unique id
    current_path_name = context.pages[0].video.path()
    BrowserContext.current_video_name = current_path_name

    page.close()


@pytest.fixture
def context(
    browser: Browser, browser_context_args: Dict, browser_name, video_path, request
) -> Generator[BrowserContext, None, None]:
    context = browser.new_context(**browser_context_args)
    current_failed_tests = request.session.testsfailed
    yield context
    current_video_name = context.current_video_name
    current_video_path = current_video_name
    updated_video_path = os.path.join(
        video_path, f"{request.node.originalname}_{browser_name}.mp4"
    )
    context.close()
    os.rename(current_video_path, updated_video_path)


def _handle_page_goto(
    page: Page, args: List[Any], kwargs: Dict[str, Any], base_url: str
) -> None:
    url = args.pop()
    if not (url.startswith("http://") or url.startswith("https://")):
        url = base_url + url
    return page._goto(url, *args, **kwargs)  # type: ignore


@pytest.fixture
def login(page):
    page.goto("")
    page.click("text=Log In")
    page.click(":nth-match(:text(\"Log In\"), 2)")
    page.fill("input[name=\"email\"]", "example@example.com")
    page.press("input[name=\"email\"]", "Tab")
    page.fill("input[name=\"password\"]", "openlex1234")
    page.click("input:has-text(\"Log In\")")
