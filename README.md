Выполненные задания по курсу Backend

Здесь будут храниться все задания, выполненные в рамках прохождения курса по Backend-разработке.

Установка и настройка проекта

Клонирование репозитория
Открываем терминал и выполняем команду:
git clone https://github.com/S-NOWNUM-B/-Bak-End-

Затем переходим в папку проекта:

cd -Bak-End-

Создание виртуального окружения (рекомендуется)
python -m venv venv

Активируем окружение:
Windows:

venv\Scripts\activate Mac/Linux:

source venv/bin/activate

Установка зависимостей
pip install -r requirements.txt

Настройка базы данных и запуск миграций
python manage.py makemigrations python manage.py migrate

Создание суперпользователя (для входа в админ-панель)
python manage.py createsuperuser

Заполняем поля (логин, email, пароль).

Запуск сервера
python manage.py runserver

После этого сервер будет доступен по адресу http://127.0.0.1:8000/.

Полезные команды Django

Создать новое приложение в Django
python manage.py startapp <app_name>

Очистить базу данных и заново применить миграции
python manage.py flush python manage.py migrate

Создать новую миграцию (если изменились модели)
python manage.py makemigrations

Просмотреть список доступных команд Django
python manage.py help

Запустить интерактивную консоль Django
python manage.py shell

Собрать статические файлы (если используется STATICFILES_DIRS)
python manage.py collectstatic

Тестирование приложения
python manage.py test

Создать дамп базы данных (бэкап)
python manage.py dumpdata > backup.json

Загрузить дамп базы данных
python manage.py loaddata backup.json