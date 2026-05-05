import requests
import streamlit as st
import os
API_KEY ="a28fdaaede7bbebbf0ba557001b892c2"


st.set_page_config(
    page_title='國際氣候資料中心',
    page_icon='🌍'
)
c='none'
st.title('國際氣候資料中心')
st.header('全球氣候數據整合與分析平台')
st.info('請在以下欄位選擇一個國家以開始進行查詢')
c = st.selectbox('國家', ['馬來西亞', '英國', '中華民國','韓國','日本','北韓','印度','新加坡','印尼','越南','土耳其'])
# data of the city
singapore_cities = [
    "Singapore,SG"
]
my_cities = [
    "Kuala Lumpur,MY",
    "George Town,MY",
    "Johor Bahru,MY",
    "Ipoh,MY",
    "Shah Alam,MY",
    "Petaling Jaya,MY",
    "Subang Jaya,MY",
    "Malacca,MY",
    "Kota Kinabalu,MY",
    "Kuching,MY",
    "Alor Setar,MY",
    "Seremban,MY",
    "Kuantan,MY",
    "Miri,MY",
    "Sungai Petani,MY",
    "Klang,MY",
    "Sandakan,MY",
    "Bintulu,MY",
    "Taiping,MY",
    "Putrajaya,MY"
]

uk_cities = [
    "London,GB",
    "Birmingham,GB",
    "Manchester,GB",
    "Liverpool,GB",
    "Leeds,GB",
    "Sheffield,GB",
    "Bristol,GB",
    "Glasgow,GB",
    "Edinburgh,GB",
    "Cardiff,GB",
    "Newcastle,GB",
    "Nottingham,GB",
    "Leicester,GB",
    "Coventry,GB",
    "Hull,GB",
    "Southampton,GB",
    "Portsmouth,GB",
    "Derby,GB",
    "Brighton,GB",
    "Oxford,GB",
    "Cambridge,GB",
    "York,GB",
    "Norwich,GB",
    "Exeter,GB",
    "Plymouth,GB",
    "Swansea,GB",
    "Aberdeen,GB",
    "Dundee,GB",
    "Stoke-on-Trent,GB",
    "Bradford,GB"
]

jp_city = [
    "Tokyo,JP",
    "Osaka,JP",
    "Kyoto,JP",
    "Yokohama,JP",
    "Nagoya,JP",
    "Sapporo,JP",
    "Kobe,JP",
    "Fukuoka,JP",
    "Hiroshima,JP",
    "Sendai,JP",
    "Kawasaki,JP",
    "Chiba,JP",
    "Saitama,JP",
    "Naha,JP",
    "Kitakyushu,JP",
    "Okayama,JP",
    "Niigata,JP",
    "Shizuoka,JP",
    "Kumamoto,JP",
    "Kanazawa,JP"
]

kr_cities = [
    "Seoul,KR",
    "Busan,KR",
    "Incheon,KR",
    "Daegu,KR",
    "Daejeon,KR",
    "Gwangju,KR",
    "Suwon,KR",
    "Ulsan,KR",
    "Changwon,KR",
    "Seongnam,KR",
    "Goyang,KR",
    "Yongin,KR",
    "Bucheon,KR",
    "Ansan,KR",
    "Jeju,KR",
    "Cheongju,KR",
    "Jeonju,KR",
    "Pohang,KR",
    "Gimhae,KR",
    "Chuncheon,KR"
]
taiwan_regions = [
    "Taipei City",
    "New Taipei City",
    "Taoyuan City",
    "Taichung City",
    "Tainan City",
    "Kaohsiung City",
    "Keelung City",
    "Hsinchu City",
    "Chiayi City",
    "Yilan County",
    "Hsinchu County",
    "Miaoli County",
    "Changhua County",
    "Nantou County",
    "Yunlin County",
    "Chiayi County",
    "Pingtung County",
    "Taitung County",
    "Hualien County",
    "Penghu County",
    "Kinmen County",
    "Lienchiang County"
]
north_korea_cities = [
    "Pyongyang,KP",
    "Hamhung,KP",
    "Nampo,KP"
]
india_cities = [
    "New Delhi,IN",
    "Mumbai,IN",
    "Bangalore,IN",
    "Kolkata,IN",
    "Chennai,IN"
]
indonesia_cities = [
    "Jakarta,ID",
    "Surabaya,ID",
    "Bandung,ID",
    "Medan,ID"
]
vietnam_cities = [
    "Hanoi,VN",
    "Ho Chi Minh City,VN",
    "Da Nang,VN"
]
turkey_cities = [
    "Istanbul,TR",
    "Ankara,TR",
    "Izmir,TR"
]
def show_weather(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=zh_tw"
        res = requests.get(url, timeout=5)
        data = res.json()

        if str(data.get("cod")) != "200":
            st.warning(f"❌ {city} 查詢失敗：{data.get('message')}")
            return

        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]

        # ✅ 保持你原本一行一行輸出
        st.write(f"📍 城市：{city}")
        st.write(f"🌡 溫度：{temp} °C")
        st.write(f"☁️ 天氣：{weather}")
        st.write("----------------------------")

    except Exception as e:
        st.error(f"⚠️ {city} 發生錯誤：{e}")


if c == '馬來西亞':
    for city in my_cities:
        show_weather(city)

elif c == '英國':
    for city in uk_cities:
        show_weather(city)

elif c == '中華民國':
    for city in taiwan_regions:
        show_weather(city)
elif c == '韓國':
    for city in kr_cities:
        show_weather(city)
elif c == '日本':
    for city in jp_city:
        show_weather(city)
elif c == '北韓':
    for city in north_korea_cities:
        show_weather(city)
elif c == '印度':
    for city in india_cities:
        show_weather(city)
elif c == '新加坡':
    for city in singapore_cities:
        show_weather(city)
elif c == '印尼':
    for city in indonesia_cities:
        show_weather(city)
elif c == '越南':
    for city in vietnam_cities:
        show_weather(city)
elif c == '土耳其':
    for city in turkey_cities:
        show_weather(city)
