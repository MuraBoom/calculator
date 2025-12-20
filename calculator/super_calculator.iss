[Setup]
; Имя программы
AppName=Calculator
; Кто создал
AppPublisher=Лиана и Даша
; Версия
AppVersion=1.0
; Папка установки по умолчанию (C:\Program Files\Calculator)
DefaultDirName={autopf}\Calculator
; Имя готового файла установщика
OutputBaseFilename=Calculator_Setup

Compression=lzma2
; метод сжатия файлов

SolidCompression=yes
; максимальное сжатие

[Files]
; Основной файл, собранный из calculator_ui.py и логики
Source: "dist\SuperCalculator.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
; Создание ярлыка в меню "Пуск"
Name: "{group}\Calculator"; Filename: "{app}\SuperCalculator.exe"
