# -*- coding: utf-8 -*-

from zeam.form.ztk.widgets import date
from grokcore.component import adapts
from zope.interface import Interface
from uvc.tbskin.skin import ITBSkinLayer


class DateFieldWidget(date.DateFieldWidget):
    adapts(date.DateField, Interface, ITBSkinLayer)
    defaultHtmlClass = ['field', 'field-date', 'form-control']


class DateFieldDisplayWidget(date.DateFieldDisplayWidget):
    adapts(date.DateField, Interface, ITBSkinLayer)
