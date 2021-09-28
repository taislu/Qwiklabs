#! /usr/bin/env python3

from booking.booking import Booking

try:
  with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='USD')
    #bot.change_currency(currency='GBP')

    bot.select_place_to_go('New York')
    #bot.select_place_to_go(input("Where do you want to go?"))
    bot.select_dates(check_in_date='2021-09-30', check_out_date='2021-10-02')
    bot.select_adults(10)
    #bot.select_adults(2)
    #bot.select_adults(1)

    bot.click_search()
    bot.apply_filtrations()
    bot.refresh() # refresh the page before pull the data for report
    
    bot.report_results()

    print('Exiting ....')
  # here will call __exit__()
except Exception as e:
  print("Error: " + str(e))


#inst = Booking()
#inst.land_first_page()