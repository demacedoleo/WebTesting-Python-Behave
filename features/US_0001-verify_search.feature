Feature: Verify amount links is displayed by search

  As a Automation Engineer
  I want to get links by search
  So that to give more options

  . NOTES:
  .  * Simple scenario to know with work behave
  .  * It is a base project to start automation with python and behave
  .  * Implement the page object pattern with spring python

  @Regression
  Scenario: The user find links according your search
    Given The user open "http://www.google.com"
    When Search to get information about "behave"
    Then Verify that web page contains at least "5" links