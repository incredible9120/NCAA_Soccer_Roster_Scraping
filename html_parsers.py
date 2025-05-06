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
        rows = soup.find_all('div', class_='sidearm-roster-player-container')
        if(rows is not None):
            for row in rows:
                # details = row.find(class_='sidearm-roster-player-details')
                # other = row.find(class_='sidearm-roster-player-other')
                
                year = row.find(class_='sidearm-roster-player-academic-year')
                # print(year.text.strip())
                position = row.find(class_='sidearm-roster-player-custom1')
                if position is None:
                    position = row.find(class_='sidearm-roster-player-hometown')
                    # print(position.text.strip())
                name = row.find(class_='sidearm-roster-player-name').find('a')
                # print(name.text.strip())
                if name:
                    players.append({
                        "School": school_name,
                        "Gender": 'Female',
                        "Name": name.text.strip() if name else None,
                        "Class": year.text.strip() if year else None,
                        "HomeTown": position.text.strip() if position else None
                    })   
        return players
        # ------------- Type 1 ----------------- 
        
        # ------------- Type 2 -----------------
        # class="s-person-card s-person-card--list flex flex-col overflow-hidden rounded-[10px] border s-person-card--theme-light-theme shadow-level-1 border"
        
        # rows = soup.find_all('div', class_='s-person-card--list')
        # if(rows is not None):
        #     for row in rows:
        #         # details = row.find(class_='sidearm-roster-player-details')
        #         # other = row.find(class_='sidearm-roster-player-other')
        #         years = row.find_all(class_='s-person-details__bio-stats-item')
        #         year = years[1]
        #         print(year.text.strip())
        #         # position = row.find(class_='sidearm-roster-player-custom1')
        #         # if position is None:
        #         # s-person-details__bio-stats-item
                
        #         position = row.find(class_='s-person-card__content__person__location-item')
        #         print(position.text.strip())
        #         name = row.find(class_='s-person-details__personal-single-line').find('a')
        #         print(name.text.strip())
        #         if name:
        #             players.append({
        #                 "School": school_name,
        #                 "Gender": 'Male',
        #                 "Name": name.text.strip() if name else None,
        #                 "Class": year.text.strip() if year else None,
        #                 "HomeTown": position.text.strip() if position else None
        #             })   
        # return players
        # ------------- Type 2 -----------------
        
        # ------------- Type 3 -----------------
        # sidearm-roster-table-row
        
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
        
        # ------------- Type 4 -----------------
        # rows = soup.find_all('li', class_='sidearm-roster-player')
        # if(rows is not None):
        #     for row in rows:
        #         # details = row.find(class_='sidearm-roster-player-details')
        #         # other = row.find(class_='sidearm-roster-player-other')
                
        #         year = row.find(class_='sidearm-roster-player-academic-year')
        #         # print(year.text.strip())
        #         # position = row.find(class_='sidearm-roster-player-custom1')
        #         # if position is None:
        #         position = row.find(class_='sidearm-roster-player-hometown')
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
        # ------------- Type 4 ----------------- 
        
        # ------------- Type 5 -----------------
        # table_section = soup.find('tbody', class_='s-table-body')
        # rows = table_section.find_all('tr', class_='s-table-body__row')
        # if(rows is not None):
        #     for row in rows:
        #         print(row)
        #         # details = row.find(class_='sidearm-roster-player-details')
        #         # other = row.find(class_='sidearm-roster-player-other')
        #         items = row.find_all('td', class_='s-table-body_cell')
                
        #         year = items[5]
        #         position = items[6].find('span')
        #         name = items[1].find('span')
                
        #         print(position.text.strip())
        #         print(year.text.strip())
        #         print(name.text.strip())
        #         if name:
        #             players.append({
        #                 "School": school_name,
        #                 "Gender": 'Male',
        #                 "Name": name.text.strip() if name else None,
        #                 "Class": year.text.strip() if year else None,
        #                 "HomeTown": position.text.strip() if position else None
        #             })   
        # return players
        # ------------- Type 5 ----------------- 
        
        # ------------- Type 6 -----------------
        # class="s-person-card s-person-card--list flex flex-col overflow-hidden rounded-[10px] border s-person-card--theme-light-theme shadow-level-1 border"
        
        # rows = soup.find_all('div', class_='s-person-card--theme-light-theme')
        # if(rows is not None):
        #     for row in rows:
        #         # details = row.find(class_='sidearm-roster-player-details')
        #         # other = row.find(class_='sidearm-roster-player-other')
        #         years = row.find_all('span', class_='s-person-details__bio-stats-item')
        #         year = years[1]
        #         print(year.text.strip())
        #         # position = row.find(class_='sidearm-roster-player-custom1')
        #         # if position is None:
        #         # s-person-details__bio-stats-item
                
        #         position = row.find(class_='s-person-card__content__person__location-item')
        #             # print(position.text.strip())
        #         name = row.find(class_='s-person-details__personal-single-line').find('h3')
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
        
        # ------------- Type 6 ----------------- 
        
        # ------------- Type 7 -----------------
        
        # rows = soup.find_all('div', class_='s-person-card--list')
        # if(rows is not None):
        #     for row in rows:
        #         # details = row.find(class_='sidearm-roster-player-details')
        #         # other = row.find(class_='sidearm-roster-player-other')
        #         years = row.find_all(class_='s-person-details__bio-stats-item')
        #         year = years[1]
        #         print(year.text.strip())
        #         # position = row.find(class_='sidearm-roster-player-custom1')
        #         # if position is None:
        #         # s-person-details__bio-stats-item
                
        #         position = row.find(class_='s-person-card__content__person__location-item')
        #         print(position.text.strip())
        #         name = row.find(class_='s-person-details__personal-single-line').find('a')
        #         print(name.text.strip())
        #         if name:
        #             players.append({
        #                 "School": school_name,
        #                 "Gender": 'Male',
        #                 "Name": name.text.strip() if name else None,
        #                 "Class": year.text.strip() if year else None,
        #                 "HomeTown": position.text.strip() if position else None
        
        # ------------- Type 7 ----------------- 
        
        # ------------- Type 8 -----------------
        
        # rows = soup.find('div', class_='roster__content-box-table').find('tr')
        # if(rows is not None):
        #     for row in rows:
        #         items = row.find_all('td', class_='roster_table__cell')
        #         # details = row.find(class_='sidearm-roster-player-details')
        #         # other = row.find(class_='sidearm-roster-player-other')
        #         year = items[3]
        #         print(year.text.strip())
        #         # position = row.find(class_='sidearm-roster-player-custom1')
        #         # if position is None:
        #         # s-person-details__bio-stats-item
                
        #         position = items[4]
        #         print(position.text.strip())
        #         name = row.find('th', class_='roster_table_cell')
        #         print(name.text.strip())
        #         if name:
        #             players.append({
        #                 "School": school_name,
        #                 "Gender": 'Male',
        #                 "Name": name.text.strip() if name else None,
        #                 "Class": year.text.strip() if year else None,
        #                 "HomeTown": position.text.strip() if position else None
        #         })   
        # return players
        # ------------- Type 8 ----------------- 
        
        # ------------- Type 9 -----------------
        
        # https://www.cneagles.com/sports/m-soccer/2024-25/roster?view=1
        # https://www.stacathletics.com/sports/msoc/2024-25/roster
        
        # rows = soup.find('tbody').find_all('tr')
        # if(rows is not None):
        #     for row in rows:
        #         items = row.find_all('td')
        #         # details = row.find(class_='sidearm-roster-player-details')
        #         # other = row.find(class_='sidearm-roster-player-other')
        #         year = items[3]
        #         print(year.text.strip())
        #         # position = row.find(class_='sidearm-roster-player-custom1')
        #         # if position is None:
        #         # s-person-details__bio-stats-item
                
        #         position = items[4]
        #         print(position.text.strip())
        #         name = row.find('th').find('a')
        #         print(name.text.strip())
        #         if name:
        #             players.append({
        #                 "School": school_name,
        #                 "Gender": 'Male',
        #                 "Name": name.text.strip() if name else None,
        #                 "Class": year.text.strip() if year else None,
        #                 "HomeTown": position.text.strip() if position else None
        #         })   
        # return players
        # ------------- Type 9 ----------------- 
        
        # ------------- Type 10 -----------------
        # rows = soup.find_all('li', class_='sidearm-list-card-item')
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
        #         name = row.find(class_='sidearm-roster-player-name-container').find('a')
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
        # ------------- Type 10 ----------------- 
 
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return []
