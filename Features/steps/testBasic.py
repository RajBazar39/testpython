from behave import *
from controllers.Config import *
from controllers.objectIDs import *
from selenium.webdriver.common.keys import Keys
import allure
from appium.webdriver.common.touch_action import TouchAction
import ipdb,datetime
import random, string

global tsObj
tsObj = {}

@Given("{device} Install and launch application")
def installaunchApp(context,device):
    tsObj[device,'obj'] = configController()
    tsObj[device,'webdriver'] = tsObj[device,'obj'].webDriverInit(device)
    context.tsObj = tsObj
    if (context.failed):
        allure.attach(tsObj[device, 'webdriver'].get_screenshot_as_png(), 'screenshot', allure.attachment_type.PNG)
    assert not context.failed

@Given("{device} Launch application")
def launchApp(context,device):
    tsObj[device,'obj'] = configController()
    tsObj[device,'webdriver'] = tsObj[device,'obj'].webDriverInit(device,delPrevApp=0)
    context.tsObj = tsObj
    assert not context.failed

@Given("{device} Test load time of app")
def launchApp(context,device):
    tsObj[device,'obj'] = configController()
    prevTime=datetime.datetime.now()
    tsObj[device,'webdriver'] = tsObj[device,'obj'].webDriverInit(device,delPrevApp=0)
    if device == 'Android':
        el = tsObj[device, 'webdriver'].find_element_by_xpath(AndroidLoginObj.moreOpts)
        if el is not None:
            currTime=datetime.datetime.now()
            diffTime=str(currTime-prevTime-datetime.timedelta(seconds=8))
            allure.attach(diffTime,'Time taken to launch:',allure.attachment_type.TEXT)
    else:
        el = tsObj[device, 'webdriver'].find_element_by_xpath(IOSLoginObj.skipBtn)
        if el is not None:
            currTime = datetime.datetime.now()
            diffTime = str(currTime - prevTime - datetime.timedelta(seconds=5))
            allure.attach(diffTime, 'Time taken to launch:', allure.attachment_type.TEXT)
    assert not context.failed
    

def sendKeysIOSeyboard(device):
    try:
        tsObj[device, 'webdriver'].find_element_by_xpath("//XCUIElementTypeTextField").send_keys(Keys.RETURN)
    except:
        pass

@then("{device} Tap on {val} button text")
def tapButtonText(context,device,val):
    if device == 'Android':
        tsObj[device, 'webdriver'].find_element_by_xpath("//android.widget.Button[@text=\""+val+"\"]").click()
    else:
        tsObj[device, 'webdriver'].find_element_by_xpath("//XCUIElementTypeButton[@name=\""+val+"\"]").click()
    if (context.failed):
        allure.attach(tsObj[device, 'webdriver'].get_screenshot_as_png(), 'screenshot', allure.attachment_type.PNG)
    assert not context.failed

@then("{device} Tap on {val} RadioButton text")
def tapRadioButtonText(context,device,val):
    if device == 'Android':
        tsObj[device, 'webdriver'].find_element_by_xpath("//android.widget.RadioButton[@text=\""+val+"\"]").click()
    else:
        pass
    if (context.failed):
        allure.attach(tsObj[device, 'webdriver'].get_screenshot_as_png(), 'screenshot', allure.attachment_type.PNG)
    assert not context.failed

@then("{device} Tap on {val} text")
def tapText(context,device,val):
    if device == 'Android':
        tsObj[device, 'webdriver'].find_element_by_xpath("//android.widget.TextView[@text=\""+val+"\"]").click()
    else:
        tsObj[device, 'webdriver'].find_element_by_xpath("//XCUIElementTypeStaticText[@label=\"" + val + "\"]").click()
    if (context.failed):
        allure.attach(tsObj[device, 'webdriver'].get_screenshot_as_png(), 'screenshot', allure.attachment_type.PNG)
    assert not context.failed

