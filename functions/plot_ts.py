import yfinance as yf
import plotly.express as px

def plot(ticker:str):
    """
    Plot a time series

    args:
        ticker(str): the company ticker.

    return:
        A plotly ticker chart
    """
    data = yf.download(ticker, period='1y', multi_level_index=False)
    df = data.reset_index()[['Date', 'Close']]
    figure = px.line(df, x="Date", y="Close", title=f"{ticker} MARKET DATA")
    return figure