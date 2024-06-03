# python_receiver
Python as Bridges communication with HTTP

## How to use
### Requirement :
- Python 3
### 1 Install module
```pip install -r requirements.txt```

### 2 Run Application
```python input_reveicer.py```

### 3 Send Request/ Data with GET
See in log : ```Running on http://192.168.xxx.xxx:5000``` place you cursor and open browser in your phone and write ```http://192.168.xxx.xxx:5000/scan_input?s=yout string here```

### 4 Send Request/ Data with POST
See in log : ```Running on http://192.168.xxx.xxx:5000``` place you cursor and open Postman in your phone and write in body payload JSON ```{"text":"yout string here"}``` send to ```http://192.168.xxx.xxx:5000/scan_input```

#### Noted :
- Http Connection Must in same Network
