# only_search_footer
Скрипт для автоматизированного тестирования сайта https://only.digital/.

# Запуск скрипта
Для запуска скрипта необходимо выполнить шаги, указанные ниже.

## 1. Установка python
Для установки интерпретатора python необходимо перейти на сайт
https://www.python.org/downloads/ и скачать Python 3.13.2 для Вашей операционной системы.

## 2. Клонирование проекта и установка локального окружения
Для клонирования проекта и установки виртуального окружения используйте скрипты, представленные ниже
### Для Windows
~~~
git clone https://github.com/umbazanova/only_search_footer.git && cd only_search_footer && python -m venv venv
~~~

### Для Linux/MacOS
~~~
git clone https://github.com/umbazanova/only_search_footer.git && cd only_search_footer && python3 -m venv venv 
~~~

## 3. Активирование виртуального окружения и установка нужных зависимостей
Для активации виртуального окружения и установки зависимостей нужно находиться в корне проекта, используйте скрипты, представленные ниже

### Для Windows
~~~
venv\Scripts\activate && python -m pip install -r requirements.txt
~~~

### Для Linux/MacOS
~~~
source ./venv/bin/activate && pip install -r ./requirements.txt
~~~

## 4. Запуск скрипта
Убедитесь, что Вы находитесь внутри активированного виртуального окружения и выполните скрипт, указанный ниже
### Для Windows
~~~
python main.py
~~~

### Для Linux/MacOS
~~~
python3 ./main.py
~~~