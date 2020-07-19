Feature: Test Basic Navigation

  @TC_LS_001
  Scenario: Install Application Android
    Given Android Install and launch application

  @TC_LS_002
  Scenario: Android Test application load time
    Given Android Install and launch application
    Given Android Test load time of app

  @TC_LS_1002
  Scenario: IOS Test application load time
    Given IOS Install and launch application
    Given IOS Test load time of app

  @TC102
  Scenario: Android OnBoarding flow Test
    Given Android Install and launch application
    Then Android Tap on SKIP button text
    Then Android Tap on REGISTER button text
    Then Android Set id emailText as randomEmail
    Then Android Set id emailPass as userPwd1
    Then Android Tap on REGISTER button text
    Then Android Tap on START ONBOARDING button text
    Then Android Set id currNum as 447700877600
    Then Android Tap on PORT NUMBER button text
    Then Android Tap on NEXT button text
    Then Android Tap on IM A CAMERA button text
    Then Android Tap on Take Photo text
    Then Android Handle Camera Permission Popups
    Then Android Wait for 5 seconds
    Then Android Tap on Camera button
    Then Android Tap on CameraDone button
    Then Android Set id userId as KASD12345678
    Then Android Scroll to NEXT text
    Then Android Tap on NEXT button text
    Then Android Wait for 5 seconds
    Then Android Tap on IM A CAMERA button text
    Then Android Tap on Take Photo text
    Then Android Wait for 5 seconds
    Then Android Tap on Camera button
    Then Android Tap on CameraDone button
    Then Android Tap on NEXT button text
    Then Android Set id Address1Id as 301, Mynew Lane
    Then Android Set id Address2Id as Oldstreet
    Then Android Set id cityId as Ipswich
    Then Android Set id pinCodeId as IP15QA
    Then Android Tap on IM A CAMERA button text
    Then Android Tap on Take Photo text
    Then Android Wait for 5 seconds
    Then Android Tap on Camera button
    Then Android Tap on CameraDone button
    Then Android Scroll to NEXT text
    Then Android Tap on NEXT button text
    Then Android Tap on useHomeAddress button
    Then Android Tap on NEXT button text
    Then Android Tap on PLACE ORDER button text
    Then Android Tap on Credit or Debit Card text
    Then Android Wait for 3 seconds
    Then Android Set id cardNumberId as 4111111111111111
    Then Android Set id cardExpDateId as 042020
    Then Android Set id cardCvvId as 456
    Then Android Set id cardPostalId as IP15QA
    Then Android Tap on ADD CARD button text
    Then Android Tap on ACTIVATE SIM button text
    Then Android Set id simNumberId as 11123243
    Then Android Tap on SUBMIT SIM NUMBER button text

  @TC_LS_1001
  Scenario: Install Application IOS
    Given IOS Install and launch application

  @TC_LS_1002
  Scenario: IOS Registration Test
    Given IOS Install and launch application
    Then IOS Tap on Skip button text
    Then IOS Tap on Register button text
    Then IOS Set id emailText as rajbazar141@gmail.com
    Then IOS Set id emailPass as qqqqqqqqq
    Then IOS Tap on Register button text
    Then IOS Tap on Start Onboarding button text
    Then IOS Set id currNum as 447500977124
    Then IOS Tap on Port Number button text
    Then IOS Tap on Next button text
    Then IOS Tap on Camera button
    Then IOS Tap on shutterButton button
    Then IOS Set id userId as KASD12345678
    Then IOS Tap on Next button text
    Then IOS Tap on Camera button
    Then IOS Tap on shutterButton button
    Then IOS Tap on Next button text
    Then IOS Set id Address1Id as 301, Mynew Lane
    Then IOS Set id Address2Id as Oldstreet
    Then IOS Set id cityId as Ipswich
    Then IOS Set id pinCodeId as IP15QA
    Then IOS Tap on Camera button
    Then IOS Tap on shutterButton button
    Then IOS Scroll to Next text
    Then IOS Tap on Next button text
    Then IOS Tap on useHomeAddress button
    Then IOS Tap on Next button text
    Then IOS Tap on Place Order button text
    Then IOS Tap on Credit or Debit Card text
    Then IOS Set id cardNumberId as 4111111111111111
    Then IOS Tap on 04 text
    Then IOS Tap on 2021 text
    Then IOS Set id cardCvvId as 456
    Then IOS Set id cardPostalId as 11223355
    Then IOS Tap on Add Card button text
    Then IOS Tap on Activate SIM button text
    Then IOS Set id simNumberId as 11123243
    Then IOS Tap on Submit button text
    Then IOS Tap on Click here to finish button text

  @TC_LS_008 @TC_LS_009
  Scenario: Android Login Test Scenario
    Given Android Launch application
    Then Android Set id emailTextLogin as userLogin1
    Then Android Set id emailPassLogin as userPwd1
    Then Android Tap on LOGIN button text

  @TC_LS_1008 @TC_LS_1009
  Scenario: Login Test Scenario
    Given IOS Launch application
    Then IOS Set id emailTextLogin as userLogin2
    Then IOS Set id emailPassLogin as userPwd2
    Then IOS Tap on Login button text

  @TC1004
  Scenario: Navigate Menu Items
    Given IOS Launch application
    Then IOS Tap on Menu button text
    Then IOS Tap on Get Help text
    Then IOS Tap on Dismiss button text
    Then IOS Tap on Menu button text
    Then IOS Tap on Features Tour text
    Then IOS Drag to right for FeaturesTour
    Then IOS Tap on Dismiss button text
    Then IOS Tap on Menu button text
    Then IOS Tap on Action Centre text
    Then IOS Tap on Dismiss button text
    Then IOS Tap on Menu button text
    Then IOS Tap on About text
    Then IOS Tap on Dismiss button text
    Then IOS Tap on Menu button text
    Then IOS Tap on Debug Options text
    Then IOS Tap on Dismiss button text
    Then IOS Tap on Menu button text
    Then IOS Tap on Logout text
    Then IOS Tap on OK button text


