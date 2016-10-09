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
