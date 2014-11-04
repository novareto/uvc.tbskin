# -*- coding: utf-8 -*-

from zeam.form.ztk.widgets import uri
from grokcore.component import adapts, name
from . import getTemplate
from zope.interface import Interface
from uvc.tbskin.skin import ITBSkinLayer


class URIWidget(uri.URIWidget):
    adapts(uri.URIField, Interface, ITBSkinLayer)
    template = getTemplate('uriwidget.cpt')


class URIDisplayWidget(uri.URIDisplayWidget):
    adapts(uri.URIField, Interface, ITBSkinLayer)
    name('display')
    template = getTemplate('uridisplaywidget.cpt')
