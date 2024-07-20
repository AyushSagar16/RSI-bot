# RSI Stock Trading With Back-testing Capabilities
from alpha_vantage.timeseries import TimeSeries
import yfinance as yf
ts = TimeSeries(key='')
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('GOOGL')

periods = ["minutes", "hours"]


msft = yf.Ticker("MSFT")

# get all stock info
information = msft.info
hist = msft.history(period="1mo")
print(hist)

