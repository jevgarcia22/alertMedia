from selenium import webdriver
import pom

if __name__ == '__main__':
    search_term = "stackoverflow"
    filter_term = "python"
    tag = "python-3.6"

    driver = webdriver.Chrome()
    driver.maximize_window()

    # navigate to google
    driver.get("https://www.google.com")

    # type in stackoverflow
    pom.WebElements(driver).search_google(search_term=search_term)

    # click link for stackoverlow
    pom.WebElements(driver).select_result(search_term=search_term)

    # open hamburger menu
    pom.WebElements(driver).open_menu()

    # select tags
    pom.WebElements(driver).click_tags()

    # filter for python tags
    pom.WebElements(driver).filter_by_tag_name(filter_term=filter_term)

    # select link for python-3.6
    pom.WebElements(driver).select_tag(tag=tag)

    # open filter options
    pom.WebElements(driver).open_filter_options()

    # click to sort by most frequent & apply filter
    pom.WebElements(driver).select_and_apply_filter()

    # find the question with highest number of votes and click on it
    pom.WebElements(driver).click_question_with_highest_votes()

    # find the answer with the highest number of votes & print author name
    pom.WebElements(driver).get_author_highest_voted_answer()
