Feature: Onboarding Flow Scenarios

@TC_OB_001
Scenario: Choosing number page
    Given Android Install and launch application
    Then Android Tap on SKIP button text
    Then Android Tap on REGISTER button text
    Then Android Set id emailText as randomEmail
    Then Android Set id emailPass as userPwd1
    Then Android Tap on REGISTER button text
    Then Android Tap on START ONBOARDING button text

@TC_OB_1001
Scenario: Choosing number page IOS
    Given IOS Install and launch application
    Then IOS Tap on Skip button text
    Then IOS Tap on Register button text
    Then IOS Set id emailText as randomEmail
    Then IOS Set id emailPass as userPwd1
    Then IOS Tap on Register button text
    Then IOS Tap on Start Onboarding button text

@TC_OB_002
Scenario: Choosing number page want to keep your number?
    Given Android Execute Steps in tag TC_OB_001
    Then Android Set id currNum as randomNumber
    Then Android Tap on PORT NUMBER button text

@TC_OB_1002
Scenario: Choosing number page want to keep your number? IOS
    Given IOS Execute Steps in tag TC_OB_1001
    Then IOS Set id currNum as 447500977124
    Then IOS Tap on Port Number button text


@TC_OB_003
Scenario: Choosing number page_Select a new number
    Given Android Execute Steps in tag TC_OB_001
    Then Android Select newNumber as 246824682
    Then Android Wait for 2 seconds
    Then Android Tap on SELECT NUMBER button text

@TC_OB_1003
Scenario: Choosing number page_Select a new number IOS
    Given IOS Execute Steps in tag TC_OB_1001
    Then IOS Select newNumber as 246824682
    Then IOS Wait for 2 seconds
    Then IOS Tap on Select Number button text

@TC_OB_004
Scenario: Choosing number page_Already have a SIM?
    Given Android Execute Steps in tag TC_OB_001
    Then Android Scroll to ACTIVATE SIM text
    Then Android Tap on ACTIVATE SIM button text
    Then Android Set id simNumberId as 11123243
    Then Android Tap on SUBMIT SIM NUMBER button text

@TC_OB_1004
Scenario: Choosing number page_Already have a SIM? IOS
    Given IOS Execute Steps in tag TC_OB_1001
    Then IOS Tap on Activate SIM button text
    Then IOS Set id simNumberId as 11123243
    Then IOS Tap on Submit button text

@TC_OB_005
Scenario: Choosing number page_back button
    Given Android Launch application
    Then Android Tap on START ONBOARDING button text
    Then Android Go to previous screen
    Then Android Wait for 3 seconds
    Then Android Take a screenshot

@TC_OB_007
Scenario: Configure your plan page_Data Voice SMS
    Given Android Execute Steps in tag TC_OB_001
    Given Android Execute Steps in tag TC_OB_002
    Then Android Set Data as 5GB
    Then Android Set Voice as 1000Mins
    Then Android Set SMS as 250
    Then Android Verify planPrice text as $33.0
    Then Android Tap on NEXT button text

@TC_OB_008
Scenario: Configure your plan page_back button
    Given Android Launch application
    Then Android Tap on START ONBOARDING button text
    Then Android Set id currNum as randomNumber
    Then Android Tap on PORT NUMBER button text
    Then Android Go to previous screen
    Then Android Wait for 3 seconds
    Then Android Take a screenshot


@TC_OB_010
Scenario: Identity Validation Take a photo? Using Passport ID
    Given Android Execute Steps in tag TC_OB_001
    Given Android Execute Steps in tag TC_OB_002
    Given Android Execute Steps in tag TC_OB_007
    Then Android Tap on IM A CAMERA button text
    Then Android Tap on Take Photo text
    Then Android Handle Camera Permission Popups
    Then Android Wait for 5 seconds
    Then Android Tap on Camera button
    Then Android Tap on CameraDone button
    Then Android Tap on Passport RadioButton text
    Then Android Set id userId as KASD12345678
    Then Android Scroll to NEXT text
    Then Android Tap on NEXT button text
    Then Android Wait for 5 seconds



@TC_OB_010_1
Scenario: Identity Validation Take a photo? Using National ID
    Given Android Execute Steps in tag TC_OB_001
    Given Android Execute Steps in tag TC_OB_002
    Given Android Execute Steps in tag TC_OB_007
    Then Android Tap on IM A CAMERA button text
    Then Android Tap on Take Photo text
    Then Android Handle Camera Permission Popups
    Then Android Wait for 5 seconds
    Then Android Tap on Camera button
    Then Android Tap on CameraDone button
    Then Android Tap on National ID RadioButton text
    Then Android Set id userId as UKRT12345678
    Then Android Scroll to NEXT text
    Then Android Tap on NEXT button text
    Then Android Wait for 5 seconds


