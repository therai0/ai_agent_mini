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
import os 

class ScarpBalmikiPage:
    def __init__(self):
        print("Initiating of scarping")

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
                    "page":"home_page",
                    "page_content":
                        {
                            "mission_vision":mission_vision,
                            "academic_program":academic_programs,
                            "student_life":student_life
                            # "description":description
                        }
                })
                print("Home page data scarped")
                return data 
        except Exception as e:
            print(e)


    def aboutus_page(self,url):
        try:
            data = []
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True) 
                page = browser.new_page()
                page.goto(url)

                last_height = 0
                while True:
                    page.mouse.wheel(0, 6000)          # scroll down
                    page.wait_for_timeout(1000)        # let content load
                    height = page.evaluate("document.body.scrollHeight")
                    if height == last_height:          # nothing new loaded
                        break
                    last_height = height

                # about us 
                aboutus_locator = page.locator(".about-content")
                our_story = aboutus_locator.nth(0).inner_text()

                recognization = page.locator("#achievements").inner_text()

                data.append({
                    "page":"aboutus_page",
                    "page_content":{
                        "our_story":our_story,
                        "recognization":recognization
                    }
                })
                print("About us page data scarped")
                return data
        except Exception as e:
            print(e)

    def course(self,url:str,page_name):
        try:
            data = []
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()
                page.goto(url)
                last_height = 0
                while True:
                    page.mouse.wheel(0, 6000)          # scroll down
                    page.wait_for_timeout(1000)        # let content load
                    height = page.evaluate("document.body.scrollHeight")
                    if height == last_height:          # nothing new loaded
                        break
                    last_height = height

                # course section
                program_overview = page.locator(".course-section").inner_text()
                if  url.endswith("courses/bhm_course_page.html"):
                    program_features_career = page.locator("#highlights-careers-section").inner_text()
                else:
                    program_features_career = page.locator("#program-features-section").inner_text()
                admission_requirement = page.locator("#admission-requirements-section").inner_text()

                

                data.append({
                    "page":page_name,
                    "page_content":{
                        "program_overview":program_overview,
                        "program_features_career":program_features_career,
                        "admission_requirement":admission_requirement
                    }
                })
                print("course data scarped")
                return data 
        except Exception as e:
            print(e)

    def contact(self,url):
        try:
            data = []
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()
                page.goto(url)

                contact = page.locator(".info-content")

                content = {}
                for i in range(contact.count()):
                    head = contact.nth(i).locator("h4").inner_text()
                    body = contact.nth(i).locator("p").inner_text()
                    content[head] = body

                data.append({
                    "page":"contact us",
                    "page_content":content
                })
                print("Contact page data scarped")
                return data

        except Exception as e:
            print(e)

    def capmus_facilities(self,url):
        try:
            data = []
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()
                page.goto(url)

                tab_locator = page.locator(".tab-pane")
                nav_locator = page.locator(".nav-item")
                content = {}
                for i in range(nav_locator.count()):
                    content[nav_locator.nth(i).inner_text()] = tab_locator.nth(i).inner_text()

                data.append({
                    "page":"Campus facilities",
                    "page_content": content
                })
                print("Campus data. scarped")
                return data 
        except Exception as e:
            print(e)
        
        

def save_json(data:list,path:str):
    try:
        dir_path = os.path.dirname(path)
        os.makedirs(dir_path,exist_ok=True)

        with open(path,'w',encoding="utf-8") as f:
            json.dump(data,f,indent=3)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    scarp = ScarpBalmikiPage()
    homepage_data = scarp.home_page("https://lincolnbalmiki.edu.np/")
    aboutuspage_data = scarp.aboutus_page("https://lincolnbalmiki.edu.np/about.html")
    bba_data = scarp.course("https://lincolnbalmiki.edu.np/courses/bba_course_page.html","BBA page")
    bit_data = scarp.course("https://lincolnbalmiki.edu.np/courses/bit_course_page.html","BIT page")
    bhm_data = scarp.course("https://lincolnbalmiki.edu.np/courses/bhm_course_page.html","BHM page")
    mba_data = scarp.course("https://lincolnbalmiki.edu.np/courses/mba_course_page.html","MBA page")
    contact_data = scarp.contact("https://lincolnbalmiki.edu.np/contact.html")
    campus_facilities_data = scarp.capmus_facilities("https://lincolnbalmiki.edu.np/campus-facilities.html")

    file_path = "./day_7/json_data/data.json"
    data  = [*homepage_data,*aboutuspage_data,*bba_data,*bit_data,*bhm_data,*mba_data,*contact_data,*campus_facilities_data]
    save_json(data,file_path)

    


