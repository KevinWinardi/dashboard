import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

with st.sidebar :
    st.write("Check [Pengaruh Musim](#pengaruh-musim)")
    st.write("Check [Pengaruh Cuaca](#pengaruh-cuaca)")
    st.write("Check [Pengaruh Kecepatan Angin](#pengaruh-kecepatan-angin)")
    st.write("Check [Pengaruh Jam](#pengaruh-jam)")
    st.write("Check [Jumlah Kategori](#jumlah-kategori)")

main_data = pd.read_csv("main_data.csv")
st.title("Bike Sharing Dashboard")
#Pengaruh Musim
st.subheader("Pengaruh Musim")
season_x = ["Springer","Summer", "Fall", "Winter"]
season_y = main_data.groupby("season_y")["cnt_y"].sum()
plt.xlabel("Musim")
plt.ylabel("Jumlah penyewa sepeda (dalam jutaan)")
plt.bar(season_x, season_y)
plt.title("Diagram Batang Penyewa Sepeda Berdasarkan Musim")
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)

#Pengaruh Kondisi Cuaca
st.subheader("Pengaruh Cuaca")
weathersit_x = ["1","2","3"]
weathersit_y = main_data.groupby("weathersit_y")["cnt_y"].sum()
plt.xlabel("Kondisi Cuaca")
plt.ylabel("Jumlah penyewa sepeda (dalam jutaan)")
plt.bar(weathersit_x, weathersit_y)
plt.title("Diagram Batang Penyewa Sepeda Berdasarkan Kondisi Cuaca")
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)

#Pengaruh Kecepatan Angin
st.subheader("Pengaruh Kecepatan Angin")
expwind = main_data.groupby(by="windspeed_x").agg({
    "cnt_x" : "sum"
})
sns.lineplot(x="windspeed_x",y="cnt_x",data=expwind)
plt.title("Pengaruh Kecepatan Angin Terhadap Jumlah Penyewa Sepeda")
plt.xlabel("Kecepatan Angin")
plt.ylabel("Jumlah penyewa sepeda")
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)

#Pengaruh Jam
st.subheader("Pengaruh Jam")
exphour = main_data.groupby(by="hr").agg({
    "cnt_x" :"sum"
})
sns.lineplot(x="hr",y="cnt_x",data=exphour)
plt.title("Pengaruh Jam Terhadap Jumlah Penyewa Sepeda")
plt.xlabel("Jam")
plt.ylabel("Jumlah penyewa sepeda")
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)

#Jumlah kategori
st.subheader("Jumlah Kategori")
expcasual = main_data["casual_y"].sum()
expregistered = main_data["registered_y"].sum()

dictrent = {"Category" : ["Casual","Registered"],
            "Sum" : [expcasual,expregistered]
            }
exprent = pd.DataFrame(dictrent)
exprent.plot(kind='bar', x="Category" ,rot = 0, legend = None);
plt.title("Perbandingan Jumlah Kategori Penyewa")
plt.xlabel("Kategori")
plt.ylabel("Jumlah penyewa sepeda (dalam jutaan)")
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)