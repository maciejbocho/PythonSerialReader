PI38 APL SLICEBUS I2C INTEG TESTS - Python

Jak utworzyc i uzyc .venv (Windows)

1. Przejdz do folderu projektu:
cd "C:\Users\E1555400\OneDrive - Emerson\Documents\TESTS\PI38 APL_SLICEBUS_I2C_INTEG_TESTS\PYTHON"

2. Utworz srodowisko wirtualne:
py -m venv .venv

3. Zainstaluj wymagany pakiet do tego srodowiska:
.\.venv\Scripts\python.exe -m pip install pyserial

4. Uruchom program na interpreterze z .venv:
.\.venv\Scripts\python.exe SerialCommunication.py

Aktywacja srodowiska (opcjonalnie)

PowerShell:
.\.venv\Scripts\Activate.ps1

CMD:
.\.venv\Scripts\activate.bat

Jesli PowerShell blokuje Activate.ps1:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

Weryfikacja, czy dziala .venv:
python -c "import sys; print(sys.executable)"

Oczekiwany wynik: sciezka zawiera .venv\Scripts\python.exe

Wazne

- Instalujesz pakiet: pyserial
- Importujesz w kodzie: import serial
