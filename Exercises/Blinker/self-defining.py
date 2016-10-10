#-*- coding: utf-8 -*-

from blinker import Namespace
web_signals = Namespace()
large_file_saved = web_signals.signal('large-file-saved')
