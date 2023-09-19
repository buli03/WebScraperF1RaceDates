from selenium import webdriver 
from bs4 import BeautifulSoup

"""
    'div' class = "col-12 col-sm-6 col-lg-4 col-xl-3"                                                    ==> where specific events are stored
    'legend' class ="card-title f1-uppercase f1-color--warmRed"                                          ==> name of event 
    'div' class ="event-info" read 'span' class ="start-date" and class ="end-date"                      ==> days of event
    'span' class="month-wrapper f1-wide--xxs"                                                            ==> month of event (3 first letters)
    in 'div' class="event-description" > 'div' class="event-place" and 'div' class="event-title f1--xxs" ==> place and desc of event

    How i want to display the data example: 
    23-25 Feb: Sakhir FORMULA 1 ARAMCO PRE-SEASON TESTING 2023
"""

#functions
def getText(e):
    if e is None:
        return ""
    return e.text

#variables
driver = webdriver.Chrome()
driver.get("https://www.formula1.com/en/racing/2023.html")
pageSource = driver.page_source
soup = BeautifulSoup(pageSource, 'html.parser')
driver.quit()

allPastEventsContainer = soup.find('div', 'row completed-events') 
allPastEvents = allPastEventsContainer.find_all('div','col-12 col-sm-6 col-lg-4 col-xl-3')

heroEventContainer = soup.find('div','hero-event')

allNextEventsContainer = soup.find('div', 'row event-below-hero')
allNextEvents = allNextEventsContainer.find_all('div','col-12 col-sm-6 col-lg-4 col-xl-3')

#program
print("\n-------------------------------{Past Events}-------------------------------")
for event in allPastEvents:
    print(
        getText(event.find('span','start-date')),
        "-",
        getText(event.find('span','end-date')),
        getText(event.find('span','month-wrapper f1-wide--xxs f1-uppercase')), getText(event.find('span','month-wrapper f1-wide--xxs')),
        ": ",
        getText(event.find('div','event-place')),
        getText(event.find('div', 'event-title f1--xxs'))
    )

print("\n--------------------------------{Hero Event}-------------------------------")
print(
    getText(heroEventContainer.find('span','start-date')),
    "-",
    getText(heroEventContainer.find('span','end-date')),
    getText(heroEventContainer.find('span','month-wrapper f1-wide--xxs')),
    ": ",
    getText(heroEventContainer.find('div','event-place')),
    getText(heroEventContainer.find('div', 'event-title f1--xxs'))
)
heroEventLinkContainer = heroEventContainer.find('a', 'event-item-wrapper event-item-link idle')
print(f"Link to the upcoming event: https://formula1.com{heroEventLinkContainer.get('href')}")

print("\n--------------------------------{Next Events}------------------------------")
for event in allNextEvents:
    print(
        getText(event.find('span','start-date')),
        "-",
        getText(event.find('span','end-date')),
        getText(event.find('span','month-wrapper f1-wide--xxs f1-uppercase')), getText(event.find('span','month-wrapper f1-wide--xxs')),
        ": ",
        getText(event.find('div','event-place')),
        getText(event.find('div', 'event-title f1--xxs'))
    )