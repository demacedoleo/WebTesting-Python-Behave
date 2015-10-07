Feature: Fight or flight
  In order to know similar web pages
  As a Googler
  I want to obtain links by search

  @Regression @browser
  Scenario: Verify links by page
    Given Google is live
     When Googler search pages matching with "Apple"
     Then Googler get "10" links per page