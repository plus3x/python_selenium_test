# -*- coding: utf-8 -*-

import pytest

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def browser():
  options = Options()
  options.headless = True

  # Initialize ChromeDriver
  driver = Firefox(options=options)

  # Wait implicitly for elements to be ready before attempting interactions
  driver.implicitly_wait(10)

  # Return the driver object at the end of setup
  yield driver

  # For cleanup, quit the driver
  driver.quit()
