# Курсовая работа на тему "Салон красоты"
## Оглавление
1. [Автор работы](#Автор-работы)
2. [Запуск проекта](#Запуск-проекта)
3. [Структура базы данных](#Структура-базы-данных)
4. [Супер пользователь](#Супер-пользователь)
5. [Остальные пользователи](#Остальные-пользователи)
## Автор работы
Автором данной работы является студент 2 курса Московского политехнического университета Ашрафулин Рамиль.
## Запуск проекта
В этом разделе перечислены основные шаги для запуска проекта на локальной машине:
1. Для запуска проекта необходимо установить на свой компьютер язык программирования Python.
2. После этого необходимо перейти в папку проекта и создать новое виртуальное окружение с помощью команды `python -m venv venv`
3. После создания виртуального окружения необходимо активировать его. Для разных операционных систем понадобятся разные команды:
	1. Windows: `venv\Scripts\activate.bat`
	2. Linux: `source ./venv/bin/activate`
4. После активации виртуального окружения можно приступить к установке необходимых библиотек с помощью команды `pip install -r requirements.txt`
5. Далее необходимо применить все имеющиеся миграции, чтобы привести базу данных к нужному состоянию.
6. После создания базы данных необходимо создать супер пользователя. Для этого нужно перейти в папку проекта `courseWorkRamil`   и применить команду `python manage.py createsuperuser`.
7. После установки необходимых библиотек, создания базы данных и суперпользователя нужно  запустить проект командой `python manage.py runserver`.
## Структура базы данных
![Структура БД](<src/images/Структура бд.png>)
## Супер пользователь
Во время работы над проектом для доступа к панели администрирования Django был создан суперпользователь (администратор) с именем пользователя *ramil* и паролем *ramil123*.
## Остальные пользователи
Так же при работе над проектом были созданы дополнительные пользователи для проверки функционала клиента и мастера.
Имена созданных пользователей можно посмотреть в админке проекта. Все пользователи имеют один и тот же пароль: *testpassword1*.