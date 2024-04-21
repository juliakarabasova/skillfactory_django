# skillfactory_django
Repository for whole process of learning Django

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