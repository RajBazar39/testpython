from behave import *
from controllers.Config import *
from controllers.objectIDs import *
from selenium.webdriver.common.keys import Keys
import allure
from appium.webdriver.common.touch_action import TouchAction
import ipdb,datetime
import random, string
import subprocess

@Given("{configVal} is pushed successfully on server {serverVal}")
def pushServerFile(context,configVal,serverVal):
    cmd = 'java -cp controllers/configFiles/cms_custom_client-5123.jar:controllers/configFiles/lib/* com.matrixx.cms.client.UploadFileClient "http://'+serverVal+'/rsgateway/data" controllers/configFiles/'+configVal+'/appconfigurationmobile.json'
    chkVal = subprocess.check_output(cmd,shell=True)
    allure.attach(chkVal, 'Output Returned: ', allure.attachment_type.TEXT)
    assert not context.failed


@then("{device} Verify that {chkItem} is visible")
def verifyElement(context,device,chkItem):
    if device == 'Android':
        elementVal = None
        if chkItem == 'BottomMenu':
            elementVal = context.tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.bottomMenuID)
            allure.attach(context.tsObj[device, 'webdriver'].get_screenshot_as_png(), chkItem + ' ScreenShot',allure.attachment_type.PNG)
        elif chkItem == 'BottomMenuMyPage':
            elementVal = context.tsObj[device, 'webdriver'].find_element_by_xpath(AndroidLoginObj.bottomMenuMyPageXpath)
        elif chkItem == 'BottomMenuFeaturesTour':
            elementVal = context.tsObj[device, 'webdriver'].find_element_by_xpath(AndroidLoginObj.bottomMenuFeatureTourXpath)
        elif chkItem == 'BottomMenuMarketplace':
            elementVal = context.tsObj[device, 'webdriver'].find_element_by_xpath(AndroidLoginObj.bottomMenuMarketplaceXpath)
        elif chkItem == 'BottomMenuAccount':
            elementVal = context.tsObj[device, 'webdriver'].find_element_by_xpath(AndroidLoginObj.bottomMenuAccountXpath)
        elif chkItem == 'SideMenuList':
            elementVal = context.tsObj[device, 'webdriver'].find_element_by_xpath(AndroidLoginObj.sideMenuListXpath)
            allure.attach(context.tsObj[device, 'webdriver'].get_screenshot_as_png(), chkItem + ' ScreenShot',allure.attachment_type.PNG)
        elif chkItem == 'GetHelpButton':
            elementVal = context.tsObj[device, 'webdriver'].find_element_by_xpath(AndroidLoginObj.getHelpXpath)
        elif chkItem == 'MarketplaceButton':
            elementVal = context.tsObj[device, 'webdriver'].find_element_by_xpath(AndroidLoginObj.marketPlaceXpath)
        elif chkItem == 'FeaturesTourButton':
            elementVal = context.tsObj[device, 'webdriver'].find_element_by_xpath(AndroidLoginObj.featuresTourXpath)
        elif chkItem == 'ActionCentreButton':
            elementVal = context.tsObj[device, 'webdriver'].find_element_by_xpath(AndroidLoginObj.actionCentreXpath)
        elif chkItem == 'LogoutButton':
            elementVal = context.tsObj[device, 'webdriver'].find_element_by_xpath(AndroidLoginObj.logoutButtonXpath)
        elif chkItem == 'AboutButton':
            elementVal = context.tsObj[device, 'webdriver'].find_element_by_xpath(AndroidLoginObj.aboutButtonXpath)
        elif chkItem == 'DebugOptionsButton':
            elementVal = context.tsObj[device, 'webdriver'].find_element_by_xpath(AndroidLoginObj.debugOptsButtonXpath)
        if elementVal is None:
            context.failed = True
    else:
        pass
    if (context.failed):
        allure.attach(context.tsObj[device, 'webdriver'].get_screenshot_as_png(), 'screenshot', allure.attachment_type.PNG)
    assert not context.failed

@then("{device} Verify that {chkItem} is present at position {val}")
def verifyPosition(context,device,chkItem,val):
    if device == 'Android':
        if chkItem == 'BottomMenuMyPage':
            elementVal = context.tsObj[device, 'webdriver'].find_element_by_xpath(AndroidLoginObj.p_bottomMenuMyPageXpath+' and @index='+val+']')
        elif chkItem == 'BottomMenuFeaturesTour':
            elementVal = context.tsObj[device, 'webdriver'].find_element_by_xpath(AndroidLoginObj.p_bottomMenuFeatureTourXpath+' and @index='+val+']')
        elif chkItem == 'BottomMenuMarketplace':
            elementVal = context.tsObj[device, 'webdriver'].find_element_by_xpath(AndroidLoginObj.p_bottomMenuMarketplaceXpath + ' and @index=' + val + ']')
        elif chkItem == 'BottomMenuAccount':
            elementVal = context.tsObj[device, 'webdriver'].find_element_by_xpath(AndroidLoginObj.p_bottomMenuAccountXpath+' and @index='+val+']')
        elif chkItem == 'GetHelpButton':
            if context.tsObj[device, 'webdriver'].find_elements_by_xpath(AndroidLoginObj.sideMenuItemList)[int(val)].text != "Get Help":
                context.failed = True
        elif chkItem == 'MarketplaceButton':
            if context.tsObj[device, 'webdriver'].find_elements_by_xpath(AndroidLoginObj.sideMenuItemList)[int(val)].text != "Marketplace":
                context.failed = True
        elif chkItem == 'FeaturesTourButton':
            if context.tsObj[device, 'webdriver'].find_elements_by_xpath(AndroidLoginObj.sideMenuItemList)[int(val)].text != "Features Tour":
                context.failed = True
        elif chkItem == 'ActionCentreButton':
            if context.tsObj[device, 'webdriver'].find_elements_by_xpath(AndroidLoginObj.sideMenuItemList)[int(val)].text != "Action Centre":
                context.failed = True
        elif chkItem == 'LogoutButton':
            if context.tsObj[device, 'webdriver'].find_elements_by_xpath(AndroidLoginObj.sideMenuItemList)[int(val)].text != "Logout":
                context.failed = True
        elif chkItem == 'AboutButton':
            if context.tsObj[device, 'webdriver'].find_elements_by_xpath(AndroidLoginObj.sideMenuItemList)[int(val)].text != "About":
                context.failed = True
        elif chkItem == 'DebugOptionsButton':
            if context.tsObj[device, 'webdriver'].find_elements_by_xpath(AndroidLoginObj.sideMenuItemList)[int(val)].text != "Debug Options":
                context.failed = True
    else:
        pass
    if (context.failed):
        allure.attach(context.tsObj[device, 'webdriver'].get_screenshot_as_png(), 'screenshot', allure.attachment_type.PNG)
    assert not context.failed