# animals-shelter
🐢 API Веб приложение для управления базой данных животных на базе PostgreSQL

<div align=center>
  <img src='https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif' alt='cute_cat'/>
</div>

---
# Подготовка к работе:
Клонирование репозитория с проектом на свою локальную машину:
```bash
git clone https://github.com/1kitten/animals-shelter
```

Необходимо перейти в папку с проектом
```bash
cd animals-shelter
```

Установка виртуального окружения:
<b>Windows:</b>
```bash
python -m venv venv
```
<b>Linux, macOS:</b>
```bash
python3 -m venv venv 
```

Активация виртуального окружения:
<b>Windows:</b>
```bash
.\venv\scripts\activate
```
<b>Linux, macOS:</b>
```bash
source venv/bin/activate
```

Установка всех зависимостей:
```bash
pip install -r requirements.txt
```

---

# Настройка проекта:

Необходимо создать и применить все миграции базы данных.<br>
Для этого перейдём в папку <code>animals_shelter</code> и выполним команды
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

К проекту была подключена база данных PostgreSQL <img src='https://github.com/devicons/devicon/blob/master/icons/postgresql/postgresql-original.svg' width=20/><br>
При помощи сервиса <a href='railway.app'>railway.app</a><br>
По необходимости измените настройки базы данных в файле <code>settings.py</code> проекта.

Необходимо создать супер-пользователя командой:
```bash
python manage.py createsuperuser
```

Проверяем работоспособность приложения командой:
```bash
python manage.py runserver
```

---

# Инструкция по использованию API

После перехода на страницу http://127.0.0.1:5000/api/v1/animals/ <br>
<b>Неавторизированный</b> пользователь сможет просмотреть список <b>НЕ УДАЛЁННЫХ</b> животных.
<b>Авторизированный</b> пользователь сможет добавить нового питомца. Если авторизированный пользователь не является администратором,
он сможет просматривать и изменять только своих добавленных питомцем.<br>
Если пользователь является супер-пользователем (Администратором), то он сможет просматривать всех доступных питомцев, а также изменять и "мягко" удалять их.

<br>

Для посмотра детальной информации о питомце, необходимо перейти по адресу http://127.0.0.1:5000/api/v1/animals/{animal_id} <br>
Где вместо <code>animal_id</code> необходимо указать идентификатор записи питомца. <br>
Если пользователь является Администратором, он сможет изменить информацию о питомце, а также "мягко" удалить его. <br>
Если пользователь авторизирован, он сможет изменять информацию только о своих добавленных питомцах, удалять их он <b>НЕ МОЖЕТ</b>.
Если пользователь является не авторизированным, ему доступен только просмотр информации о питомце.

---

# Дополнительная информация

Для просмотра более детальной документации, рекомендую перейти на страницу http://127.0.0.1:5000/api/swagger/ <br>
На данной странице расположена вся необходимая информация для комфортного использования приложения, документация оформлена с помощью модуля drf-yasg (swagger). <br>
<br>
В папке под названием <code>animals</code> расположена директория <code>fixtures</code>. В данной папке лежит файл <code>animals.json</code> - файл фикструры
для заполнения таблицы animals в базе данных готовыми данными. Для использования необходимо выполнить команду:

```bash
python manage.py loaddata animals/fixtures/animals.json
```
---

<div align=center>
  <p>Приятного пользования 😉!</p>
</div>
