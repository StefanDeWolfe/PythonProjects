Description: add invite user function 

Acceptance Criteria: 

1. Users with admin role can invite new users by email 
2. The email signup link expires after 1 hour 

# Written in Gherkin
Feature: Invite user
    Users with admin role can invite new users by email 
    The email signup link expires after 1 hour 
# There are Admin roles and non-admin, standard user roles
# Only NEW users can be invited
# Email invite expires after an hour
# Assumptions:
#   The Admin user is either created (in code) or predefined as a part of setup.
#   Admin credentials are stored in a safe file and decoded for use in code.
#   The new users are removed after each run as a part of test teardown (in code).
#   The "" around words mean that this is a parameter that is passed into the test.
#   The <> around words mean that it is an example, something we define at 
#     this level that is a parameter that is passed into the test.
# Positive tests:

Scenario: Admin invites new user, new user clicks sign up link
    Given "admin" is logged in
    When "admin" invites new user <NewUserEmail>
    And <NewUserEmail> has invitation email
    And the <NewUserEmail> follows the link
    Then the user can sign up

    Examples:
        | NewUserEmail   | 
        | user@email.com |

Scenario: New user clicks sign up link just before/after it expires
    Given the "admin" is logged in
    When the "admin" invites new user <NewUserEmail>
    And the <NewUserEmail> has invitation email
    And the <NewUserEmail> follows the link at "1" minute <beforeAfter> expiration
    Then the user <CanOrCannot> sign up

    Examples:
        | NewUserEmail   | beforeAfter | CanOrCannot |
        | user1@email.com | before      | can         |
        | user2@email.com | after       | cannot      |

# Negative Tests:

Scenario Outline: Admin gets alert message that user already exists
    Given the "admin" is logged in
    When the "admin" invites new user "<ExistingEmail>"
    Then the "admin" cannot add existing user

    Examples:
        | ExistingEmail      |
        | existing@email.com |


Scenario Outline: Admin gets email return to sender
    Given the "admin" is logged in
    When the "admin" invites new user <BogusEmail>
    Then the "admin" gets a "email not found" email

    Examples:
        | BogusEmail   | 
        | bogus@email.com |

Scenario Outline: non-admin user fails to invite new user
    Given the "user" is logged in
    When the "user" invites new user <NewUserEmail>
    Then the "user" cannot invite new user

    Examples:
        | NewUserEmail   | 
        | user@email.com |