@TC_OB_010_2
Scenario: Identity Validation Take a photo? Using Drivers License
    Given Android Execute Steps in tag TC_OB_001
    Given Android Execute Steps in tag TC_OB_002
    Given Android Execute Steps in tag TC_OB_007
    Then Android Tap on IM A CAMERA button text
    Then Android Tap on Take Photo text
    Then Android Handle Camera Permission Popups
    Then Android Wait for 5 seconds
    Then Android Tap on Camera button
    Then Android Tap on CameraDone button
    Then Android Tap on Drivers License RadioButton text
    Then Android Set id userId as AABB12345678
    Then Android Scroll to NEXT text
    Then Android Tap on NEXT button text
    Then Android Wait for 5 seconds



@TC_OB_011
Scenario: Identity validation - Step 1 page_ back button
    Given Android Launch application
    Then Android Tap on START ONBOARDING button text
    Then Android Set id currNum as randomNumber
    Then Android Tap on PORT NUMBER button text
    Then Android Tap on NEXT button text
    Then Android Go to previous screen
    Then Android Wait for 3 seconds
    Then Android Take a screenshot


@TC_OB_013
Scenario: Identity validation - Step 1 page_ back button
    Given Android Launch application
    Then Android Tap on START ONBOARDING button text
    Then Android Set id currNum as randomNumber
    Then Android Tap on PORT NUMBER button text
    Then Android Tap on NEXT button text
    Then Android Tap on IM A CAMERA button text
    Then Android Tap on Take Photo text
    Then Android Wait for 5 seconds
    Then Android Tap on Camera button
    Then Android Tap on CameraDone button
    Then Android Tap on Passport RadioButton text
    Then Android Set id userId as KASD12345678
    Then Android Scroll to NEXT text
    Then Android Tap on NEXT button text
    Then Android Wait for 5 seconds
    Then Android Go to previous screen
    Then Android Wait for 3 seconds
    Then Android Take a screenshot


@TC_OB_014
Scenario: Address Validation page
    Given Android Execute Steps in tag TC_OB_001
    Given Android Execute Steps in tag TC_OB_002
    Given Android Execute Steps in tag TC_OB_007
    Given Android Execute Steps in tag TC_OB_010
    Then Android Tap on IM A CAMERA button text
    Then Android Tap on Take Photo text
    Then Android Wait for 5 seconds
    Then Android Tap on Camera button
    Then Android Tap on CameraDone button
    Then Android Tap on NEXT button text
    Then Android Set id Address1Id as 301 New Lane
    Then Android Set id Address2Id as Old Street
    Then Android Set id cityId as Ipswich
    Then Android Set id pinCodeId as IP12AB
    Then Android Tap on IM A CAMERA button text
    Then Android Tap on Take Photo text
    Then Android Wait for 5 seconds
    Then Android Tap on Camera button
    Then Android Tap on CameraDone button
    Then Android Scroll to NEXT text
    Then Android Tap on NEXT button text


@TC_OB_015
Scenario: Address validation page_back button
    Given Android Launch application
    Then Android Tap on START ONBOARDING button text
    Then Android Set id currNum as randomNumber
    Then Android Tap on PORT NUMBER button text
    Then Android Tap on NEXT button text
    Then Android Tap on IM A CAMERA button text
    Then Android Tap on Take Photo text
    Then Android Wait for 5 seconds
    Then Android Tap on Camera button
    Then Android Tap on CameraDone button
    Then Android Tap on Passport RadioButton text
    Then Android Set id userId as KASD12345678
    Then Android Scroll to NEXT text
    Then Android Tap on NEXT button text
    Then Android Tap on IM A CAMERA button text
    Then Android Tap on Take Photo text
    Then Android Wait for 5 seconds
    Then Android Tap on Camera button
    Then Android Tap on CameraDone button
    Then Android Tap on NEXT button text
    Then Android Wait for 5 seconds
    Then Android Go to previous screen
    Then Android Wait for 3 seconds
    Then Android Take a screenshot


@TC_OB_016
Scenario: Delivery options page
    Given Android Execute Steps in tag TC_OB_001
    Given Android Execute Steps in tag TC_OB_002
    Given Android Execute Steps in tag TC_OB_007
    Given Android Execute Steps in tag TC_OB_010
    Given Android Execute Steps in tag TC_OB_014
    Then Android Set id DelAddress1Id as 501 New Lane
    Then Android Set id DelAddress2Id as Old Street
    Then Android Set id DelcityId as Ipswich
    Then Android Set id DelpinCodeId as IP12AB
    Then Android Tap on NEXT button text
    Then Android Tap on PLACE ORDER button text


