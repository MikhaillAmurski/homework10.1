# Проект "Моё обучение Python"

## Описание

Этот проект представляет собой мой путь освоения языка Python
В нём будут представлены мои работы над виджетом банковских операций клиента
Я только начал свой путь в освоении IT и много не знаю, но буду усердно трудиться!
Это обучение очень вдохновляет и мотивирует меня, мне безумно нравиться!

## Code coverage

Code coverage моего проекта достигает 95%

## Описание


Это веб-приложение на Python для управления задачами и проектами, которые показывает несколько последних успешных банковских операций клиента.

реализована функция, которая принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX Т. е. видны первые 6 цифр и последние 4, номер разбит по блокам по 4 цифры, разделенным пробелами.

реализована функция, которая принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате **XXXX Т. е. видны только последние 4 цифры.

реализована функция, которая принимать на вход строку с информацией — тип карты/счета и номер карты/счета. Возвращать исходную строку с замаскированным номером карты/счета. Для карты и счета используйте разные маскировки.

реализована функция, которая принимает на вход строку вида 2018-07-11T02:26:18.671407 и возвращает строку с датой в виде 11.07.2018

реализована функция, которая принимает на вход список словарей и значение для ключа state (опциональный параметр со значением по умолчанию EXECUTED) и возвращает новый список, содержащий только те словари, у которых ключ state содержит переданное в функцию значение.

реализована функция, которая принимает на вход список словарей и возвращает новый список, в котором исходные словари отсортированы по убыванию даты (ключ date). Функция принимает два аргумента, второй необязательный задает порядок сортировки (убывание, возрастание).

реализована функцию, которая принимает список словарей с банковскими операциями (или объект-генератор, который выдает по одной банковской операции) и возвращает итератор, который выдает по очереди операции, в которых указана заданная валюта.

реализован генератор, который принимает список словарей и возвращает описание каждой операции по очереди

реализован генератор номеров банковских карт, который должен генерировать номера карт в формате XXXX XXXX XXXX XXXX, где X — цифра. Должны быть сгенерированы номера карт в заданном диапазоне, например от 0000 0000 0000 0001 до 9999 9999 9999 9999 (диапазоны передаются как параметры генератора).


## Установка:

1. Клонируйте репозиторий:
```
git clone git@github.com:MikhaillAmurski/homework10.1.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```


## Тестирование:



- реализованы тестовые функции с использованием библиотеки pytest для существующего кода проекта.
- Использованы фикстуры для формирования входных данных для тестов.
- Использована параметризация в тестах для запуска одного теста с различным набором входных параметров.

## Подробнее...

Если Вы тоже хотить освоить что-от новое, записывайтесь на обучение в SKYPRO!
Новые открытия и эмоции от познания мира IT ждут ВАС по [ссылке](https://my.sky.pro)!
Лучшие кураторы и наставники не оставят Вас один на один с непонятной задачей и всегда помогут!

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).
