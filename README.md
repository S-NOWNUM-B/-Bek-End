**Выполненные задания по курсу Backend**

Данный репозиторий содержит выполненные задания в рамках курса по Backend-разработке.

**1. Установка и настройка проекта**

**1.1 Клонирование репозитория**
1.Открываем терминал и выполняем команду:

git clone https://github.com/S-NOWNUM-B/-Bak-End-

2. Затем переходим в папку проекта:
3. cd -Bak-End-

**1.2 Создание виртуального окружения (рекомендуется)**
Создаем виртуальное окружение:

python -m venv venv

4. Активация окружения:
Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

**1.3 Установка зависимостей**

5. Устанавливаем зависимости:

pip install -r requirements.txt

**1.4 Настройка базы данных и запуск миграций**
6. Создаем миграции:

python manage.py makemigrations

7. Применяем миграции:

python manage.py migrate

**1.5 Создание суперпользователя (для входа в админ-панель)**
8. Выполняем команду:

python manage.py createsuperuser

9. Заполняем поля (логин, email, пароль).

**1.6 Запуск сервера**
10. Запускаем сервер:

python manage.py runserver

11. После этого сервер будет доступен по адресу: http://127.0.0.1:8000/

**2. Полезные команды Django**

**2.1 Создать новое приложение в Django**

12. python manage.py startapp <app_name>

**2.2 Очистить базу данных и заново применить миграции**

13. python manage.py flush
14. python manage.py migrate

**2.3 Создать новую миграцию (если изменились модели)**

15. python manage.py makemigrations

**2.4 Просмотреть список доступных команд Django**

16. python manage.py help

**2.5 Запустить интерактивную консоль Django**

17. python manage.py shell

**2.6 Собрать статические файлы (если используется STATICFILES_DIRS)**

18. python manage.py collectstatic

**2.7 Тестирование приложения**

19. python manage.py test

**2.8 Создать дамп базы данных (бэкап)**

20. python manage.py dumpdata > backup.json

**2.9 Загрузить дамп базы данных**

21. python manage.py loaddata backup.json
