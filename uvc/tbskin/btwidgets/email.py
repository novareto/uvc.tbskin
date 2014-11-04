# -*- coding: utf-8 -*-

from zeam.form.ztk.widgets import email
from grokcore.component import adapts, name
from zope.interface import Interface
from uvc.tbskin.skin import ITBSkinLayer


class EmailWidget(email.EmailWidget):
    adapts(email.EmailField, Interface, ITBSkinLayer)


class EmailDisplayWidget(email.EmailDisplayWidget):
    adapts(email.EmailField, Interface, ITBSkinLayer)
    name('display')
