# Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as soup
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape_all():
    #set up splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    news_title, news_p = mars_news(browser)
    #adding hemispheres
    img_urls_titles=mars_hemis(browser)

    # Run all scraping functions and store results in dictionary
    data = {
      "news_title": news_title,
      "news_paragraph": news_p,
      "featured_image": featured_image(browser),
      "facts": mars_facts(),
      "last_modified": dt.datetime.now(),
      "hemispheres":img_urls_titles}

    # Stop webdriver and return data
    browser.quit()
    return data

def mars_news(browser):
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)
    # Optional delay for loading the page
    #One is that we're searching for elements with a specific combination of tag (div) and attribute (list_text).
    #As an example, ul.item_list would be found in HTML as <ul class="item_list">

    #Optional delay for leading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    #The . is used for selecting classes, such as list_text, so the code 'div.list_text' pinpoints the <div /> tag with the class of list_text. 
    #CSS works from right to left, such as returning the last item on the list instead of the first
    # Convert the browser html to a soup object
    html = browser.html
    news_soup = soup(html, 'html.parser')
    #slide_elem as the variable to look for the <div /> tag and its descendent, this is our parent element.
    
    try: 
        slide_elem = news_soup.select_one('div.list_text')

        slide_elem.find('div', class_='content_title')

        # Use the parent element to find the first a tag and save it as `news_title`
        news_title=slide_elem.find('div', class_='content_title').get_text()
    

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    
    except AttributeError:
        return None, None 

    return  news_title, news_p


# ## JPL Space Images Featured Image

def featured_image(browser):
# Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='thumbimg').get('src')
    
    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    
    return img_url

# ##Mars Facts

def mars_facts():
#By specifying an index of 0, we're telling Pandas to pull only the first table it encounters, or the first item in the list.

    try:
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    except BaseException:
        return None
    ## Assign columns and set index of dataframe    
    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)

    #convert to html
    return df.to_html(classes='table table-striped')


def mars_hemis(browser):

    url = 'https://marshemispheres.com/'
    browser.visit(url)

    hemisphere_image_urls = []

    html = browser.html
    class_items_soup = soup(html, 'html.parser')

    class_items=len(class_items_soup.find_all('div', class_='item'))

    for hemis in range(class_items):
        browser.links.find_by_partial_text('Hemisphere')[hemis].click()
        
        html = browser.html
        hemis_soup = soup(html, 'html.parser')
        
        title=hemis_soup.find('h2', class_='title').text
        img_url=hemis_soup.find('li').a.get('href')
        
        hemispheres={}
        hemispheres['img_url'] = f'{url}{img_url}'
        hemispheres['title'] = title
        hemisphere_image_urls.append(hemispheres)
        
        browser.back()
        
    return hemisphere_image_urls

if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())




