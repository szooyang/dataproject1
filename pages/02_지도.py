# main.py
import streamlit as st
from streamlit_folium import st_folium
import folium
from folium.plugins import MarkerCluster

st.set_page_config(page_title="Seoul Top10 (For Foreign Visitors) 🌏", layout="wide")

st.title("외국인이 좋아하는 서울 주요 관광지 Top 10 📍")
st.markdown("지도에서 마커를 클릭하면 간단한 설명과 추천 방문시간을 볼 수 있어요. 즐겁게 둘러봐~ 😊")

# Top10 장소 데이터 (이름, 위도, 경도, 짧은 설명)
places = [
    {
        "name": "Gyeongbokgung Palace (경복궁)",
        "lat": 37.580467,
        "lon": 126.976944,
        "desc": "조선의 대표 궁궐. 오전에 경복궁 및 수문장 교대식을 보는 걸 추천해요. ⏰ 09:00~17:00(시즌별 다름)."
    },
    {
        "name": "N Seoul Tower (N서울타워, 남산)",
        "lat": 37.551170,
        "lon": 126.988228,
        "desc": "서울 시내를 한눈에 내려다볼 수 있는 전망대. 야경이 특히 예뻐요. 🌃"
    },
    {
        "name": "Bukchon Hanok Village (북촌한옥마을)",
        "lat": 37.58218,
        "lon": 126.98326,
        "desc": "한옥 골목 산책. 사진 찍기 좋은 장소. 주민 생활 존중해 주세요. 📸"
    },
    {
        "name": "Myeongdong (명동 쇼핑거리)",
        "lat": 37.55998,
        "lon": 126.98583,
        "desc": "화장품·패션 쇼핑 천국. 길거리 음식도 꼭 맛보세요. 🍢"
    },
    {
        "name": "Dongdaemun Design Plaza (DDP, 동대문디자인플라자)",
        "lat": 37.56652,
        "lon": 127.00911,
        "desc": "현대적 건축+야간 조명이 인상적. 패션·디자인 관련 행사 자주 열림. 🏙️"
    },
    {
        "name": "Hongdae (홍대, 홍익대입구)",
        "lat": 37.55528,
        "lon": 126.92333,
        "desc": "젊음의 거리, 스트리트 공연·카페·클럽이 많아요. 저녁 분위기 굿! 🎶"
    },
    {
        "name": "Insadong (인사동)",
        "lat": 37.574165,
        "lon": 126.98491,
        "desc": "전통 기념품·찻집 많은 골목. 한국 전통 느낌을 찾는다면 여기! 🍵"
    },
    {
        "name": "Changdeokgung Palace (창덕궁)",
        "lat": 37.57925,
        "lon": 126.99215,
        "desc": "세계문화유산으로 지정된 궁궐. 후원이 유명하니 시간 맞춰 투어 추천. 🌳"
    },
    {
        "name": "Lotte World Tower (롯데월드타워 / 잠실)",
        "lat": 37.51250,
        "lon": 127.10278,
        "desc": "초고층 전망대와 쇼핑몰, 아쿠아리움 등 한 번에 즐길 수 있는 복합시설. 🏢"
    },
    {
        "name": "Itaewon (이태원)",
        "lat": 37.53499,
        "lon": 126.99003,
        "desc": "다국적 음식과 외국인 친화적 상점이 많은 동네. 밤에도 활기찬 편. 🌎"
    }
]

# 기본 중심 좌표와 줌레벨
center_lat = 37.56
center_lon = 126.98
m = folium.Map(location=[center_lat, center_lon], zoom_start=12, control_scale=True)

# 마커 클러스터
cluster = MarkerCluster().add_to(m)

for p in places:
    popup_html = f"<b>{p['name']}</b><br>{p['desc']}"
    folium.Marker(
        location=[p["lat"], p["lon"]],
        popup=folium.Popup(popup_html, max_width=300),
        tooltip=p["name"],
        icon=folium.Icon(icon="map-marker", prefix="fa")
    ).add_to(cluster)

# 사이드바 옵션
st.sidebar.header("옵션")
if st.sidebar.checkbox("지도 타입: 위성 보기 (Folium Tile 변경)", value=False):
    # 위성 타일 레이어 추가
    folium.TileLayer('Stamen Terrain').add_to(m)

st.sidebar.markdown("※ 마커를 클릭하면 간단 설명이 나와요. 즐거운 여행 계획 되길! ✈️")

# 렌더링
st.subheader("서울 Top10 지도")
st_data = st_folium(m, width=1100, height=700)

# 장소 목록(클릭 가능한 간단 리스트)
st.subheader("장소 목록")
for i, p in enumerate(places, start=1):
    st.markdown(f"**{i}. {p['name']}** — {p['desc']}")

st.caption("앱 제작: Streamlit + Folium (streamlit-folium) — 좌표 출처는 아래 참고.")
