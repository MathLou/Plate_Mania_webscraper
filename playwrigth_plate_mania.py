from playwright.sync_api import sync_playwright

def scrape_images(count, url):
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        
        # Wait for the images to load
        page.wait_for_selector("div.row")
        
        images_info = []
        
        # Select the top-level panels for the images
        panels = page.query_selector_all("div.panel.panel-grey")[:count]

        # Loop over each panel to extract the two images and alt text
        for panel in panels:
            # Get the main gallery image (first image)
            main_image_element = panel.query_selector("div.panel-body a img.img-responsive.center-block")
            main_image_url = main_image_element.get_attribute("src") if main_image_element else None
            
            # Get the license plate image (second image) with alt text
            license_image_element = panel.query_selector("div.panel-body div.row img.img-responsive.center-block.margin-bottom-10")
            license_image_url = license_image_element.get_attribute("src") if license_image_element else None
            license_alt = license_image_element.get_attribute("alt") if license_image_element else None
            
            # Collect the extracted data for each panel
            images_info.append({
                "main_image_url": main_image_url,
                "license_image_url": license_image_url,
                "license_plate": license_alt
            })
        
        # Print the extracted information
        for i, info in enumerate(images_info, start=1):
            print(f"Image {i}:")
            print(f"  Main Image URL = {info['main_image_url']}")
            print(f"  License Image URL = {info['license_image_url']}")
            print(f"  License Plate = {info['license_plate']}")
        
        # Close the browser
        browser.close()

adress = "https://platesmania.com/us/gallery.php?region=7503"
# Specify the number of images to scrape
scrape_images(10,adress)
