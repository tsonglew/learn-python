from flask import Flask
from flask_qiniustorage import Qiniu

QINIU_ACCESS_KEY = ''
QINIU_SECRET_KEY = ''
QINIU_BUCKET_NAME = ''
QINIU_BUCKET_DOMAIN = ''

app = Flask(__name__)
app.config.from_object(__name__)
qiniu_store = Qiniu(app)
# 或者
# qiniu_store = Qiniu()
# qiniu_store.init_app(app)

# 保存文件到七牛
@app.route('/save')
def save():
    data = 'data to save'
    filename = 'filename'
    ret, info = qiniu_store.save(data, filename)
    return str(ret)

# 删除七牛空间中的文件
@app.route('/delete')
def delete():
    filename = 'filename'
    ret, info = qiniu_store.delete(filename)
    return str(ret)

# 根据文件名获取对应的公开URL
@app.route('/url')
def url():
    filename = 'filename'
    return qiniu_store.url(filename)
