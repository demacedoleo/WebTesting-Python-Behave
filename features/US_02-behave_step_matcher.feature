Feature: Use step matcher to improve skills

  As a Automation Engineer
  I want to get links by search using step matcher
  So that to increase my automation power

  . NOTES:
  .  * Simple scenario to know with work behave
  .  * It is a base project to start automation with python and behave
  .  * Implement the page object pattern with spring python

  @step_matcher
  Scenario: The user find links according your search
    Given A googler open the "http://www.google.com"
    When Search information about step_matcher
    Then Verify that web page contains at least "5" links

  @step_matcher
  Scenario: The user find links according your search
    Given A googler open the "http://www.google.com"
    When Search links about step_matcher
    Then Verify that web page contains at least "5" links