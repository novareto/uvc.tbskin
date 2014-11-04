# -*- coding: utf-8 -*-

from zeam.form.ztk.widgets import text
from grokcore.component import adapts, name
from . import getTemplate
from zope.interface import Interface
from uvc.tbskin.skin import ITBSkinLayer


class TextareaWidget(text.TextareaWidget):
    adapts(text.TextField, Interface, ITBSkinLayer)
    template = getTemplate('textareawidget.cpt')
    defaultHtmlClass = ['field', 'field-text', 'form-control']


class DisplayTextareaWidget(TextareaWidget):
    name('display')
    template = getTemplate('pre_text.cpt')
