<p align="center">
    <img width="200" src="https://raw.githubusercontent.com/E-RROR/djfiler/master/djfiler/d376573d-c0f3-4fde-8467-952d7ffada1d_200x200.png" />
</p>

<h1 align="center">Django Filer</h1>
<p align="center">An Easy Way To Upload Files To Django</p>
<div align="center">
<img align="center" alt="PyPI" src="https://img.shields.io/pypi/v/djfiler?color=%23cccc&label=version&style=plastic" />
<img align="center" alt="PyPI - Django Version" src="https://img.shields.io/pypi/djversions/djangorestframework" />
<img align="center" alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/djfiler" />
<img align="center" alt="PyPI - Wheel" src="https://img.shields.io/pypi/wheel/djfiler" />
</div>

## ✨ Features

- Upload Any File With Any Size In Any Format
- Saves Files Secure and Denied Foreign Requests
- Simple Import and Usage
- Host Files Safely With Simple Key

## 📦 Install

```bash
$ pip3 install djfiler
```

## 🔨 Usage

```python

# Import Django Filer & json
import json
from djfiler import djfiler

# Initial Django Filer
djs = djfiler.Filer('/dir/of/uploades', True)

''' djs can be any name you like '''
```

## 📤 Upload in Any Format
first create the function
urls.py
```python
def home(request):
    if request.method == "POST":
        callback = djs.upload(file=request.FILES['file name uploaded'], name="Optional" )
        print(callback) # Its Returns {status:ok | fail,name: name of file ( Its Key Of File ),type: type of file }
```
Return Any File With A Simple Key (Key Is The String That We Return To You When Uploaded file)
then in html file create simple form that send files with a name
```html
<form action="/path/to/any/url" method="post" enctype="multipart/form-data">
    Select File to upload:
    <input type="file" name="fileToUpload" id="fileToUpload">
    <input type="submit" value="Upload Image" name="submit">
</form>
```
then files saves to directory you inital in the Class

## 🎯 Host Files

urls.py
```python
 path('images/<slug:key>', sendfile)
 
 ''' path name can be anything you like we just need the key parameters '''
```
views.py
```python
def sendfile(request, key):
    callback = djs.find(key)
    if callback != None:
        data = json.loads(callback)
        if data['find']:
            with open(data['uri'], "rb") as f:
                return HttpResponse(f.read(), content_type='*/*')
        else:
            return HttpResponse('ERROR TO SEND FILE')
    else:
        return HttpResponse('File Not Found')
```
file.html
```html
<img src="/images/<key>" />
```
Thats All

## 🗜️ Test Code
Simply Test code by this commands
```shell
$ git clone https://github.com/E-RROR/djfiler
$ cd djfiler
$ python3 test-djfiler.py
```

