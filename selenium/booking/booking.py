import booking.constants as const
import os
from selenium import webdriver
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
from prettytable import PrettyTable

class Booking(webdriver.Chrome):
  def __init__(self, driver_path=r"PathToSeleniumDriver", teardown=False):
    self.driver_path = driver_path
    #os.environ['PATH'] += self.driver_path
    self.teardown = teardown
    super(Booking, self).__init__()
    self.implicitly_wait(15) # wait up to 15 seconds for url page loading
    self.maximize_window()

  #def __exit__(self, exc_type, exc_val, exc_tn):
  def __exit__(self, *args) -> None:
    if self.teardown:
      self.quit()
    #return super().__exit__(*args)  # will destroy the webdrive window
    return
      
  def land_first_page(self):
    self.get(const.BASE_URL)

  def change_currency(self, currency=None):
    currency_element = self.find_element_by_css_selector(
      'button[data-tooltip-text="Choose your currency"]'
    )
    print(currency_element.text)
    currency_element.click()

    selected_currency_element = self.find_element_by_css_selector(
      f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
    )
    print(selected_currency_element.text)
    selected_currency_element.click()

  def select_place_to_go(self, place_to_go):
    search_field = self.find_element_by_id('ss')
    search_field.clear()  # remove the existing text
    search_field.send_keys(place_to_go)

    first_result = self.find_element_by_css_selector(
      'li[data-i="0"]'
    )
    first_result.click()

  def select_dates(self, check_in_date, check_out_date):
    check_in_element = self.find_element_by_css_selector(
      f'td[data-date="{check_in_date}"]'
    )
    check_in_element.click()

    check_out_element = self.find_element_by_css_selector(
      f'td[data-date="{check_out_date}"]'
    )
    check_out_element.click()

  def select_adults(self, count=1):
    selection_element = self.find_element_by_id("xp__guests__toggle")
    selection_element.click()

    decrease_adults_element = self.find_element_by_css_selector(
      'button[aria-label="Decrease number of Adults"]'
    )
    increase_adults_element = self.find_element_by_css_selector(
      'button[aria-label="Increase number of Adults"]'
    )
    adults_value_element = self.find_element_by_id("group_adults")
    # default adult count, get_attribute returns a string
    adults_value = adults_value_element.get_attribute('value') 
    print("default adult count: " + adults_value)

    default_cnt = int(adults_value)
    clicks = count - default_cnt
    print("adults default: {}, count: {}".format(str(default_cnt), str(count)))
    if clicks > 0:
      print("Increase clicks: {}".format(str(clicks)))
      for _ in range(clicks): # _ is a variable place holder
        increase_adults_element.click()
    elif clicks < 0:
      print("Decrease clicks: {}".format(str(default_cnt-count)))
      for _ in range(default_cnt-count):
        decrease_adults_element.click()
    else:
      print("Adults Count: No Change")

  def click_search(self):
    #search_button = self.find_element_by_css_selector('button[type="submit"]')
    search_button = self.find_element_by_css_selector('button[class="sb-searchbox__button "]')
    search_button.click()

  def apply_filtrations(self):
    filtration = BookingFiltration(driver=self)
    filtration.apply_star_rating(3,4,5)

    filtration.sort_price_lowest_first()

  def report_results(self):
    #hotel_boxes = self.find_element_by_id(
    #  'hotellist_inner'
    #  ).find_elements_by_class_name('sr_property_block')

    hotels_section_element = self.find_element_by_id('hotellist_inner')

    report = BookingReport(hotels_section_element)
    table = PrettyTable(field_names=["Hotel Name", "Hotel Price", "Hotel Rating"])
    table.add_rows(report.pull_deal_box_attributes())  # a list of lists
    print(table)
    
