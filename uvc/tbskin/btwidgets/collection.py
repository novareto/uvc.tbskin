# -*- coding: utf-8 -*-

from zeam.form.ztk.widgets import collection as col
from grokcore.component import adapts, name
from . import getTemplate
from zope.interface import Interface
from uvc.tbskin.skin import ITBSkinLayer



class MultiGenericFieldWidget(col.MultiGenericFieldWidget):
    adapts(col.ICollectionField, Interface, Interface, ITBSkinLayer)
    defaultHtmlClass = ['field', 'field-choice', 'form-control']
    template = getTemplate('multigenericfieldwidget.cpt')


class ListGenericFieldWidget(col.ListGenericFieldWidget):
    adapts(col.ListField, Interface, Interface, ITBSkinLayer)
    defaultHtmlClass = ['field', 'field-choice', 'form-control']
    template = getTemplate('multigenericfieldwidget.cpt')


class MultiGenericDisplayFieldWidget(MultiGenericFieldWidget):
    name('display')
    template = getTemplate('multigenericdisplayfieldwidget.cpt')


class MultiObjectFieldWidget(col.MultiObjectFieldWidget):
    adapts(col.ICollectionField, col.ObjectField, Interface, ITBSkinLayer)
    defaultHtmlClass = ['field', 'field-choice', 'form-control']
    template = getTemplate('multiobjectfieldwidget.cpt')


class ListObjectFieldWidget(col.ListObjectFieldWidget):
    adapts(col.ListField, col.ObjectField, Interface, ITBSkinLayer)
    defaultHtmlClass = ['field', 'field-choice', 'form-control']
    template = getTemplate('listobjectfieldwidget.cpt')


class RegularMultiObjectFieldWidget(MultiGenericFieldWidget):
    name('input-list')


class RegularListObjectFieldWidget(ListGenericFieldWidget):
    name('input-list')


class MultiChoiceFieldWidget(col.MultiChoiceFieldWidget):
    adapts(col.SetField, col.ChoiceField, Interface, ITBSkinLayer)
    template = getTemplate('multichoicefieldwidget.cpt')


class MultiSelectFieldWidget(MultiChoiceFieldWidget):
    name('multiselect')
    template = getTemplate('multiselectfieldwidget.cpt')


class MultiChoiceDisplayFieldWidget(MultiChoiceFieldWidget):
    name('display')
    template = getTemplate('multichoicedisplayfieldwidget.cpt')
