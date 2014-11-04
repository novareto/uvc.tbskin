# -*- coding: utf-8 -*-

from zeam.form.ztk.widgets import textline
from grokcore.component import adapts
from uvc.tbskin.skin import ITBSkinLayer
from zope.interface import Interface
from . import getTemplate


class TextLineWidget(textline.TextLineWidget):
    adapts(textline.TextLineField, Interface, ITBSkinLayer)
    template = getTemplate('textlinewidget.cpt')
    defaultHtmlClass = ['field', 'field-textline', 'form-control']
