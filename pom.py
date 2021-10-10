from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time


class Locators(object):
    """class to hold required locators"""

    # Google search elements
    input_field = "//input[@name='q']"
    google_home = "//img[@alt='Google']"

    # Popup elements
    popup = "//*[@class='ff-sans ps-fixed z-nav-fixed ws4 sm:w-auto p32 sm:p16 bg-black-750 fc-white bar-lg " \
             "b16 l16 r16 js-consent-banner']"
    accept_cookies_btn = '//button[contains(., "Accept all cookies")]'

    # Stack Overflow elements
    hamburger_menu = '//a[contains(@href, "#")][@role="menuitem"]'
    tags_menu_option = "nav-tags"
    tags_h1 = "//h1[contains(., 'Tags')]"
    filter_input_field = "tagfilter"

    # filter elements
    filter_btn = '//button[@class="s-btn s-btn__filled s-btn__sm s-btn__icon ws-nowrap"]'
    sort_by_most_frequent_radio_btn = "//input[@value='MostFrequent']"
    apply_filter_btn = '//button[@data-se-uql-target="applyButton"]'

    # question/answer vote elements
    question_votes = '//span[@class="vote-count-post "]'
    answer_votes = "//div[contains(@class, 'vote-count')]"


class WebElements:
    # when class is instantiated, run this automatically
    def __init__(self, driver):
        """
        :param driver:
        """
        self.driver = driver

    def wait_for_page_to_load(self, locator):
        """
        wait for page to load based on given locator
        :return: None
        """
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(locator))

    def search_google(self, search_term):
        """
        input search term and press Enter to search
        :param search_term: string to search on
        :return: None
        """
        search_input = self.driver.find_element_by_xpath(Locators.input_field)
        search_input.send_keys(search_term)
        search_input.send_keys(Keys.RETURN)

    def select_result(self, search_term):
        """
        selects the link that contains the given search parameter
        :param search_term: string
        :return: None
        """
        self.wait_for_page_to_load(locator=(By.XPATH, Locators.google_home))
        self.driver.find_element_by_xpath("//a[contains(@href, '"+search_term+"')]//h3").click()
        self.check_for_popup()

    def check_for_popup(self):
        """
        checks for presence of popup window, closes if necessary
        :return: None
        """
        popup = Locators.popup
        btn = Locators.accept_cookies_btn
        if (self.driver.find_element_by_xpath(popup)).is_displayed():
            self.driver.find_element_by_xpath(btn).click()
        else:
            pass

    def open_menu(self):
        """
        opens stackoverflow hamburger menu
        :return: None
        """
        menu = self.driver.find_element_by_xpath(Locators.hamburger_menu)
        menu.click()

    def click_tags(self):
        """
        select tags option from hamburger menu
        :return: None
        """
        tags = self.driver.find_element_by_id(Locators.tags_menu_option)
        tags.click()

    def filter_by_tag_name(self, filter_term):
        """
        enter string into Filter by tag name field and press enter,
        sleep(2) used to allow time for transition
        :param filter_term: term to filter by
        :return: None
        """
        self.wait_for_page_to_load(locator=(By.XPATH, Locators.tags_h1))
        self.check_for_popup()
        filter_input_field = self.driver.find_element_by_id(Locators.filter_input_field)
        filter_input_field.send_keys(filter_term)
        time.sleep(2)

    def select_tag(self, tag):
        """
        select a tag from the filtered tags view
        :param tag: tag to select
        :return: None
        """
        tag = self.driver.find_element_by_xpath("//div[@class='flex--item']//a[contains(@href, '" + tag + "')]")
        tag.click()

    def open_filter_options(self):
        """
        click btn to open filter options
        :return: None
        """
        filter_ele = self.driver.find_element_by_xpath(Locators.filter_btn)
        filter_ele.click()

    def select_and_apply_filter(self):
        """
        select most frequent radio btn and apply filter
        :return: None
        """
        self.driver.find_element_by_xpath(Locators.sort_by_most_frequent_radio_btn).click()
        self.driver.find_element_by_xpath(Locators.apply_filter_btn).click()

    def find_highest_vote(self, votes):
        """
        get all votes, convert to ints and sort descending
        :return: highest value from sorted list
        """
        values = []
        [values.append(int(vote.text)) for vote in votes]
        sorted_values = sorted(values, reverse=True)
        return sorted_values[0]

    def click_question_with_highest_votes(self):
        """
        get highest vote value to find and click on corresponding question.
        retrieve id from highest voted question element and use stripped id value as locator.
        :return: None
        """
        votes = self.driver.find_elements_by_xpath(Locators.question_votes)
        highest_vote = self.find_highest_vote(votes)
        highest_voted_question = self.driver.find_element_by_xpath("//div[@class='question-summary' "
                                                                   "and contains(., '" + str(highest_vote) + "')]")
        question_id = highest_voted_question.get_attribute('id')
        value = "".join(question_id.split("-", -1)[-1:])
        highest = self.driver.find_element_by_xpath("//div[@class='question-summary' "
                                                    "and contains(., '" + str(highest_vote) + "')]//div[@class='summary"
                                                                                              "']//a[contains(@href, "
                                                                                              "'" + value + "')]")
        highest.click()

    def get_author_highest_voted_answer(self):
        """
        find answer with highest number of votes and print the author
        :return: None
        """
        votes = self.driver.find_elements_by_xpath(Locators.answer_votes)
        highest_number = self.find_highest_vote(votes)
        post = self.driver.find_element_by_xpath(
            "//div[@class='post-layout' and contains(., '" + str(highest_number) + "')]//span[@itemprop='name']")
        author = post.get_attribute('innerText')
        print('The author of the highest voted answer is {0}'.format(author))
