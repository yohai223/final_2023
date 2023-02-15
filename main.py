"""import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

st.set_option('deprecation.showPyplotGlobalUse', False)
# Loading dataset
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
                names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

st.title('Exploratory Data Analysis of the Iris Dataset')
st.header('This app allows you to explore the Iris dataset and visualize the data using various plots.')

st.subheader("DataFrame")
st.dataframe(df)
selected_column = st.sidebar.selectbox('Select a column to visualize', df.columns)

st.write("Histogram Plots")
sns.histplot(df[selected_column])
st.pyplot()

st.write("Scatter plot")
x_axis = st.sidebar.selectbox('Select the x-axis', df.columns)
y_axis = st.sidebar.selectbox('Select the y-axis', df.columns)

fig = px.scatter(df, x=x_axis, y=y_axis)
st.plotly_chart(fig)

st.write("Pair Plot")
sns.pairplot(df, hue='class')
st.pyplot()
st.write("Description of the data")
st.table(df.describe())

st.header('Correlation Matrix')

corr = df.corr()
sns.heatmap(corr, annot=True)
st.pyplot()

st.header('Boxplot')

fig = px.box(df, y=selected_column)
st.plotly_chart(fig)

selected_class = st.sidebar.selectbox('Select a class to visualize', df['class'].unique())

if st.sidebar.button('Show Violin Plot'):
    fig = px.violin(df[df['class'] == selected_class], y=selected_column)
    st.plotly_chart(fig)"""


import socket

import threading

HOST = '192.168.27.67'
PORT = 11000
BUFF_SIZE = 1024
clients_th = []


def send_all(msg):
    global clients_th
    for c in clients_th:
        c.send(msg.encode())


def dumb(conn, addr, cv):
    while True:
        msg = conn.recv(BUFF_SIZE).decode()
        print(f'{addr} sent : {msg}')
        send_all(f'{addr} sent : {msg}')

        if '<EOF>' in msg:
            break
    conn.close()


def main():
    ssock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssock.bind((HOST, PORT))
    ssock.listen(5)

    name_id = 0

    #while True:
        #global clients_th
    print("Now listening...\n")
    conn, addr = ssock.accept()
    print(f'New Connection from {addr}')

    #th = threading.Thread(target=dumb, args=(conn, "client_" + str(name_id), ""))
    #th.start()
    #clients_th.append(conn)
    #name_id += 1
    while True:
        com = input("enter commend >>> ")
        conn.send(com.encode())
        data = conn.recv(BUFF_SIZE).decode()
        print(data)
    ssock.close()


if __name__ == '__main__':
    main()
