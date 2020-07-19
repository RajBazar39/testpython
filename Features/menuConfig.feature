Feature: Configuration Menus Scenarios

@TC_ME_CONF1_001
Scenario: Bottom menu is properly configured for Config1
  Given config1 is pushed successfully on server 52.53.197.70:8080
  Then Android Wait for 5 seconds
  Given Android Launch application
  Then Android Verify that BottomMenu is visible
  Then Android Verify that BottomMenuMyPage is visible
  Then Android Verify that BottomMenuMyPage is present at position 0
  Then Android Verify that BottomMenuFeaturesTour is visible
  Then Android Verify that BottomMenuFeaturesTour is present at position 1
  Then Android Verify that BottomMenuAccount is visible
  Then Android Verify that BottomMenuAccount is present at position 2

@TC_ME_CONF1_002
Scenario: Side menu is properly configured for Config1
  Given Android Execute Steps in tag TC_ME_CONF1_001
  Given Android Launch application
  Then Android Tap on SideMenu button
  Then Android Verify that SideMenuList is visible
  Then Android Verify that GetHelpButton is visible
  Then Android Verify that GetHelpButton is present at position 0
  Then Android Verify that MarketplaceButton is visible
  Then Android Verify that MarketplaceButton is present at position 1
  Then Android Verify that ActionCentreButton is visible
  Then Android Verify that ActionCentreButton is present at position 2
  Then Android Verify that LogoutButton is visible
  Then Android Verify that LogoutButton is present at position 3
  Then Android Verify that AboutButton is visible
  Then Android Verify that AboutButton is present at position 4
  Then Android Verify that DebugOptionsButton is visible
  Then Android Verify that DebugOptionsButton is present at position 5


@TC_ME_CONF2_001
Scenario: Bottom menu is properly configured for Config2
  Given config2 is pushed successfully on server 52.53.197.70:8080
  Then Android Wait for 5 seconds
  Given Android Launch application
  Then Android Verify that BottomMenu is visible
  Then Android Verify that BottomMenuMyPage is visible
  Then Android Verify that BottomMenuMyPage is present at position 0
  Then Android Verify that BottomMenuMarketplace is visible
  Then Android Verify that BottomMenuMarketplace is present at position 1
  Then Android Verify that BottomMenuAccount is visible
  Then Android Verify that BottomMenuAccount is present at position 2

@TC_ME_CONF2_002
Scenario: Side menu is properly configured for Config2
  Given Android Execute Steps in tag TC_ME_CONF2_001
  Given Android Launch application 
  Then Android Tap on SideMenu button
  Then Android Verify that SideMenuList is visible 
  Then Android Verify that GetHelpButton is visible
  Then Android Verify that GetHelpButton is present at position 0
  Then Android Verify that FeaturesTourButton is visible
  Then Android Verify that FeaturesTourButton is present at position 1
  Then Android Verify that ActionCentreButton is visible
  Then Android Verify that ActionCentreButton is present at position 2
  Then Android Verify that LogoutButton is visible
  Then Android Verify that LogoutButton is present at position 3
  Then Android Verify that AboutButton is visible
  Then Android Verify that AboutButton is present at position 4
  Then Android Verify that DebugOptionsButton is visible
  Then Android Verify that DebugOptionsButton is present at position 5


@TC_ME_CONF_ALL
Scenario: Run ALl Configs
  Given Android Execute Steps in tag TC_ME_CONF1_001
  Given Android Execute Steps in tag TC_ME_CONF1_002
  Given Android Execute Steps in tag TC_ME_CONF2_001
  Given Android Execute Steps in tag TC_ME_CONF2_002