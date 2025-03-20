Feature: Order Transaction
  Tests related to Order Transaction


  Scenario Outline: Verify Order success message shown in details page
    Given place the item in order with <username> and <password>
    And the user is on landing page
    When I login to portal with <username> and <password>
    And navigate to orders page
    And select order Id
    Then order message is successfully displayed
    Examples:
    |username             |password   |
    |rahulshetty@gmail.com|Iamking@000|