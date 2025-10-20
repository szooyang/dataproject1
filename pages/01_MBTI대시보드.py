import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.colors import sample_colorscale

# 페이지 설정
st.set_page_config(page_title="MBTI by Country", page_icon="🌍", layout="wide")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

st.title("🌍 세계 각국의 MBTI 유형 비율 시각화")
st.markdown("**국가를 선택하면 MBTI 16유형의 비율을 인터랙티브 그래프로 볼 수 있어요!**")

# 국가 선택
countries = sorted(df["Country"].unique())
selected_country = st.selectbox("국가를 선택하세요:", countries)

# 선택한 국가의 데이터만 추출
country_data = df[df["Country"] == selected_country].iloc[0, 1:]  # Country 제외
country_df = pd.DataFrame({
    "MBTI": country_data.index,
    "비율": country_data.values
}).sort_values(by="비율", ascending=False)

# 색상 설정 (1등은 빨강, 나머지는 파랑계열 그라데이션)
gradient_colors = sample_colorscale("Blues", [i/15 for i in range(15)])
colors = ['#FF4C4C'] + gradient_colors  # 1등 빨강 추가
country_df["색상"] = colors[:len(country_df)]

# Plotly 그래프 생성
fig = px.bar(
    country_df,
    x="MBTI",
    y="비율",
    text=country_df["비율"].apply(lambda x: f"{x:.2%}"),
    color="색상",
    color_discrete_sequence=country_df["색상"],
)

# 그래프 꾸미기
fig.update_traces(
    textposition="outside",
    hovertemplate="<b>%{x}</b><br>비율: %{y:.2%}<extra></extra>"
)
fig.update_layout(
    title=f"🇨🇭 {selected_country}의 MBTI 유형 비율",
    xaxis_title="MBTI 유형",
    yaxis_title="비율",
    showlegend=False,
    template="simple_white"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.caption("데이터 출처: MBTI 16types by Country CSV | 시각화: Streamlit + Plotly 💫")
