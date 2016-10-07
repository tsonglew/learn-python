#-*- coding: utf-8 -*-

from flask import Flask
import settings

app = Flask(__name__)
# 静态文件
# 1. url_for('static', filename='style.css')
# 2. app = Flask(__name__, static_folder='/tmp')

# 加载配置变量的方式
# 1. 通过配置文件加载
app.config.from_object('settings')
# 2. 通过文件名字加载
app.config.from_pyfile('settings.py', silent=True)
# 3. 通过环境变量加载
# > export YOURAPPLICATION_SETTINGS='settings.py'
app.config.from_envvar('YOURAPPLICATION_SETTINGS')

# 动态参数 <converter: variable_name>
# string: 接受任何没有斜杠的文本(默认)
# path: 与默认相似, 但也接受斜杠
# uuid: 只接受uuid字符串
# any: 可指定多种路径, 但是需要传入参数
@app.route('/item/<id>/')
def item(id):
    return 'Item: {}'.format(id)

@app.route('/<any(a, b):page_name>/')
def page(page_name):
    return 'Page_Name: {}'.format(page_name)

# 调试模式
# 1.
app.debug = True
app.run()
# 2.
# app.run(debug=True)
