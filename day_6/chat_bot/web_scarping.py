""" 
Read the data from the Balmiki Lincoln Website 
store the data into json format

Required information:
--> About college
--> College programs
--> Admission and scholarship
--> Contact information

Data should be in json format
 data = {
 page:str,
 content:[list]
 }
"""
from playwright.sync_api import sync_playwright
import json 

class ScarpBalmikiPage:
    def __init__(self):
        self.data = []

    def home_page(self,url):
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()
                page.goto(url)
                data = []
                card_selector = page.locator(".value-card")

                # mission-vision-row data
                mission_vision = []
                for i in range(card_selector.count()):
                    card = card_selector.nth(i)
                    mission_vision.append({card.locator("h3").inner_text():card.locator("p").inner_text()})

                # academic programs cards
                academic_programs = []
                program_selector = page.locator(".program-content")
                for i in range(program_selector.count()):
                    card = program_selector.nth(i)
                    academic_programs.append({
                        "program_title":card.locator("h3").inner_text(),
                        "duration":card.locator("span").nth(0).inner_text(),
                        "credit_hours":card.locator("span").nth(1).inner_text(),
                        "description":card.locator("p").inner_text()
                    })

                # student life
                student_life = []
                std_lf_selector = page.locator(".student-activity-item")
                for i in range(std_lf_selector.count()):
                    card = std_lf_selector.nth(i)
                    student_life.append({
                        "title":card.locator("h4").inner_text(),
                        "description":card.locator("p").inner_text()
                    })

                # description = card.locator(".stats-description").inner_text()

                data.append({
                    "page_title":"home_page",
                    "page_content":
                        {
                            "mission_vision":mission_vision,
                            "academic_program":academic_programs,
                            "student_life":student_life
                            # "description":description
                        }
                })
                return data 
        except Exception as e:
            print(e)


    def aboutus_page(self,url):
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True) 
                page = browser.new_page()
                page.goto(url)

                # about us 
                aboutus_locator = page.locator(".about-content")
                our_story = aboutus_locator.nth(0).inner_text()
                headline = aboutus_locator.nth(1).inner_text()
                paragraph = aboutus_locator.nth(2).inner_text()
                print(our_story)
                print(headline)
                print(paragraph)

                timeline_content = page.locator("timeline-content")
                print(timeline_content.count())

        except Exception as e:
            print(e)


        
scarp = ScarpBalmikiPage()
# h1 = scarp.home_page("https://lincolnbalmiki.edu.np/")
scarp.aboutus_page("https://lincolnbalmiki.edu.np/about.html")