@then("{device} Wait for {num} seconds")
def waitProc(context,device,num):
    if device == 'Android':
        time.sleep(int(num))
    if (context.failed):
        allure.attach(tsObj[device, 'webdriver'].get_screenshot_as_png(), 'screenshot', allure.attachment_type.PNG)
    assert not context.failed

@then("{device} Handle Camera Permission Popups")
def checkPopups(context,device):
    try:
        if device == 'Android':
            if tsObj[device, 'webdriver'].find_element_by_xpath('//android.widget.Button[@text=\"ALLOW\"]') is not None:
                tsObj[device, 'webdriver'].find_element_by_xpath('//android.widget.Button[@text=\"ALLOW\"]').click()
        if (context.failed):
            allure.attach(tsObj[device, 'webdriver'].get_screenshot_as_png(), 'screenshot', allure.attachment_type.PNG)
    except:
        print('No Popups found')


@then("{device} Set id {txt} as {val}")
def editTextVal(context,device,txt,val):
    if device == 'Android':
        if txt == 'emailText':
            if val == 'randomEmail':
                emailVal = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
                tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.editEmailTxtId).send_keys(emailVal+'@gmail.com')
            else:
                tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.editEmailTxtId).send_keys(val)
        elif txt == 'emailPass':
            if str(val).__contains__('userPwd'):
                uVal=tsObj[device, 'obj'].yamlDict[val]
                tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.editPassTxtId).send_keys(uVal)
                tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.editConfTxtId).send_keys(uVal)
            else:
                tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.editPassTxtId).send_keys(val)
                tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.editConfTxtId).send_keys(val)
        elif txt == 'emailTextLogin':
            if str(val).__contains__('userLogin'):
                uVal=tsObj[device, 'obj'].yamlDict[val]
                tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.editEmailTxtId).send_keys(uVal)
            else:
                tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.editEmailTxtId).send_keys(val)
        elif txt == 'emailPassLogin':
            tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.editPassTxtId).send_keys(val)
        elif txt == 'currNum':
            if val == 'randomNumber':
                numVal = '44'+''.join(random.choices(string.digits, k=10))
                tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.editcurrPhoneTxtId).send_keys(numVal)
            else:
                tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.editcurrPhoneTxtId).send_keys(val)
        elif txt == 'userId':
            tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.editUserId_id).send_keys(val)
        elif txt == 'Address1Id':
            tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.editAddress1Id).send_keys(val)
        elif txt == 'Address2Id':
            tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.editAddress2Id).send_keys(val)
        elif txt == 'cityId':
            tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.editTownCityId).send_keys(val)
        elif txt == 'pinCodeId':
            tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.editPostCodeId).send_keys(val)
        elif txt == 'DelAddress1Id':
            tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.editDelAddress1Id).send_keys(val)
        elif txt == 'DelAddress2Id':
            tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.editDelAddress2Id).send_keys(val)
        elif txt == 'DelcityId':
            tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.editDelTownCityId).send_keys(val)
        elif txt == 'DelpinCodeId':
            tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.editDelPostCodeId).send_keys(val)
        elif txt == 'cardNumberId':
            tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.editCardNumber).send_keys(val)
        elif txt == 'cardExpDateId':
            time.sleep(2)
            tsObj[device, 'webdriver'].back()
            time.sleep(2)
            tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.editCardExpDateId).send_keys(val)
        elif txt == 'cardCvvId':
            tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.editCardCVVId).send_keys(val)
        elif txt == 'cardPostalId':
            tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.editCardPostalCode).send_keys(val)
        elif txt == 'simNumberId':
            tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.editSIMNumberId).send_keys(val)
    else:
        if txt == 'emailText':
            if val == 'randomEmail':
                emailVal = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
                tsObj[device, 'webdriver'].find_element_by_xpath("//XCUIElementTypeTextField[@name=\"" + IOSLoginObj.editEmailTxtId + "\"]").send_keys(emailVal+'@gmail.com')
            else:
                tsObj[device, 'webdriver'].find_element_by_xpath("//XCUIElementTypeTextField[@name=\""+IOSLoginObj.editEmailTxtId+"\"]").send_keys(val)
        elif txt == 'emailPass':
            if str(val).__contains__('userPwd'):
                uVal = tsObj[device, 'obj'].yamlDict[val]
                tsObj[device, 'webdriver'].find_element_by_xpath("///XCUIElementTypeSecureTextField[@name=\"" + IOSLoginObj.editPassTxtId + "\"]").send_keys(uVal)
                tsObj[device, 'webdriver'].find_element_by_xpath("///XCUIElementTypeSecureTextField[@name=\"" + IOSLoginObj.editConfTxtId + "\"]").send_keys(uVal)
                tsObj[device, 'webdriver'].find_element_by_xpath("//XCUIElementTypeSecureTextField").send_keys(Keys.RETURN)
            else:
                tsObj[device, 'webdriver'].find_element_by_xpath("///XCUIElementTypeSecureTextField[@name=\"" + IOSLoginObj.editPassTxtId + "\"]").send_keys(val)
                tsObj[device, 'webdriver'].find_element_by_xpath("///XCUIElementTypeSecureTextField[@name=\"" + IOSLoginObj.editConfTxtId + "\"]").send_keys(val)
                tsObj[device, 'webdriver'].find_element_by_xpath("//XCUIElementTypeSecureTextField").send_keys(Keys.RETURN)
        elif txt == 'emailTextLogin':
            if str(val).__contains__('userLogin'):
                uVal=tsObj[device, 'obj'].yamlDict[val]
                tsObj[device, 'webdriver'].find_element_by_xpath("//XCUIElementTypeTextField[@name=\"" + IOSLoginObj.editEmailTxtId + "\"]").send_keys(uVal)
            else:
                tsObj[device, 'webdriver'].find_element_by_xpath("//XCUIElementTypeTextField[@name=\"" + IOSLoginObj.editEmailTxtId + "\"]").send_keys(val)
        elif txt == 'emailPassLogin':
            tsObj[device, 'webdriver'].find_element_by_xpath("///XCUIElementTypeSecureTextField[@name=\"" + IOSLoginObj.editPassTxtId + "\"]").send_keys(val)
            tsObj[device, 'webdriver'].find_element_by_xpath("//XCUIElementTypeSecureTextField").send_keys(Keys.RETURN)
        elif txt == 'currNum':
            if val == 'randomNumber':
                numVal = '44'.join(random.choices(string.digits, k=10))
                tsObj[device, 'webdriver'].find_element_by_xpath("//XCUIElementTypeTextField[@name=\"" + IOSLoginObj.editcurrPhoneTxtId + "\"]").send_keys(numVal)
            else:
                tsObj[device, 'webdriver'].find_element_by_xpath("//XCUIElementTypeTextField[@name=\""+IOSLoginObj.editcurrPhoneTxtId+"\"]").send_keys(val)
            sendKeysIOSeyboard(device)
        elif txt == 'userId':
            tsObj[device, 'webdriver'].find_element_by_xpath("//XCUIElementTypeTextField[@name=\""+IOSLoginObj.editUserId_id+"\"]").send_keys(val)
            sendKeysIOSeyboard(device)
        elif txt == 'Address1Id':
            tsObj[device, 'webdriver'].find_element_by_xpath("//XCUIElementTypeTextField[@name=\""+IOSLoginObj.editAddress1Id+"\"]").send_keys(val)
        elif txt == 'Address2Id':
            tsObj[device, 'webdriver'].find_element_by_xpath("//XCUIElementTypeTextField[@name=\"" + IOSLoginObj.editAddress2Id + "\"]").send_keys(val)
        elif txt == 'cityId':
            tsObj[device, 'webdriver'].find_element_by_xpath("//XCUIElementTypeTextField[@name=\""+IOSLoginObj.editTownCityId+"\"]").send_keys(val)
        elif txt == 'pinCodeId':
            tsObj[device, 'webdriver'].find_element_by_xpath("//XCUIElementTypeTextField[@name=\""+IOSLoginObj.editPostCodeId+"\"]").send_keys(val)
            sendKeysIOSeyboard(device)
        elif txt == 'cardNumberId':
            tsObj[device, 'webdriver'].find_element_by_xpath("//XCUIElementTypeTextField[@name=\""+IOSLoginObj.editCardNumber+"\"]").send_keys(val)
        elif txt == 'cardCvvId':
            tsObj[device, 'webdriver'].find_element_by_xpath("//XCUIElementTypeTextField[@name=\""+IOSLoginObj.editCardCVVId+"\"]").send_keys(val)
        elif txt == 'cardPostalId':
            tsObj[device, 'webdriver'].find_element_by_xpath("//XCUIElementTypeTextField[@name=\""+IOSLoginObj.editCardPostalCode+"\"]").send_keys(val)
        elif txt == 'simNumberId':
            tsObj[device, 'webdriver'].find_element_by_xpath("//XCUIElementTypeTextField[@name=\""+IOSLoginObj.editSIMNumberId+"\"]").send_keys(val)
        if (context.failed):
            allure.attach(tsObj[device, 'webdriver'].get_screenshot_as_png(), 'screenshot', allure.attachment_type.PNG)
    assert not context.failed


