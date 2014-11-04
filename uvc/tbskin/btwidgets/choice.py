# -*- coding: utf-8 -*-

from zeam.form.ztk.widgets import choice
from grokcore.component import adapts, name
from . import getTemplate
from uvc.tbskin.skin import ITBSkinLayer
from zope.interface import Interface


class ChoiceFieldWidget(choice.ChoiceFieldWidget):
    adapts(choice.ChoiceField, Interface, ITBSkinLayer)
    template = getTemplate('choicefieldwidget.cpt')
    defaultHtmlClass = ['field', 'field-choice', 'form-control']


class ChoiceDisplayWidget(ChoiceFieldWidget):
    name('display')
    template = getTemplate('choicedisplaywidget.cpt')


class RadioFieldWidget(choice.RadioFieldWidget):
    adapts(choice.ChoiceField, Interface, ITBSkinLayer)
    name('radio')
    template = getTemplate('radiofieldwidget.cpt')
