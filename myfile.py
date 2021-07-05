import yfinance as yf
import streamlit as st

st.write("""
# Accurate Stock Price (USD)
Shown are the stock **closing price** and ***volume**
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = st.text_input("ENTER TICK SYMBOL E.G AAPL FOR APPLE")
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
x = st.text_input("ENTER PERIOD(Day) E.G 1d")
y = st.text_input("ENTER START DATE E.G 2010-5-31")
z = st.text_input("ENTER END DATE E.G 2020-5-31")
tickerDf = tickerData.history(period= x, start= y, end= z)
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.write("""
## **Closing Price**
""")
st.line_chart(tickerDf.Close)
st.write("""
## **Volume Price**
""")
st.line_chart(tickerDf.Volume)
st.write("""
### Email woohoufeng@gmail.com for a FREE in depth analysis report
""")
