import streamlit as st

from functions.plot_ts import plot

def printTicker(ticker):
    st.plotly_chart(plot(ticker))

st.title("Histórico de cotações")
st.write("Veja o histórico das cotações")
ticker = st.sidebar.text_input("Escolha o ticker: ", value="AAPL")
st.sidebar.button(label="procurar", on_click=printTicker(ticker))
