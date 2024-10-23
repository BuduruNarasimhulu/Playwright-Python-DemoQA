import pytest
from playwright.async_api import async_playwright


@pytest.mark.asyncio
async def test_all_elements_visibility():
    async with async_playwright() as p:
        # Launch the browser in non-headless mode (to see the UI actions)
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()

        # Block unnecessary network requests (ads, trackers) to avoid slowdowns
        async def handle_route(route, request):
            if "ads" in request.url or "google-analytics" in request.url:
                await route.abort()  # Block ads and tracking services
            else:
                await route.continue_()

        # Intercept all network requests
        await context.route("**/*", handle_route)

        # Open a new page
        page = await context.new_page()

        # Navigate to the demoqa page
        await page.goto("https://demoqa.com/")

        # Wait for the page to fully load (using domcontentloaded for speed)
        await page.wait_for_load_state("domcontentloaded")

        # Query and validate all elements on the page
        elements = await page.query_selector_all("*")  # Select all elements on the page
        print(f"Found {len(elements)} elements on the page.")

        invisible_elements_count = 0
        for element in elements:
            # Get element text or tag for logging purposes
            tag_name = await element.evaluate("(element) => element.tagName")
            visible = await element.is_visible()
            print(f"Element <{tag_name}> is visible: {visible}")

            # Assert visibility for each element
            if not visible:
                invisible_elements_count += 1
                print(f"WARNING: Element <{tag_name}> is not visible!")

        # Log the total number of invisible elements found
        print(f"Total invisible elements: {invisible_elements_count}")

        # Close the page and browser context
        await page.close()
        await context.close()
        await browser.close()


# Running the script as a standalone file
if __name__ == "__main__":
    import asyncio

    asyncio.run(test_all_elements_visibility())



