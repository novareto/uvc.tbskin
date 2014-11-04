# -*- coding: utf-8 -*-

from zeam.form.ztk.widgets import bool
from grokcore.component import adapts
from . import getTemplate
from uvc.tbskin.skin import ITBSkinLayer
from zope.interface import Interface


class CheckBoxWidget(bool.CheckBoxWidget):
    adapts(bool.BooleanField, Interface, ITBSkinLayer)
    template = getTemplate('checkboxwidget.cpt')


class CheckBoxDisplayWidget(bool.CheckBoxDisplayWidget):
    adapts(bool.BooleanField, Interface, ITBSkinLayer)
