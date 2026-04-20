### RFID Poker Table Control Software

## Install
1. If you do not have python installed: Goto https://www.python.org/downloads/ and download the latest version of python.
2. Insatll python. There is no need for the python install manager.
3. Open/Reopen Power shell 
4. Navigate to git repo
5. Create venv: 
```powershell
python -m venv .venv
```
6.Activate venv:
```powershell
.\venv\Scripts\activate.ps1
```
If power shell blocks:
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
7.Install packages:
```
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

8.Double click executable