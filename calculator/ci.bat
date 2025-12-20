echo 1. DOWNLOADING CODE
git clone https://github.com/MuraBoom/calculator.git
cd calculator

echo 2. CHECKING FOLDER STRUCTURE
if exist "calculator" (
    echo Found nested calculator folder
    cd calculator
)

echo 3. CHECKING FOR TEST FILE
echo Files in current folder:
dir *.py

if exist "test_division.py" (
    echo Found test_division.py
) else (
    echo ERROR: test_division.py not found
    echo Please check if test file exists in repo
    pause
    exit /b 1
)

echo 4. BUILDING EXE
pyinstaller --onefile --windowed --name="Calculator" main.py

echo 5. RUNNING TESTS
python test_division.py
if errorlevel 1 (
    echo TESTS FAILED
    pause
    exit /b 1
)

echo 6. CREATING INSTALLER
if exist "calculator.iss" (
    iscc calculator.iss
    echo Installer created
) else (
    echo WARNING: calculator.iss not found
)

echo 7. INSTALLING APPLICATION
md "%USERPROFILE%\Calculator" 2>nul
if exist "dist\Calculator.exe" (
    copy "dist\Calculator.exe" "%USERPROFILE%\Calculator\"
    echo [InternetShortcut] > "%USERPROFILE%\Desktop\Calculator.url"
    echo URL=file:///%USERPROFILE%/Calculator/Calculator.exe >> "%USERPROFILE%\Desktop\Calculator.url"
    echo SUCCESS: Calculator installed
) else (
    echo ERROR: Calculator.exe not found in dist folder
)

echo DONE
pause
