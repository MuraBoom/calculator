#!/bin/bash

VERSION=$1

if [ -z "$VERSION" ]; then
    echo "Ошибка: Введите версию проекта."
    echo "Пример: ./deploy.sh 1.0.5"
    exit 1
fi

echo "--- ЭТАП 1: Загрузка актуального состояния  ---"
git clone https://github.com/MuraBoom/calculator

cd calculator/calculator || exit

echo "--- ЭТАП 2: Сборка окружения и подготовка  ---"
python -m venv venv
source venv/Scripts/activate
pip install pyinstaller

echo "--- ЭТАП 3: Выполнение unittest  ---"
python test_memory.py && python test_operations.py && python test_division.py
if [ $? -ne 0 ]; then
    echo "Тесты провалены! Сборка остановлена."
    exit 1
fi

echo "--- ЭТАП 4: Создание установщика  ---"
pyinstaller --onefile --noconsole --name "SuperCalculator" main.py

sed -i "s/AppVersion=.*/AppVersion=$VERSION/" super_calculator.iss

"C:/Program Files (x86)/Inno Setup 6/ISCC.exe" super_calculator.iss

echo "--- ЭТАП 5: Установка приложения  ---"
./Output/Calculator_Setup.exe

echo "Интеграция завершена успешно! Версия: $VERSION"
