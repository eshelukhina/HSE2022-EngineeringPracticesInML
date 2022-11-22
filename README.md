# SVM и его ядр
### Содержание
1. [Пакетный менеджер](#пакетный_менеджер)
2. [Развертывание окружения](#развертывание_окружения)
3. [Сборка_пакета](#сборка_пакета)
3. [Ссылка_на_пакет_в_pypi-test](#ссылка_на_пакет)
4. [Установка_пакета_из_pypi-test](#установка_пакета)

<a name="пакетный_менеджер"></a>
## Пакетный менеджер PIP
* Установка пакетного менеджера
```
sudo apt install python3-pip 
```
* На случай если что-то пошло не так (не Linux)

    https://pip.pypa.io/en/stable/installation/



<a name="развертывание_окружения"></a>
## Развертывание окружения
* Создание виртуальной среды `env`
```
python3 -m venv env
cd env
```
* Активация
```
. bin/activate
```
* Установка пакетных зависимостей
```
# для разработки
pip install -r requirements-dev.txt
# для использования
pip install -r requirements.txt
```
* Запуск программы
```
python3 main.py
```

<a name="сборка_пакета"></a>
### Сборка пакета
```
python setup.py sdist bdist_wheel   
```
* Публикация
```
twine upload --repository testpypi dist/*
```

<a name="ссылка_на_пакет"></a>
### Ссылка на пакет в pypi-test
[https://test.pypi.org/](https://test.pypi.org/project/svm-eshelukhina/0.0.1/)

<a name="установка_пакета"></a>
### Установка пакета из pypi-test
```
pip3 install -i https://test.pypi.org/simple/ svm-eshelukhina
```
