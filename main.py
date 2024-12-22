import random
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>Это главная страница!</h1>
    <a href="/namber/3">Причины</a><br>
    <a href="/namber/2">Я не знаю, что написать</a><br>
    <a href="/namber">Вторая страница</a><br>
    <a href="/news/1">Новости</a><br>
    <a href="/minus/12/10">Минус</a><br>
    <a href="/plus/7/5">Плюс</a><br>
    <a href="/divide/20/4">Деление</a><br>
    <a href="/coin">Подбросить монетку</a><br>
    <a href="/random/1/100">Случайное число</a><br>
    <a href="/reverse/hello">Обратный текст</a><br>
    <a href="/multiply/6/7">Умножение</a><br>
    <a href="/factorial/5">Факториал</a><br>
    <a href="/time">Текущее время</a><br>
    <a href="/encrypt/hello/3">Шифрование текста</a><br>
    <a href="/fibonacci/10">Фибоначчи</a><br>
    <a href="/prime/7">Проверка числа на простоту</a><br>
    """

# Простая страница
@app.route("/namber")
def namber_1():
    return "<h1>Это вторая страница</h1>"

@app.route("/namber/2")
def namber_2():
    return "<h1>Это третья страница</h1>"

@app.route("/namber/3")
def namber_3():
    reasons = [
        'игры', 'Социальные сети', 'Стриминговые платформы', 
        'Электронная коммерция', 'Виртуальные миры и метавселенные',
        'Азартные игры', 'Онлайн-знакомства', 'Программы для творчества'
    ]
    return f"<h1>Рандомная причина технологической зависимости: {random.choice(reasons)}</h1>"

@app.route("/news/<int:number>")
def news(number):
    return f"<h1>Вы смотрите новость под номером {number}</h1>"


@app.route('/plus/<int:a>/<int:b>')
def plus(a, b):
    result = a + b
    return f'<h1>Результат: {result}</h1>'

@app.route('/minus/<int:a>/<int:b>')
def minus(a, b):
    result = a - b
    return f'<h1>Результат: {result}</h1>'

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    result = a * b
    return f'<h1>Результат: {result}</h1>'

@app.route('/divide/<int:a>/<int:b>')
def divide(a, b):
    if b == 0:
        return "<h1>Деление на ноль невозможно!</h1>"
    result = a / b
    return f'<h1>Результат: {result}</h1>'

@app.route('/coin')
def coin():
    result = random.choice(["решка", "орёл 🦅"])
    return f"<h1>Выпало: {result}</h1>"

@app.route('/random/<int:start>/<int:end>')
def random_number(start, end):
    if start > end:
        return "<h1>Некорректный диапазон</h1>"
    number = random.randint(start, end)
    return f"<h1>Случайное число между {start} и {end}: {number}</h1>"

@app.route('/reverse/<string:text>')
def reverse_text(text):
    reversed_text = text[::-1]
    return f"<h1>Обратный текст: {reversed_text}</h1>"

@app.route('/factorial/<int:n>')
def factorial(n):
    if n < 0:
        return "<h1>Факториал определён только для неотрицательных чисел</h1>"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return f"<h1>Факториал {n}: {result}</h1>"

@app.route('/time')
def current_time():
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Текущее время: {formatted_time}</h1>"

@app.route('/encrypt/<string:text>/<int:shift>')
def encrypt(text, shift):
    encrypted_text = ''.join(chr((ord(char) - 97 + shift) % 26 + 97) if char.islower() else char for char in text)
    return f"<h1>Зашифрованный текст: {encrypted_text}</h1>"

@app.route('/fibonacci/<int:n>')
def fibonacci(n):
    if n < 0:
        return "<h1>Число Фибоначчи определено только для неотрицательных чисел</h1>"
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return f"<h1>{n}-е число Фибоначчи: {a}</h1>"

@app.route('/prime/<int:n>')
def is_prime(n):
    if n < 2:
        return f"<h1>Число {n} не является простым</h1>"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return f"<h1>Число {n} не является простым</h1>"
    return f"<h1>Число {n} является простым</h1>"

if __name__ == "__main__":
    app.run(debug=True)
