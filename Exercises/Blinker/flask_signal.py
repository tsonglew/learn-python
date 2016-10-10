#-*- coding: utf-8 -*-

# 1. flask.template_rendered
# 模板渲染成功时发送, 与模板实例template、上下文的字典一起调用
def log_template_renders(sender, template, context, **extra):
    sender.logger.debug('Rendering template "%s" with context %s', template.name or 'string template', context)

from flask import template_rendered
template_rendered.connect(log_template_renders, app)

# 2. flask.request_started
# 建立请求上下文后，在请求处理开始前发送
def log_request(sender, **extra):
    sender.logger.debug('Request context is set up')

from flask import request_started
request_started.connect(log_request, app)

# 3. flask.request_finished
# 在响应发送给客户端之前发送
def log_response(sender, response, **extra):
    sender.logger.debug('Request context is about to close down. Response: %s', response)

from flask import request_finished
request_finished.connect(log_response, app)

# 4. flask.got_request_exception
# 在请求处理中抛出异常时发送, 异常本身通过exception传递到订阅函数
def log_exception(sender, exception, **extra):
    sender.logger.debug('Got exception during processing: %s', exception)

from flask import got_request_exception
got_requset_exception.connect(log_exception, app)

# 5. flask.request_tearing_down
# 在请求销毁时发送
def close_db_connection(sender, extra):
    session.close()

from flask import request_tearing_down
request_tearing_down.connect(close_db_connection, app)

# 6. flask.appcontext_tearing_down
# 在应用上下文销毁时发送
def close_db_connection(sender, **extra):
    session.close()

from flask import appcontext_tearing_down
appcontext_tearing_down.connect(close_db_connection, app)
