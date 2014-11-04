# -*- coding: utf-8 -*-

from zeam.form.ztk.widgets import password as pwd
from grokcore.component import adapts
from . import getTemplate
from zope.interface import Interface
from uvc.tbskin.skin import ITBSkinLayer


class PasswordWidget(pwd.PasswordWidget):
    adapts(pwd.PasswordField, Interface, ITBSkinLayer)
    template = getTemplate('passwordwidget.cpt')
    defaultHtmlClass = ['field', 'field-password', 'form-control']
