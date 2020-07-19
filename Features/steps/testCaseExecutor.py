from behave import *
import allure
from pymongo import *
import ipdb,re
from controllers.featureParser import featureParser

ftParseObj = featureParser()
ftParseObj.getFListNames()
ftParseObj.parseFeatures()


def getTagData(tag):
    if tag in ftParseObj.tagList:
        return ftParseObj.stepDict[tag]
    else:
        return []


@Given("{device} Execute Steps in tag {tagName}")
def execTagteps(context,device,tagName):
    testCaseTagList = getTagData('@'+tagName)
    print('Running Tag', tagName)
    if testCaseTagList != []:
        for stepitem in testCaseTagList:
            try:
                #print('Running step', stepitem)
                context.execute_steps(stepitem)
                allure.attach('Passed', stepitem, allure.attachment_type.TEXT)
            except Exception as e:
                print('Step failed', stepitem)
                allure.attach(str(e), 'Failed to execute step: ' + stepitem, allure.attachment_type.TEXT)
                allure.attach(context.tsObj[device, 'webdriver'].get_screenshot_as_png(), 'screenshot',allure.attachment_type.PNG)
                raise e
    else:
        print("Tag not found in stepDict")
        allure.attach('## No Steps ##', 'Tag not found in stepDict', allure.attachment_type.TEXT)