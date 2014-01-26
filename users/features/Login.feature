Feature: Login

    Scenario: Login with valid credentials
        Given a user "austiine" with password "password" exists
        And i login as "austiine" with password "password"
        Then i should see "Hi austiine".
        And i should see a logout link