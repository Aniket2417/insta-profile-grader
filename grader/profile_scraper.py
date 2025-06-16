from playwright.sync_api import sync_playwright

def scrape_user_profile(username: str):
    url = f"https://www.instagram.com/{username}/"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_selector("img", timeout=10000)

        bio = page.locator('div.-vDIg span').all_inner_texts()
        posts = page.locator("img").all_attribute_values("alt")[:10]
        img_urls = page.locator("img").all_attribute_values("src")[:3]

        browser.close()

    return {
        "bio": bio[0] if bio else "",
        "captions": posts,
        "images": img_urls
    }