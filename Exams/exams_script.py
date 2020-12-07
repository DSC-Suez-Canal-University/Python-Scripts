from selenium import webdriver
from bs4 import BeautifulSoup
import time
import json


def exams():
    options = webdriver.ChromeOptions()
    options.add_argument('-incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    driver.get("https://forms.gle/vcDioG3sWUziKDPG8")

    time.sleep(2)

    content = driver.page_source

    answers = {}
    soup = BeautifulSoup(content, features="html.parser")

    def pass_question(question):
        with open('exams.json') as f:
            data = json.load(f)
            for keys in data:
                if keys.__contains__(question):
                    return data[keys]

    radios = driver.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
    counter = 0
    for a in soup.findAll('div', attrs={
        'class': 'freebirdFormviewerViewNumberedItemContainer'}):

        question = a.find('div', attrs={'class': 'freebirdFormviewerComponentsQuestionBaseTitleDescContainer'})
        الإجابة = pass_question(question=question.text)

        for answer in a.findAll('span', attrs={'class',
                                               'docssharedWizToggleLabeledLabelText exportLabel freebirdFormviewerComponentsQuestionRadioLabel'}):
            answers[counter] = answer.text

            if answer.text == الإجابة:
                radios[counter].click()
            counter += 1

    driver.find_element_by_xpath("//*[contains(text(), 'إرسال')]").click()
    driver.close()
