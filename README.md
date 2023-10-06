# **Store**

## **Описание:**
Интернет магазин Store
***Данный сервис позволяет:***
* Тавары поделены на категории, что позволит легче ореентироваться на сайте
* просматривать товары
* регестрироваться в магазине через GitHub
* добавлять тавары в покупки
* совершать оплату товаров

### **Технолгии**
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)<br>
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)<br>
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)<br>
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)<br>
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)<br>
![Stripe](https://img.shields.io/badge/Stripe-626CD9?style=for-the-badge&logo=Stripe&logoColor=white)<br>

### **Запуск проекта:**
```
git clone https://github.com/Rishat-Ver/Store.git # клонируем проект
python -m venv venv # Создаем виртуальное окружение
source /venv/Scripts/activate # Активируем виртуальное окружение
pip install -r requirements.txt # Устанавливаем зависимости
# Создайте файл .end (Шаблон см. ниже)
python manage.py makemigrations # Сщздания миграций
python manage.py migrate # Применение миграций
python manage.py loaddata products/fixtures/categories.json # Заполняем базу категориями
python manage.py loaddata products/fixtures/books.json #  Заполняем базу продуктами
python manage.py runserver
```

### **.env:**
```
DEBUG=True
SECRET_KEY=Секретный ключ джанги
DOMAIN_NAME=http://127.0.0.1:8000

REDIS_HOST=127.0.0.1
REDIS_PORT=6379

DATABASE_NAME=Имя базы
DATABASE_USER=Имя ползователя
DATABASE_PASSWORD=Пароль от базы
DATABASE_HOST=localhost
DATABASE_PORT=5432

EMAIL_HOST=smtp.yandex.com
EMAIL_PORT=465
EMAIL_HOST_USER=Ваша почта
EMAIL_HOST_PASSWORD= Пароль от почты
EMAIL_USE_SSL=True
EMAIL_USE_TLC=False

STRIPE_PUBLIC_KEY=<https://stripe.com/docs/keys>
STRIPE_SECRET_KEY=<https://stripe.com/docs/keys>
STRIPE_WEBHOOK_SECRET=<https://stripe.com/docs/keys>
```


### **Разработчик:**
- Вергасов Ришат <br>
- GitHub: https://github.com/Rishat-Ver <br>
- Telegram: https://t.me/Rishik1991 <br>
- Email: Zvezda-Rishat1991@yandex.ru <br>
- Вконтакте: https://vk.com/id356120934

