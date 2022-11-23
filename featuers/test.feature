# Пример тестирования на английском языке
# Feature: Check working
# Scenario: Сheck work site
#   Given website "http://127.0.0.1:8000/"
#   When push button with div 'fs_start_game'
#   Then page include div 'rounds-container'

# language: ru

Функционал: Работает ли основной функционал программы
Сценарий: Прохождение полного цикла игры
Дано Запущен сайт "http://localhost:8000/"
Когда Пользователь выбирает первый раздел, первую тему, первый раунд и прокликивает до конца
То воспроизводится фейерверк