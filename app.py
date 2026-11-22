import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(page_title="오늘의 점심 추천기", page_icon="🍱")

# 앱 제목 및 설명
st.title("🍱 오늘의 점심 메뉴 추천")
st.write("무엇을 먹을지 고민되시나요? 아래 버튼을 눌러 오늘의 메뉴를 정해보세요!")

# 점심 메뉴 리스트 (원하는 메뉴를 자유롭게 추가하거나 수정하세요)
lunch_menus = [
    "김치찌개", "된장찌개", "제육볶음", "돈가스", 
    "비빔밥", "짜장면", "짬뽕", "탕수육", 
    "초밥", "라멘", "우동", "파스타", 
    "햄버거", "샌드위치", "국밥", "쌀국수",
    "떡볶이", "마라탕", "부대찌개", "칼국수"
]

# 버튼을 눌렀을 때 실행될 동작
if st.button("🎲 오늘의 점심 뽑기!", type="primary"):
    # 리스트에서 랜덤으로 1개 선택
    selected_menu = random.choice(lunch_menus)
    
    # 결과 출력 및 축하 효과
    st.success(f"오늘의 추천 메뉴는 **{selected_menu}**입니다! 맛있게 드세요! 😋")
    st.balloons()
