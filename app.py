import streamlit as st

st.title("作業報告アプリ")

name = st.text_input("名前を入力してください")
task = st.text_input("今日の作業内容は？")
time = st.number_input("所要時間（時間）", min_value=0.0, step=0.25)

if st.button("送信"):
    st.success(f"{name}さんの作業「{task}」を記録しました！（{time}時間）")