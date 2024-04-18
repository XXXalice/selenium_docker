from selenium import webdriver


def _build_options(headless=True):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")

    return options


print("up scraper.")
browser = webdriver.Remote(
    command_executor="http://selenium:4444/wd/hub",
    options=_build_options()
)
browser.get("https://www.google.com/")
print(browser.page_source)
