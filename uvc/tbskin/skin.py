# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GMBH
# ck@novareto.de

import grok
from megrok import layout
from uvc.layout.layout import IUVCSkin
from zope.interface import Interface
from zope.publisher.interfaces import browser
from zope.container.interfaces import IContainer
from zope.traversing.browser import absoluteURL

grok.templatedir('templates')


class ITBSkinLayer(grok.IDefaultBrowserLayer):
    pass


class ITBSkin(ITBSkinLayer, IUVCSkin):
    grok.skin('tbskin')


class Layout(layout.Layout):
    grok.context(Interface)
    grok.layer(ITBSkinLayer)
    grok.name('uvc.layout')

    def update(self):
        self.base = absoluteURL(self.context, self.request)
        if IContainer.providedBy(self.context) and self.base[:-1] != '/':
            self.base = self.base + '/'