@then("{device} Tap on {val} button")
def tapButton(context,device,val):
    if device == 'Android':
        if val == 'Camera':
            tsObj[device, 'webdriver'].find_element_by_xpath(AndroidLoginObj.shutterButtonXpath).click()
        elif val == 'CameraDone':
            tsObj[device, 'webdriver'].find_element_by_xpath(AndroidLoginObj.cameraDoneXpath).click()
        elif val == 'useHomeAddress':
            tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.checkBoxId).click()
        elif val == 'SideMenu':
            tsObj[device, 'webdriver'].find_element_by_xpath(AndroidLoginObj.sideMenuButtonXpath).click()
    else:
        if val == 'Camera':
            tsObj[device, 'webdriver'].find_element_by_xpath(IOSLoginObj.cameraButton).click()
        elif val == 'shutterButton':
            tsObj[device, 'webdriver'].find_element_by_xpath(IOSLoginObj.cameraShutterButton).click()
        elif val == 'useHomeAddress':
            tsObj[device, 'webdriver'].find_element_by_xpath(IOSLoginObj.useHomeAddSwitch).click()
        if (context.failed):
            allure.attach(tsObj[device, 'webdriver'].get_screenshot_as_png(), 'screenshot', allure.attachment_type.PNG)
    assert not context.failed

