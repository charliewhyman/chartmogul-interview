import os
import chartmogul

#store API key using environment variable
api_key = os.environ['CHARTMOGUL_KEY']

#choose parameters for MRR data request
selected_start_date = '2019-01-01'
selected_end_date = '2019-04-30'
selected_interval = 'month'

#using enhanced API Access Management, as described in https://dev.chartmogul.com/docs/authentication
config = chartmogul.Config(api_key, api_key)

#test against the ping endpoint
print(chartmogul.Ping.ping(config).get())

#retrieve MRR data for the chosen parameters
metrics = chartmogul.Metrics.mrr(config,
                       start_date=selected_start_date,
                       end_date=selected_end_date,
                       interval=selected_interval).get()

print(metrics.entries)

for entry in metrics.entries:
    print(entry.date)