import os
import chartmogul

api_key = os.environ['CHARTMOGUL_KEY']
#store API key using environment variable

config = chartmogul.Config(api_key, api_key)
#using enhanced API Access Management, as described in https://dev.chartmogul.com/docs/authentication

print(chartmogul.Ping.ping(config).get())
#test against the ping endpoint