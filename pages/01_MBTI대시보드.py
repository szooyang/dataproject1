import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.colors import sample_colorscale

# 페이지 설정
st.set_page_config(page_title="MBTI Global Dashboard", page_icon="🌍", layout="wide")

# 데이터 불러오기
@st.cache_data
def load_data():
    return pd.read_csv("countriesMBTI_16types.csv")

df = load_data()

st.title("🌍 세계 각국의 MBTI 유형 비율 대시보드")
st.markdown("국가별 MBTI 분포와 유형별 글로벌 경향을 한눈에 확인하세요 👀")

# 탭 구분
tab1, tab2 = st.tabs(["📊 국가별 MBTI 비율", "📈 유형별 글로벌 비율"])

# ------------------------- TAB 1: 국가별 MBTI 막대 그래프 -------------------------
with tab1:
    st.subheader("📍 국가별 MBTI 유형 비율")
    country = st.selectbox("국가를 선택하세요:", sorted(df["Country"].unique()))

    # 선택된 국가의 데이터 추출
    country_data = df[df["Country"] == country].iloc[0, 1:]
    country_df = pd.DataFrame({
        "MBTI": country_data.index,
        "비율": country_data.values
    }).sort_values(by="비율", ascending=False)

    # 색상 (1등: 빨강, 나머지: 파랑계열 그라데이션)
    gradient_colors = sample_colorscale("Blues", [i / 15 for i in range(15)])
    colors = ['#FF4C4C'] + gradient_colors  # 1등 빨강
    country_df["색상"] = colors[:len(country_df)]

    # 그래프 생성
    fig_bar = px.bar(
        country_df,
        x="MBTI",
        y="비율",
        text=country_df["비율"].apply(lambda x: f"{x:.2%}"),
        color="색상",
        color_discrete_sequence=country_df["색상"],
    )

    fig_bar.update_traces(
        textposition="outside",
        hovertemplate="<b>%{x}</b><br>비율: %{y:.2%}<extra></extra>"
    )
    fig_bar.update_layout(
        title=f"🇨🇭 {country}의 MBTI 유형 비율",
        xaxis_title="MBTI 유형",
        yaxis_title="비율",
        showlegend=False,
        template="simple_white",
        height=550
    )

    st.plotly_chart(fig_bar, use_container_width=True)
    st.markdown("---")
    st.caption("1등은 빨간색, 나머지는 파랑계열 그라데이션으로 표시됩니다 🎨")

# ------------------------- TAB 2: 유형별 글로벌 꺾은선 그래프 -------------------------
with tab2:
    st.subheader("🌐 유형별 국가별 비율 비교")
    mbti_types = [col for col in df.columns if col != "Country"]
    mbti_selected = st.selectbox("MBTI 유형을 선택하세요:", mbti_types)

    # 해당 유형의 데이터 추출
    type_df = df[["Country", mbti_selected]].sort_values(by=mbti_selected, ascending=False)

    fig_line = px.line(
        type_df,
        x="Country",
        y=mbti_selected,
        markers=True,
        line_shape="spline",
    )

    fig_line.update_traces(
        hovertemplate=f"<b>%{{x}}</b><br>{mbti_selected} 비율: %{{y:.2%}}<extra></extra>",
        line=dict(color="#FF6B6B", width=3)
    )
    fig_line.update_layout(
        title=f"{mbti_selected} 유형의 국가별 비율 비교",
        xaxis_title="국가",
        yaxis_title="비율",
        template="simple_white",
        height=550
    )

    st.plotly_chart(fig_line, use_container_width=True)
    st.markdown("---")
    st.caption("국가별 MBTI 유형 비율을 꺾은선 그래프로 확인할 수 있습니다 📈")
