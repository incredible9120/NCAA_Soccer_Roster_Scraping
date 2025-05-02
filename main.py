
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import time
import undetected_chromedriver as uc
from duckduckgo_search import DDGS

def get_college_list(url: str = "https://www.ncsasports.org/mens-soccer/division-1-colleges"):
    """
    This function retrieves a list of colleges from the given URL.
    """
    
    print(f"Scraping {url} to get college list...")

    try:
        options = uc.ChromeOptions()
        options.headless = False  # Set to True if you want it headless

        driver = uc.Chrome(options=options)

        # Go to your target JS-heavy website
        driver.get(url)

        # Wait for the page to fully load (you can adjust the sleep or use WebDriverWait)
        time.sleep(5)

        # Get the full HTML after JS is executed
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        college_names = []
        table_section = soup.find(class_='wp-block-ncsa-college-list')
        
        for row in table_section.find_all('div', class_='row'):            
            college_name = row.find('a')
            if college_name is not None:
                print(college_name)
                college_names.append(college_name.text.strip())
        driver.quit()
        
        with open("colleges.txt", "w") as f:
            for college in college_names:
                f.write(college + "\n")
            
    except Exception as e:
        print(f"Error scraping {url}: {e}")


def get_athletics_site_list():
    """
    This function retrieves a list of athletics from the college names (specified in 'colleges.txt').
    """
    try:
        print("Scraping athletics site list...")
        with open("colleges.txt", "r") as f:
            college_names = [line.strip() for line in f.readlines()]
    except:
        print("Error reading college names from colleges.txt. Please ensure the file exists.")
        return
    
    college_athletics = {}
    for college_name in college_names:
        query = f"{college_name} athletics soccer roster"
        print(f"Searching for {college_name} athletics official site...")
        try:
            with DDGS() as ddgs:
                results = ddgs.text(query)
                for result in results:
                    if 'roster' in result['href'] and 'soccer' in result['href']:
                        college_athletics[college_name] = result['href']
                        print(f"Found soccer roster site for {college_name}: {result['href']}")
                        break
        except Exception as e:
            print(f"Error searching for {college_name} athletics site: {e}")
            continue
        time.sleep(1)
        
    # Save the results to a file
    with open("athletics_sites.txt", "w") as f:
        for college, site in college_athletics.items():
            f.write(f"{college}: {site}\n")

def get_athletics():
    """
    This function retrieves athletics data from the database.
    """
    # Code to retrieve athletics data goes here
    pass

def get_athletics_by_college(college_id):
    """
    This function retrieves athletics data for a specific college from the database.
    """
    # Code to retrieve athletics data by college goes here
    pass

def get_athletics_by_college_and_sport(college_id, sport_id):
    """
    This function retrieves athletics data for a specific college and sport from the database.
    """
    # Code to retrieve athletics data by college and sport goes here
    pass

if __name__ == "__main__":
    # get_college_list()
    get_athletics_site_list()
    # get_athletics()
