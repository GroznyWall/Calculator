import streamlit as st

# НАСТРОЙКА СТРАНИЦЫ (Пишется строго в самом верху кода!)
st.set_page_config(
    page_title="Мой Супер Калькулятор",  # Название вкладки в браузере
    page_icon="🧮",  # Иконка вкладки (можно вставить любой эмодзи)
    layout="centered"  # Выравнивание контента по центру
)

# Дальше идет твой обычный код
st.title("🧮 Мой красивый калькулятор")
st.write("Этот сайт сделан полностью на чистом Python!")
st.write("Примечание оставьте английский в ином случае в место привычного посчитать будет бред")

with st.container(border=True):
    num1 = st.number_input("Введите первое число", value=0.0, step=1.0)
    # Вместо обычного st.selectbox:
    operator = st.sidebar.selectbox("Выберите операцию", ["+", "-", "*", "/"])

    num2 = st.number_input("Введите второе число", value=0.0, step=1.0)

    if st.button("Посчитать", type="primary"):
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                result = "Ошибка: деление на ноль!"
            else:
                result = num1 / num2

        st.success(f"Результат: {result}")
