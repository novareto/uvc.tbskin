# -*- coding: utf-8 -*-

from zeam.form.ztk.widgets import link
from grokcore.component import adapts, name
from . import getTemplate
from zope.interface import Interface
from uvc.tbskin.skin import ITBSkinLayer


class LinkFieldWidget(link.LinkFieldWidget):
    adapts(link.IField, Interface, ITBSkinLayer)
    name('link')
    template = getTemplate('linkfieldwidget.cpt')
