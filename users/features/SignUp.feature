Feature: User registration

    Scenario: Submitting sign up form with matching passwords
        Given I access the url "/users/new".
        And I sign up with credentials "supermarket@email.com", "password", "password".
        Then i should not see "CSRF verification failed. Request aborted."
        And i should see "Your account has been successfully created".
        
    Scenario: Submitting up form with mis - matching passwords
        Given I access the url "/users/new".
        And I sign up with credentials "supermarket@email.com", "password", "password123".
        Then i should not see "CSRF verification failed. Request aborted."
        And i should see "The two password fields didn't match".