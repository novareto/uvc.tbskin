# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de 

import uvclight

from .skin import ITBSkinLayer
from zope.interface import Interface
from dolmen.forms.base import interfaces
from dolmen.forms.base.widgets import ActionWidget
from dolmen.forms.ztk.widgets.choice import RadioFieldWidget, ChoiceSchemaField


class UvcRadioFieldWidget(RadioFieldWidget):
    """ Simple Override for removing <br> between choices
    """
    uvclight.adapts(ChoiceSchemaField, Interface, ITBSkinLayer)
    template = uvclight.get_template('uvcradiofieldwidget.cpt', __file__)


    
class ActionWidget(ActionWidget):
    uvclight.adapts(
        interfaces.IAction,
        interfaces.IFieldExtractionValueSetting,
        ITBSkinLayer)

    template = uvclight.get_template('actionwidget.cpt', __file__)
    
    def htmlClass(self):
        return 'action btn'
