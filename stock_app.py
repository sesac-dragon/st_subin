from sqlalchemy import create_engine
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


engine = create_engine('sqlite:///stocks.db')

# load_data

def load_data():
    with engine.connect() as conn:
        query = "SELECT * FROM stocks LIMIT 300"
        return pd.read_sql(query, conn)
    
data = load_data()
# st.write(data)


st.title('Real-Time Stock Dashboard')

cols = st.columns(3)
with cols[0]:
    st.metric('Latest Price', f"$ {data['price'].iloc[-1]:.2f}")

with cols[1]:
    st.metric('Latest Volume', f"{data['volume'].iloc[-1]}" )

with cols[2]:
    st.metric('Price Change', f"${data['price'].iloc[-1] - data['price'].iloc[-2]:.2f}", f"{data['price'].iloc[-1] - data['price'].iloc[-2]:.2f}" )
    st.metric('Volume Change', f"{data['volume'].iloc[-1] - data['volume'].iloc[-2]}", f"{data['volume'].iloc[-1] - data['volume'].iloc[-2]}" )
 

st.write('Stock Price and Volume')

fig = make_subplots(rows=2, cols=1)

fig.add_trace(
    go.Scatter(x = data['timestamp'], y = data['price'], line=dict(color='blue')),
    row=1, col=1
)
fig.add_trace(
    go.Bar(x = data['timestamp'], y = data['volume'], marker=dict(color='orange')),
    row=2, col=1
)

fig.update_layout(title_text="Stock Price & Volume",
                  yaxis_title="Price",
                  yaxis2_title="Volume")
fig.update_xaxes(showticklabels=False, row=1, col=1)

st.plotly_chart(fig)

# st.selectbox(data.columns)