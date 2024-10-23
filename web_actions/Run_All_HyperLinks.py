import pytest
from playwright.async_api import async_playwright

@pytest.mark.asyncio
async def test_scan_demo_qa():
    async with async_playwright() as p:
        # Launch the browser
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()

        # Route handler to block unnecessary resources (ads, tracking scripts)
        async def handle_route(route, request):
            if "ads" in request.url or "google-analytics" in request.url:
                await route.abort()  # Abort requests to ads or tracking services
            else:
                await route.continue_()

        # Apply the route to intercept all network requests
        await context.route("**/*", handle_route)

        page = await context.new_page()

        # Navigate to the DemoQA page
        await page.goto("https://demoqa.com/")

        # Wait until DOM content is loaded (faster and less likely to cause timeout)
        await page.wait_for_load_state("domcontentloaded")

        # Collect and validate all anchor elements (links) for visibility
        links = await page.query_selector_all("a")
        print(f"Found {len(links)} links on the page.")
        for link in links:
            href = await link.get_attribute("href")
            visible = await link.is_visible()

            if href is None:
                # Log link details for debugging if no href attribute is found
                link_text = await link.inner_text()
                link_html = await link.inner_html()
                print(f"Link without href found! Text: {link_text}, HTML: {link_html}")
                continue  # Skip this link and move on

            # Print and assert visibility for links with href
            print(f"Link: {href}, Visible: {visible}")
            assert visible, f"Link {href} is not visible!"

        # Perform interaction: click "Elements" section
        await page.click("text=Elements")
        await page.wait_for_load_state("domcontentloaded")
        assert await page.is_visible("text=Text Box"), "Failed to navigate to the 'Elements' section!"

        # Close the page and browser context
        await page.close()
        await context.close()
        await browser.close()


# Running as a standalone script
if __name__ == "__main__":
    import asyncio

    asyncio.run(test_scan_demo_qa())




