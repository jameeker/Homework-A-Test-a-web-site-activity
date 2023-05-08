Feature: User Login on eBay

  Scenario: There has been a successful login
    Given I am on the eBay homepage
    When I click on the "Sign In" button
        And I enter valid login credentials
        And I click on the "Login" button
    Then I should be redirected to the "My eBay" page
        And I should see my username displayed

  Scenario: There has been an invalid login
    Given I am on the eBay homepage
    When I click on the "Sign In" button
        And I enter invalid login credentials
        And I click on the "Login" button
    Then I should see an error message
        And I should still be on the login page

Scenario Outline: Sign in/ login
    Given that we have gone to wwww.ebay.com
     When we click on on "<gh-menu>"
     Then we are directed to the login page "<signin-form>"

Examples: Different user credentials
  | username  | password |
  | user1     | pass123  |
  | user2     | 123456678|
  | jmeeker9  | 872384917|