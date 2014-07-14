# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GMBH
# ck@novareto.de

import uvclight
from uvc.layout.layout import IUVCBaseLayer
from zope.interface import Interface
from dolmen.location import get_absolute_url


class ITBSkinLayer(IUVCBaseLayer):
    pass


class Layout(uvclight.Layout):
    uvclight.context(Interface)
    uvclight.layer(ITBSkinLayer)
    uvclight.name('uvc.layout')

    template = uvclight.get_template('layout.cpt', __file__)

    def update(self):
        self.base = get_absolute_url(self.context, self.request)
        if IContainer.providedBy(self.context) and self.base[:-1] != '/':
            self.base = self.base + '/'
