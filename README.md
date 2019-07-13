# 環境準備

- python の ver 確認

```bash
$ python -V
Python 3.6.5
```

- `requirements.txt`を使用して flask をインストール

```bash
$ pip install -r requirements.txt
Collecting flask (from -r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/9b/93/628509b8d5dc749656a9641f4caf13540e2cdec85276964ff8f43bbb1d3b/Flask-1.1.1-py2.py3-none-any.whl
Collecting itsdangerous>=0.24 (from flask->-r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/76/ae/44b03b253d6fade317f32c24d100b3b35c2239807046a4c953c7b89fa49e/itsdangerous-1.1.0-py2.py3-none-any.whl
Collecting Werkzeug>=0.15 (from flask->-r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/9f/57/92a497e38161ce40606c27a86759c6b92dd34fcdb33f64171ec559257c02/Werkzeug-0.15.4-py2.py3-none-any.whl
Collecting Jinja2>=2.10.1 (from flask->-r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/1d/e7/fd8b501e7a6dfe492a433deb7b9d833d39ca74916fa8bc63dd1a4947a671/Jinja2-2.10.1-py2.py3-none-any.whl
Collecting click>=5.1 (from flask->-r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/fa/37/45185cb5abbc30d7257104c434fe0b07e5a195a6847506c074527aa599ec/Click-7.0-py2.py3-none-any.whl
Collecting MarkupSafe>=0.23 (from Jinja2>=2.10.1->flask->-r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/f0/00/a6aea33f5598b080b86d6b6d1214b51afe3ffa6100b902d5aa465080083f/MarkupSafe-1.1.1-cp36-cp36m-macosx_10_6_intel.whl
Installing collected packages: itsdangerous, Werkzeug, MarkupSafe, Jinja2, click, flask
Successfully installed Jinja2-2.10.1 MarkupSafe-1.1.1 Werkzeug-0.15.4 click-7.0 flask-1.1.1 itsdangerous-1.1.0
```

- pip 確認

```bash
$ pip list
Package      Version
------------ -------
Click        7.0
Flask        1.1.1
itsdangerous 1.1.0
Jinja2       2.10.1
MarkupSafe   1.1.1
pip          19.1.1
setuptools   39.0.1
Werkzeug     0.15.4
```

- flask の起動

```bash
$ python src/main.py
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

- 起動確認 の起動

  - <http://127.0.0.1:5000/> にブラウザからアクセス
  - <http://127.0.0.1:5000/bye> にブラウザからアクセス
