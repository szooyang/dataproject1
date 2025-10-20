import streamlit as st

st.set_page_config(page_title="MBTI 진로 추천기 💡", page_icon="🎯")

st.title("🎯 MBTI로 알아보는 나의 진로 추천기 💬")
st.write("너의 MBTI를 골라봐! 그 유형에 어울리는 진로를 추천해줄게 😎")

mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

mbti = st.selectbox("👉 MBTI를 선택해줘!", mbti_list)

careers = {
    "INTJ": [
        {"job": "데이터 분석가 📊", 
         "major": "통계학, 컴퓨터공학, 산업공학 등",
         "fit": "논리적이고 체계적인 사람! 혼자 몰두하는 걸 좋아하는 타입에게 딱이야 🔍"},
        {"job": "전략기획자 🧠",
         "major": "경영학, 경제학, 행정학 등",
         "fit": "큰 그림을 그리는 걸 좋아하고 계획 세우는 걸 즐기는 사람에게 어울려!"}
    ],
    "INFP": [
        {"job": "작가 ✍️",
         "major": "문예창작, 국어국문, 철학 등",
         "fit": "감수성이 풍부하고 자기 생각을 글로 표현하는 걸 좋아하는 사람에게 좋아 💫"},
        {"job": "상담사 💬",
         "major": "심리학, 사회복지학 등",
         "fit": "다른 사람의 이야기를 공감하고 도와주는 걸 좋아하는 사람에게 찰떡!"}
    ],
    "ENFP": [
        {"job": "마케팅 기획자 📢",
         "major": "광고홍보학, 경영학 등",
         "fit": "창의력 넘치고 새로운 아이디어를 내는 걸 좋아하는 사람에게 어울려 💡"},
        {"job": "이벤트 플래너 🎉",
         "major": "호텔관광학, 문화콘텐츠학 등",
         "fit": "활발하고 사람 만나는 걸 좋아하는 성격이면 딱이야!"}
    ],
    "ISTJ": [
        {"job": "공무원 🏛️",
         "major": "행정학, 법학 등",
         "fit": "책임감 있고 계획적으로 일하는 걸 좋아하는 사람에게 잘 맞아 ✅"},
        {"job": "회계사 💼",
         "major": "회계학, 경영학 등",
         "fit": "세세한 걸 꼼꼼히 챙기고 숫자 감각이 좋은 사람에게 추천해!"}
    ],
    "ESFP": [
        {"job": "연예기획자 🎤",
         "major": "미디어커뮤니케이션, 공연예술 등",
         "fit": "사람을 좋아하고 분위기를 띄우는 데 자신 있는 사람에게 완전 찰떡 ✨"},
        {"job": "관광 가이드 🗺️",
         "major": "관광경영학, 국제관광학 등",
         "fit": "활발하고 이야기 잘하는 성격이라면 완전 잘 어울려 😁"}
    ]
}

if mbti:
    st.subheader(f"🌟 {mbti} 유형에게 어울리는 진로는 바로...")
    if mbti in careers:
        for c in careers[mbti]:
            st.markdown(f"### {c['job']}")
            st.markdown(f"**관련 학과:** {c['major']}")
            st.markdown(f"**이런 성격이라면 잘 맞아요:** {c['fit']}")
            st.markdown("---")
    else:
        st.info("앗! 아직 이 MBTI에 대한 데이터가 부족해 😅 다음 업데이트를 기대해줘!")