@then("{device} Scroll to {val} text")
def scrollToButton(context,device,val):
    if device == 'Android':
        user_scroll = 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("'+val+'").instance(0))'
        tsObj[device, 'webdriver'].find_elements_by_android_uiautomator(user_scroll)
    else:
        script = {"predicateString" : "name == '"+val+"'", "toVisible" : "not an empty string"}
        tsObj[device, 'webdriver'].execute_script('mobile: scroll',script)
    if (context.failed):
        allure.attach(tsObj[device, 'webdriver'].get_screenshot_as_png(), 'screenshot', allure.attachment_type.PNG)
    assert not context.failed

@then("{device} Drag to right for {elementTxt}")
def dragElement(context,device,elementTxt):
    if device == 'Android':
       pass
    else:
        if elementTxt == 'FeaturesTour':
            actions = TouchAction(tsObj[device, 'webdriver'])
            el1 = tsObj[device, 'webdriver'].find_element_by_xpath(IOSLoginObj.featureScreen1Xpath)
            tsObj[device, 'webdriver'].execute_script('mobile: scroll', {'direction': 'right'})
            el2 = tsObj[device, 'webdriver'].find_element_by_xpath(IOSLoginObj.featureScreen2Xpath)
    if (context.failed):
        allure.attach(tsObj[device, 'webdriver'].get_screenshot_as_png(), 'screenshot', allure.attachment_type.PNG)
    assert not context.failed

