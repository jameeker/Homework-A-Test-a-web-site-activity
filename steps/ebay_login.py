from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Given step
@given('I am on the eBay homepage')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('https://www.ebay.com/')
    assert 'Electronics, Cars, Fashion, Collectibles & More | eBay' in context.browser.title

#
@given(u'that we have gone to wwww.ebay.com')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given that we have gone to wwww.ebay.com')
#

# When steps
@when('I click on the "Sign In" button')
def step_impl(context):
    sign_in_link = context.browser.find_element_by_id('gh-ug') 
    sign_in_link.click()

@when('I enter valid login credentials')
def step_impl(context):
    username_field = context.browser.find_element_by_id('userid')
    password_field = context.browser.find_element_by_id('pass')
    username_field.send_keys('my_username')
    password_field.send_keys('my_password')

@when('I enter invalid login credentials')
def step_impl(context):
    username_field = context.browser.find_element_by_id('userid')
    password_field = context.browser.find_element_by_id('pass')
    username_field.send_keys('invalid_username')
    password_field.send_keys('invalid_password')

@when('I click on the "Login" button')
def step_impl(context):
    login_button = context.browser.find_element_by_id('sgnBt')
    login_button.click()

#
@when(u'we click on on "<gh-menu>"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we click on on "<gh-menu>"')
#

# Then steps
@then('I should be redirected to the "My eBay" page')
def step_impl(context):
    assert 'My eBay' in context.browser.title

@then('I should see my username displayed')
def step_impl(context):
    username_element = context.browser.find_element_by_id('gh-ug') 
    assert 'my_username' in username_element.text

@then('I should see an error message')
def step_impl(context):
    error_message = context.browser.find_element_by_id('errf')
    assert 'Incorrect username or password. Please try again.' in error_message.text

@then('I should still be on the login page')
def step_impl(context):
    assert 'Sign in or Register | eBay' in context.browser.title

#
@then(u'we are directed to the login page "<signin-form>"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we are directed to the login page "<signin-form>"')
#
