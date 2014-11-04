# -*- coding: utf-8 -*-

from zeam.form.ztk.widgets import number
from grokcore.component import adapts, name
from . import getTemplate
from zope.interface import Interface
from uvc.tbskin.skin import ITBSkinLayer


class NumberWidget(number.NumberWidget):
    adapts(number.IntegerField, Interface, ITBSkinLayer)
    template = getTemplate('numberwidget.cpt')
    defaultHtmlClass = ['field', 'field-number', 'form-control']


class CurrencyDisplayWidget(number.CurrencyDisplayWidget):
    adapts(number.CurrencyField, Interface, ITBSkinLayer)
    name('display')
    template = getTemplate('currencydisplaywidget.cpt')