@then("{device} Select {txtVal} as {val}")
def selectValue(context,device,txtVal,val):
    if device == 'Android':
        if txtVal == 'newNumber':
            tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.selectNumberInputId).clear()
            tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.selectNumberInputId).send_keys(val)
    else:
        if txtVal == 'newNumber':
            tsObj[device, 'webdriver'].find_element_by_xpath(IOSLoginObj.numberSelectPicker).send_keys(val)
    if (context.failed):
        allure.attach(tsObj[device, 'webdriver'].get_screenshot_as_png(), 'screenshot', allure.attachment_type.PNG)
    assert not context.failed


@then("{device} Set {txtVal} as {val}")
def setValue(context,device,txtVal,val):
    if device == 'Android':
        planDict = {
            "Data" : {'1GB':'0','2GB':'25','5GB':'50','10GB':'75','25GB':'100'},
            "Voice": {'100Mins': '0', '250Mins': '25', '500Mins': '50', '1000Mins': '75', 'UnlimitedMins': '100'},
            "SMS": {'100': '0', '250': '25', '500': '50', '1000': '75', 'Unlimited': '100'}
        }
        if txtVal == 'Data':
           slider=tsObj[device, 'webdriver'].find_element_by_xpath(AndroidLoginObj.dataSeekBarXpath)
           xSPnt = slider.location['x'];yPnt=slider.location['y']
           totWidth = slider.size['width'];xEPnt=xSPnt+(totWidth*int(planDict['Data'][val])/100)
           actions = TouchAction(tsObj[device, 'webdriver'])
           actions.press(x=xSPnt, y=yPnt).move_to(x=xEPnt, y=yPnt).release().perform()
        elif txtVal == 'Voice':
            slider = tsObj[device, 'webdriver'].find_element_by_xpath(AndroidLoginObj.minsSeekBarXpath)
            xSPnt = slider.location['x'];
            yPnt = slider.location['y']
            totWidth = slider.size['width'];
            xEPnt = xSPnt + (totWidth * int(planDict['Voice'][val]) / 100)
            actions = TouchAction(tsObj[device, 'webdriver'])
            actions.press(x=xSPnt, y=yPnt).move_to(x=xEPnt, y=yPnt).release().perform()
        elif txtVal == 'SMS':
            slider = tsObj[device, 'webdriver'].find_element_by_xpath(AndroidLoginObj.smsSeekBarXpath)
            xSPnt = slider.location['x'];
            yPnt = slider.location['y']
            totWidth = slider.size['width'];
            xEPnt = xSPnt + (totWidth * int(planDict['SMS'][val]) / 100)
            actions = TouchAction(tsObj[device, 'webdriver'])
            actions.press(x=xSPnt, y=yPnt).move_to(x=xEPnt, y=yPnt).release().perform()
    else:
        pass
    if (context.failed):
        allure.attach(tsObj[device, 'webdriver'].get_screenshot_as_png(), 'screenshot', allure.attachment_type.PNG)
    assert not context.failed

@then("{device} Verify {txtVal} text as {val}")
def verifyTxtValue(context,device,txtVal,val):
    if device == 'Android':
        if txtVal == 'planPrice':
            fVal = tsObj[device, 'webdriver'].find_element_by_id(AndroidLoginObj.planPriceId).text
            if fVal != val:
                context.failed = True
            else:
                allure.attach(fVal, 'Plan Price:', allure.attachment_type.TEXT)
    else:
        pass
    if (context.failed):
        allure.attach(tsObj[device, 'webdriver'].get_screenshot_as_png(), 'screenshot', allure.attachment_type.PNG)
    assert not context.failed


@then("{device} Go to previous screen")
def pressBackButton(context,device):
    if device == 'Android':
        tsObj[device, 'webdriver'].find_element_by_xpath(AndroidLoginObj.backButtonXpath).click()
    else:
        pass
    if (context.failed):
        allure.attach(tsObj[device, 'webdriver'].get_screenshot_as_png(), 'screenshot', allure.attachment_type.PNG)
    assert not context.failed

@then("{device} Take a screenshot")
def takeScreenShot(context,device):
        allure.attach(tsObj[device, 'webdriver'].get_screenshot_as_png(), 'screenshot', allure.attachment_type.PNG)