@TC_OB_017
Scenario: Delivery options page_back button
    Given Android Launch application
    Then Android Tap on START ONBOARDING button text
    Then Android Set id currNum as randomNumber
    Then Android Tap on PORT NUMBER button text
    Then Android Tap on NEXT button text
    Then Android Tap on IM A CAMERA button text
    Then Android Tap on Take Photo text
    Then Android Wait for 5 seconds
    Then Android Tap on Camera button
    Then Android Tap on CameraDone button
    Then Android Tap on Passport RadioButton text
    Then Android Set id userId as KASD12345678
    Then Android Scroll to NEXT text
    Then Android Tap on NEXT button text
    Then Android Tap on IM A CAMERA button text
    Then Android Tap on Take Photo text
    Then Android Wait for 5 seconds
    Then Android Tap on Camera button
    Then Android Tap on CameraDone button
    Then Android Tap on NEXT button text
    Then Android Wait for 5 seconds
    Then Android Set id Address1Id as 301 New Lane
    Then Android Set id Address2Id as Old Street
    Then Android Set id cityId as Ipswich
    Then Android Set id pinCodeId as IP12AB
    Then Android Tap on IM A CAMERA button text
    Then Android Tap on Take Photo text
    Then Android Wait for 5 seconds
    Then Android Tap on Camera button
    Then Android Tap on CameraDone button
    Then Android Scroll to NEXT text
    Then Android Tap on NEXT button text
    Then Android Go to previous screen
    Then Android Wait for 3 seconds
    Then Android Take a screenshot


@TC_OB_018
Scenario: Delivery Options page Use your home address
    Given Android Execute Steps in tag TC_OB_001
    Given Android Execute Steps in tag TC_OB_002
    Given Android Execute Steps in tag TC_OB_007
    Given Android Execute Steps in tag TC_OB_010
    Given Android Execute Steps in tag TC_OB_014
    Then Android Tap on useHomeAddress button
    Then Android Tap on NEXT button text
    Then Android Tap on PLACE ORDER button text
    #Then Android Execute Steps in current scenario


@TC_OB_020
Scenario: Payment details page
    Given Android Execute Steps in tag TC_OB_001
    Given Android Execute Steps in tag TC_OB_002
    Given Android Execute Steps in tag TC_OB_007
    Given Android Execute Steps in tag TC_OB_010
    Given Android Execute Steps in tag TC_OB_014
    Given Android Execute Steps in tag TC_OB_018
    Then Android Tap on Credit or Debit Card text
    Then Android Wait for 3 seconds
    Then Android Set id cardNumberId as 4111111111111111
    Then Android Set id cardExpDateId as 042020
    Then Android Set id cardCvvId as 456
    Then Android Set id cardPostalId as 12345
    Then Android Tap on ADD CARD button text
    Then Android Tap on ACTIVATE SIM button text
    Then Android Set id simNumberId as 11123243
    Then Android Tap on SUBMIT SIM NUMBER button text
    Then Android Tap on CLICK HERE TO FINISH button text
    Then Android Wait for 5 seconds


@TC_OB_021
Scenario: Payment details page_back button
    Given Android Launch application 
    Then Android Tap on START ONBOARDING button text
    Then Android Set id currNum as randomNumber
    Then Android Tap on PORT NUMBER button text
    Then Android Tap on NEXT button text
    Then Android Tap on IM A CAMERA button text
    Then Android Tap on Take Photo text
    Then Android Wait for 5 seconds
    Then Android Tap on Camera button
    Then Android Tap on CameraDone button
    Then Android Tap on Passport RadioButton text
    Then Android Set id userId as KASD12345678
    Then Android Scroll to NEXT text
    Then Android Tap on NEXT button text
    Then Android Tap on IM A CAMERA button text
    Then Android Tap on Take Photo text
    Then Android Wait for 5 seconds
    Then Android Tap on Camera button
    Then Android Tap on CameraDone button
    Then Android Tap on NEXT button text
    Then Android Wait for 5 seconds
    Then Android Set id Address1Id as 301 New Lane
    Then Android Set id Address2Id as Old Street
    Then Android Set id cityId as Ipswich
    Then Android Set id pinCodeId as IP12AB
    Then Android Tap on IM A CAMERA button text
    Then Android Tap on Take Photo text
    Then Android Wait for 5 seconds
    Then Android Tap on Camera button
    Then Android Tap on CameraDone button
    Then Android Scroll to NEXT text
    Then Android Tap on NEXT button text
    Then Android Tap on useHomeAddress button
    Then Android Tap on NEXT button text
    Then Android Go to previous screen
    Then Android Wait for 3 seconds
    Then Android Take a screenshot


@TC_Test_1001
  Scenario: Install Application IOS
    Given IOS Install and launch application
