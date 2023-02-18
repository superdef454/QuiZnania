# QuiZnania

Викторина предназначенная для преподавателей для работы с аудиторией в стиле своей игры

***Цель***

Реализовать переносное вэб приложения с базой данных вопросов преподавателей

***Задачи***

+ Собрать приложение в единый EXE файл
+ Реализовать интерефейс в окне браузера
+ Реализовать лёгкую для преподавателей возможность редактирование базы вопросов (Базы данных)

***Реализация***

Стек программы:
+ Python (portable python для переноса программы под разные системы)
+ Django (+Django-admin)
+ JS (JQuery)

***Этапы проведения викторины (работы программы)***

1. Начальная страница с справкой по использованию

![image](https://user-images.githubusercontent.com/92267924/203496828-ed31bd5e-4dbf-4380-9967-1bb4808a4785.png)

2. Выбор требумего раздела, игры и раунда

3. Проведение игры:

*Единое окно для всех команд с темами и вопросами*

![image](https://user-images.githubusercontent.com/92267924/203497249-19fb9139-04e6-4965-b8a3-b548022bce0d.png)

*Поле вопроса*

![image](https://user-images.githubusercontent.com/92267924/203500908-c4a327aa-ddb2-46b3-be15-e8aff3570790.png) 
![image](https://user-images.githubusercontent.com/92267924/203500975-01ce4fed-b27c-456a-b16c-ab3d3d5bfc9a.png)

*Результат программы после ответа команды на вопрос*

![image](https://user-images.githubusercontent.com/92267924/203501255-da3f1448-c791-4434-a5e4-d506dc5865e5.png)

*Финальный подсчёт очков команды с анимацией фейерверка*

![image](https://user-images.githubusercontent.com/92267924/203501521-da711303-5018-4c43-aeb7-a27755899655.png)

> Настройки игры:
>> + Количество команд задаёт преподаватель
>> + Предоставляется возможность сбросить очки команд
>> + Предоставляется возможность настроить отображаемые блоки вопросов и сами вопросы
>> 
>> *Поле настроек на странице игры*
>>
>> ![image](https://user-images.githubusercontent.com/92267924/203497991-190decea-34e4-4c40-a0c9-61d5ab1a28d2.png)
>>
>>
>> *Окна настроек БД*
>>
>> ![image](https://user-images.githubusercontent.com/92267924/203498952-e641af57-af1c-4975-b0b9-ad44e01bb481.png)
>>
>> ![image](https://user-images.githubusercontent.com/92267924/203499071-03f8879d-92d4-438d-807c-aad45d3e0866.png)
>> 
>> *Окно добавления темы и вопросов в ней*
>> 
>> ![image](https://user-images.githubusercontent.com/92267924/203499906-dcb4c717-483f-4ebe-910b-9527cc26ddf1.png)

---

***Установка и запуск***

+ Скачать файл Quiz.exe
+ Распаковать и запустить файл start.bat

***Пост задачи***

+ Реализовать тестирование на Gherkin с запуском Selenium
+ Подготовить проект к развёртыванию в докере
