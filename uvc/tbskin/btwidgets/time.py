# -*- coding: utf-8 -*-

from zeam.form.ztk.widgets import time
from grokcore.component import adapts
from zope.interface import Interface
from uvc.tbskin.skin import ITBSkinLayer


class TimeFieldWidget(time.TimeFieldWidget):
    adapts(time.TimeField, Interface, ITBSkinLayer)
    defaultHtmlClass = ['field', 'field-time', 'form-control']


class TimeFieldDisplayWidget(time.TimeFieldDisplayWidget):
    adapts(time.TimeField, Interface, ITBSkinLayer)
