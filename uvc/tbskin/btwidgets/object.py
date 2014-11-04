# -*- coding: utf-8 -*-

from zeam.form.ztk.widgets import object as obj
from grokcore.component import adapts, name
from . import getTemplate
from uvc.tbskin.skin import ITBSkinLayer
from zope.interface import Interface


class ObjectFieldWidget(obj.FieldWidget):
    adapts(obj.ObjectField, Interface, ITBSkinLayer)
    template = getTemplate('objectfieldwidget.cpt')


class ObjectDisplayWidget(ObjectFieldWidget):
    name('display')
