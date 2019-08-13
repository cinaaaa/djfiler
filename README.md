<p align="left">
    <img width="300" src="https://raw.githubusercontent.com/E-RROR/django-filer/master/d376573d-c0f3-4fde-8467-952d7ffada1d_200x200.png" />
</p>

<h1 align="left">Dj 'ango' Filer</h1>
<h2>An Easy Way To Upload Files To Django</h2>


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

# Import Django Filer
from djfiler import djfiler

# Initial Django Filer
djs = djfiler.Filer('/dir/of/uploades', True)

''' djs can be any name you like '''
```

Handle Upload Files In Any Format

```python
def home(request):
    if request.method == "POST":
        callback = djs.upload(file=request.FILES['file name uploaded'], name="Optional" )
        print(callback) # Its Returns {status:ok | fail,name: name of file ( Its Key Of File ),type: type of file }
```

Return Any File With A Simple Key (Key Is The String That We Return To You When Uploaded file)

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
Thats All
