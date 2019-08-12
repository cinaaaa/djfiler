<p align="center">
    <img width="300" src="https://raw.githubusercontent.com/E-RROR/django-filer/master/d376573d-c0f3-4fde-8467-952d7ffada1d_200x200.png" />
</p>

<h1 align="center">Django Filer</h1>

<div align="center">
    <h2>An Easy Way To Upload Files To Django</h2>
</div>

## ✨ Features

- Upload Any File With Any Size In Any Format
- Saves Files Secure and Denied Foreign Requests
- Simple Import and Usage
- Host Files Safely With Simple Key

## 📦 Install

```bash
pip3 install django-filer
```

## 🔨 Usage

```python

# Import Django Filer
from djangofiler import djangofiler

# Initial Django Filer
djs = djangofiler.Filer('/dir/of/uploades', True: is "Debugger Mode")

''' djs can be any name you like '''
```

Handle Upload Files In Any Format

```python
def home(request):
    if request.method == "POST":
        callback = djs.upload(file=request.FILES['file name uploaded'])
        print(callback) # Its Returns {status: ok or fail , name: name of file , type: type of file }
```
