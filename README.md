# skillfactory_django
Repository for whole process of learning Django

## 7. Итоговое задание 28.5.1 (HW-03)

* Установить библиотеки celery и redis
* Запустить celery для сигналов: (venv)...\skillfactory_django\NewsPortal> celery -A NewsPortal worker -l INFO --pool=solo
* Запустить периодическую задачу: celery -A NewsPortal beat -l INFO

```commandline
>> 1. Установить Redis.
>> 2. Установить Celery.
>> 3. Произвести необходимые конфигурации Django для соединения всех компонентов системы.
>> 4. Реализовать рассылку уведомлений подписчикам после создания новости.
>> 5. Реализовать еженедельную рассылку с последними новостями (каждый понедельник в 8:00 утра).
```

## 6. Итоговое задание 27.5.4 (HW-03)

* Подписаться на категорию можно по ссылке /news/categories/
* При регистрации приходит письмо от адреса juliakarabasova@yandex.ru
* При добавлении новой статьи подписанным на категории пользователям приходят письма с заголовком, первыми 50 символами и гиперссылкой
* Каждую неделю подписанным пользователям приходит на почту список новых статей, появившийся за неделю с гиперссылкой (нужно запустить в отдельном пространстве командой python manage.py runapscheduler)

```commandline
>> 1. В категории должна быть возможность пользователей подписываться на рассылку новых статей в этой категории.
>> 2. Если пользователь подписан на какую-либо категорию, то, как только в неё добавляется новая статья, её краткое содержание приходит пользователю на электронную почту, которую он указал при регистрации. В письме обязательно должна быть гиперссылка на саму статью, чтобы он мог по клику перейти и прочитать её.
>> 3. Если пользователь подписан на какую-либо категорию, то каждую неделю ему приходит на почту список новых статей, появившийся за неделю с гиперссылкой на них, чтобы пользователь мог перейти и прочесть любую из статей.
>> 4. Добавьте приветственное письмо пользователю при регистрации в приложении.
```

## 5. Итоговое задание 26.6.2 (HW-03)

* Созданы страницы регистрации и входа
* Есть возможность войти через Google-аккаунт
* Созданы две группы пользователей
* Пользователям автор доступно создание, редактирование и удаление постов

```commandline
>> 1. В классе-представлении редактирования профиля добавить проверку аутентификации.
>> 2. Выполнить необходимые настройки пакета allauth в файле конфигурации.
>> 3. В файле конфигурации определить адрес для перенаправления на страницу входа в систему и адрес перенаправления после успешного входа.
>> 4. Реализовать шаблон с формой входа в систему и выполнить настройку конфигурации URL.
>> 5. Реализовать шаблон страницы регистрации пользователей.
>> 6. Реализовать возможность регистрации через Google-аккаунт.
>> 7. Создать группы common и authors.
>> 8. Реализовать автоматическое добавление новых пользователей в группу common.
>> 9. Создать возможность стать автором (быть добавленным в группу authors).
>> 10. Для группы authors предоставить права создания и редактирования объектов модели Post (новостей и статей).
>> 11. В классах-представлениях добавления и редактирования новостей и статей добавить проверку прав доступа.
```

## 4. Итоговое задание 25.7 (HW-03)

* Новости можно фильтровать по ссылке /news/search
* Создавать новые новости можно по ссылке /news/create
* Каждый отдельный пост можно редактировать по ссылке /news/<id-поста>/edit и удалять по ссылке /news/<id-поста>/delete
* Аналогично можно создавать (/articles/create), редактировать (/articles/<id>/edit) и удалять (/articles/<id>/delete) записи

```commandline
>> Добавьте постраничный вывод на /news/, чтобы на одной странице было не больше 10 новостей и были видны номера лишь ближайших страниц, а также возможность перехода к первой или последней странице.

>> Добавьте страницу /news/search. На ней должна быть реализована возможность искать новости по определённым критериям. Критерии должны быть следующие:

>> - по названию
>> - по имени автора
>> - позже указываемой даты

>> Убедитесь, что можно выполнить фильтрацию сразу по нескольким критериям.

>> Запрограммируйте страницы создания, редактирования и удаления новостей и статей. Предлагаем вам расположить страницы по следующим ссылкам:
>>      /news/create/
>>      /news/<int:pk>/edit/
>>      /news/<int:pk>/delete/
>>      /articles/create/
>>      /articles/<int:pk>/edit/
>>      /articles/<int:pk>/delete/
```

## 3. Итоговое задание 24.6 (HW-03)

* Все новости доступны по ссылке /news/
* Каждый отдельный пост доступен по ссылке /news/<id-поста>
* "Плохие" слова цензурируются до первого символа с сохранением пунктуации

```commandline
>> Создать новую страницу с адресом /news/, на которой должен выводиться список всех новостей.
>> Вывести все статьи в виде заголовка, даты публикации и первых 20 символов текста.
>> Новости должны выводиться в порядке от более свежей к самой старой.
>> Сделать отдельную страницу для полной информации о статье /news/<id новости>.
>> На этой странице должна быть вся информация о статье. Название, текст и дата загрузки в формате день.месяц.год.
>> Написать собственный фильтр censor, который заменяет буквы нежелательных слов в заголовках и текстах статей на символ «*».
>> Все новые страницы должны использовать шаблон default.html как основу.
```

## 2. Итоговое задание 23.9 (HW-03)

* Создать приложение news
* Разработать в нем модели Author, Category, Post, PostCategory, Comment (NewsPortal/news/models.py)
* Подготовить файл со всеми командами для Django shell (shell_commands.py)
```commandline
>> Создать двух пользователей (с помощью метода User.objects.create_user('username')).
>> Создать два объекта модели Author, связанные с пользователями.
>> Добавить 4 категории в модель Category.
>> Добавить 2 статьи и 1 новость.
>> Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
>> Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
>> Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
>> Обновить рейтинги пользователей.
>> Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
>> Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
>> Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
```

## 1. Итоговое задание 23.9 (HW-03) 
### [NOT AVAILABLE HERE ANYMORE]

* Создать проект Django.
* Добавить в него 3 статические странички.
* На одной из страниц контент повторяется 2 раза без изменения content (два раза прописано ```{{ flatpage.content }}```).
* Одна из страниц на сайте доступна только админу (только вошедшему пользователю).
* На одной из страниц изменены шрифты и размеры текста.
* Сайт представляет собой оформленный Bootstrap-шаблон со встроенными пользовательскими данными.
* Статические файлы Bootstrap загружаются через теги ```{% load static %}``` и ```{% static %}```.

```
>> Репозиторий содержит проект Django
>> Три статические странички: about, contact, information
>> На странице information контент повторяется 2 раза
>> Страница contact доступна только админу (Логин: admin, Пароль: admin)
>> На странице contact изменены шрифты и размеры текста
>> Сайт оформлен в Bootstrap-шаблон 
```
