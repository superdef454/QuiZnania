# language: ru

Функционал: Работает ли флаг отображения в БД
Сценарий: Нажатие на флаг в бд
Дано Страница "http://localhost:8000/sigame/" с объектом "/html/body/div/div/div/a"
Когда На странице бд "http://localhost:8000/admin/sigame/section/" выключить отображение объекта "/html/body/div/div[3]/div/div[1]/div/div/div/form/div[4]/table/tbody/tr/td[2]/input" и сохранить изменения "/html/body/div/div[3]/div/div[1]/div/div/div/form/p/input"
То На странице "http://localhost:8000/sigame/" пропадёт объект "/html/body/div/div/div/a"