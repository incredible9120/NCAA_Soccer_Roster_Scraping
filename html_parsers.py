import requests
from bs4 import BeautifulSoup
import time
import undetected_chromedriver as uc

def scrape_roster(school_name, url):
    try:
        options = uc.ChromeOptions()
        options.headless = True  # Set to True if you want it headless

        driver = uc.Chrome(options=options)

        # Go to your target JS-heavy website
        driver.get(url)

        # Wait for the page to fully load (you can adjust the sleep or use WebDriverWait)
        time.sleep(5)

        print(url)
        # Get the full HTML after JS is executed
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        players = []
        
        # class="s-person-card s-person-card--list flex flex-col overflow-hidden rounded-[10px] border s-person-card--theme-light-theme shadow-level-1 border"
        
        # ------------- Type 1 -----------------
        # rows = soup.find_all('div', class_='sidearm-roster-player-container')
        # if(rows is not None):
        #     for row in rows:
        #         # details = row.find(class_='sidearm-roster-player-details')
        #         # other = row.find(class_='sidearm-roster-player-other')
                
        #         year = row.find(class_='sidearm-roster-player-academic-year')
        #         # print(year.text.strip())
        #         position = row.find(class_='sidearm-roster-player-custom1')
        #         if position is None:
        #             position = row.find(class_='sidearm-roster-player-hometown')
        #             # print(position.text.strip())
        #         name = row.find(class_='sidearm-roster-player-name').find('h3').find('a')
        #         # print(name.text.strip())
        #         if name:
        #             players.append({
        #                 "School": school_name,
        #                 "Gender": 'Male',
        #                 "Name": name.text.strip() if name else None,
        #                 "Class": year.text.strip() if year else None,
        #                 "HomeTown": position.text.strip() if position else None
        #             })   
        # return players
        # ------------- Type 1 ----------------- 
        
        # ------------- Type 2 -----------------
        # class="s-person-card s-person-card--list flex flex-col overflow-hidden rounded-[10px] border s-person-card--theme-light-theme shadow-level-1 border"
        
        rows = soup.find_all('div', class_='s-person-card--list')
        if(rows is not None):
            for row in rows:
                # details = row.find(class_='sidearm-roster-player-details')
                # other = row.find(class_='sidearm-roster-player-other')
                years = row.find_all(class_='s-person-details__bio-stats-item')
                year = years[1]
                print(year.text.strip())
                # position = row.find(class_='sidearm-roster-player-custom1')
                # if position is None:
                # s-person-details__bio-stats-item
                
                position = row.find(class_='s-person-card__content__person__location-item')
                    # print(position.text.strip())
                name = row.find(class_='s-person-details__personal-single-line').find('a')
                # print(name.text.strip())
                if name:
                    players.append({
                        "School": school_name,
                        "Gender": 'Male',
                        "Name": name.text.strip() if name else None,
                        "Class": year.text.strip() if year else None,
                        "HomeTown": position.text.strip() if position else None
                    })   
        return players
        # ------------- Type 2 -----------------
        
        # ------------- Type 3 -----------------
        # rows = soup.find_all('li', class_='sidearm-roster-list-item')
        # if(rows is not None):
        #     for row in rows:
        #         # details = row.find(class_='sidearm-roster-player-details')
        #         # other = row.find(class_='sidearm-roster-player-other')
                
        #         year = row.find(class_='sidearm-roster-list-item-year')
        #         # print(year.text.strip())
        #         position = row.find(class_='sidearm-roster-player-custom1')
        #         if position is None:
        #             position = row.find(class_='sidearm-roster-list-item-hometown')
        #             # print(position.text.strip())
        #         name = row.find(class_='sidearm-roster-player-name').find('a')
        #         # print(name.text.strip())
        #         if name:
        #             players.append({
        #                 "School": school_name,
        #                 "Gender": 'Male',
        #                 "Name": name.text.strip() if name else None,
        #                 "Class": year.text.strip() if year else None,
        #                 "HomeTown": position.text.strip() if position else None
        #             })   
        # return players
        
        # ------------- Type 3 -----------------
        
        
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return []
