# QR Code Example

https://pypi.org/project/qrcode/


```
cd qrcode

pyenv shell 3.14.2

python --version

python -m venv .venv

source .venv/bin/activate

which python

pip install --upgrade pip

pip install "qrcode[pil]"
```

**Test the CLI:** 

```
qr www.google.com > google_qr.png
```

**Write code. Run it using:** 

```
python example_qrcode.py
```

**Deactivate**

```
deactivate
```