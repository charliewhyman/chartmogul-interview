import os
import chartmogul
import datetime
from calendar import monthrange

#store API key using environment variable
api_key = os.environ['CHARTMOGUL_KEY']

#choose parameters for MRR data request
selected_interval = 'month'

#chose reporting quarter to obtain MRR for
selected_year = 2021
selected_quarter = 3

#calculate start and end dates of selected quarter
first_month_of_quarter = 3 * selected_quarter - 2
last_month_of_quarter = 3 * selected_quarter
date_of_first_day_of_quarter = datetime.date(selected_year, first_month_of_quarter, 1)
date_of_last_day_of_quarter = datetime.date(selected_year, last_month_of_quarter, monthrange(selected_year, last_month_of_quarter)[1])

#using enhanced API Access Management, as described in https://dev.chartmogul.com/docs/authentication
config = chartmogul.Config(api_key, api_key)

#retrieve MRR data for the chosen parameters
metrics = chartmogul.Metrics.mrr(config,
                       start_date=date_of_first_day_of_quarter,
                       end_date=date_of_last_day_of_quarter,
                       interval=selected_interval).get()

print('Total MRR for Q'+str(selected_quarter)+' '+str(selected_year)+': ')

for entry in metrics.entries:
    date = entry.date
    mrr_dollars = (entry.mrr)/100
    print(date.strftime('%B'), mrr_dollars)