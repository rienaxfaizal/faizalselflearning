import pytest
import time

from todoist.app.pages.LoginPage import LoginPage


@pytest.mark.stable
def test_create_project(driver, todoist_api, todoist_test_user):
    TEST_PROJECT_NAME = 'test_project_creation'

    # Create project via API
    todoist_api.create_project(TEST_PROJECT_NAME)

    # Login to Todoist
    login_page = LoginPage(driver)
    main_page = login_page.select_email_login()\
        .set_email(todoist_test_user['email'])\
        .continue_with_email()\
        .set_password(todoist_test_user['password'])\
        .click_login()

    # TODO: replace with explicit wait
    time.sleep(10)

    # Get list of projects
    projects_list = main_page.expand_sidebar()\
        .expand_projects()\
        .get_project_list()

    assert TEST_PROJECT_NAME in projects_list

    # Cleanup
    todoist_api.delete_project_by_name(TEST_PROJECT_NAME)
