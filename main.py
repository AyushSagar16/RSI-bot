# RSI Stock Trading With Back-testing Capabilities
from alpha_vantage.timeseries import TimeSeries
import yfinance as yf
ts = TimeSeries(key='')
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('GOOGL')
#RSI = 100 – [100 ÷ ( 1 + (Average Gain During Up Periods ÷ Average Loss During Down Periods ))]

periods = ["minutes", "hours"]


msft = yf.Ticker("MSFT")

# get all stock info
information = msft.info
hist = msft.history(period="1mo")
print(type(hist))

class RSI():
    # This class will be used to get the RSI of different stocks and it will probably be only one method big
    def __init__(self, stockName):
        self.sName = stockName

    def getPrice(self):
        return price

