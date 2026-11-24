# Проект FitLife - MVP версия 1.0
import sys

sys.stdout.reconfigure(encoding="utf-8")

# 1. Знакомство
user_name = input("Как Вас зовут?")
user_age = int(input("Сколько Вам лет?"))

# 2. Сбор данных
user_weight = float(input("Введите Ваш вес(кг):"))
user_height = float(input("Введите Ваш рост(м):"))

# 3. Рассчет индекса массы тела
bmi = user_weight / (user_height ** 2)
round(bmi, 1)

# Подсчет воды
water_needed = user_weight * 30
water_l = water_needed / 1000

# 4. Вывод красивого результата
print(f"Здравствуйте, {user_name}!")
print(f"Ваш ИМТ: {round(bmi, 1)}")
print(f"Рекомендуемая норма воды: {water_l} л")
print("Расчет окончен. Будьте здоровы!")
