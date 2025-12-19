[Setup]
; основные настройки программы
AppName=Калькулятор
; название программы

AppVersion=1.0
; версия программы

AppPublisher=Лиана и Даша
; кто создал

AppPublisherURL=https://github.com/MuraBoom
; ссылка на репозиторий

DefaultDirName={pf}\Calculator
; папка установки (Program Files\Calculator)

DefaultGroupName=Калькулятор
; название в меню "Пуск"

UninstallDisplayIcon={app}\Calculator.exe
; иконка для удаления в панели управления

Compression=lzma2
; метод сжатия файлов

SolidCompression=yes
; максимальное сжатие

OutputDir=.
; куда сохранить setup (в текущую папку)

OutputBaseFilename=setup_calculator
; имя установщика


[Languages]
; русский язык интерфейса установщика
Name: "russian"; MessagesFile: "compiler:Languages\Russian.isl"

[Tasks]
; дополнительные задачи при установке
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
; создать ярлык на рабочем столе (по умолчанию не выбран)

[Files]
; список файлов, которые копируются при установке
Source: "dist\Calculator.exe"; DestDir: "{app}"; Flags: ignoreversion
; главный файл программы из папки dist

; исходные файлы программы (необязательно, можно удалить)
Source: "main.py"; DestDir: "{app}\src"; Flags: ignoreversion
; главный скрипт

Source: "calculator_ui.py"; DestDir: "{app}\src"; Flags: ignoreversion
; интерфейс калькулятора

Source: "calculator_logic.py"; DestDir: "{app}\src"; Flags: ignoreversion
; логика вычислений

Source: "memory.py"; DestDir: "{app}\src"; Flags: ignoreversion
; работа с памятью калькулятора

Source: "operations.py"; DestDir: "{app}\src"; Flags: ignoreversion
; математические операции

[Icons]
; создание ярлыков
Name: "{group}\Калькулятор"; Filename: "{app}\Calculator.exe"
; ярлык в меню "Пуск" в папке "Калькулятор"

Name: "{group}\Удалить Калькулятор"; Filename: "{uninstallexe}"
; ярлык для удаления программы в меню "Пуск"

Name: "{commondesktop}\Калькулятор"; Filename: "{app}\Calculator.exe"; Tasks: desktopicon
; ярлык на рабочем столе (только если выбрали в задачах)

[Run]
; действия после установки
Filename: "{app}\Calculator.exe"; Description: "{cm:LaunchProgram,Калькулятор}"; Flags: nowait postinstall skipifsilent
; запустить калькулятор после установки

[UninstallDelete]
; что удалять при деинсталляции
Type: filesandordirs; Name: "{app}"
; удалить всю папку программы
