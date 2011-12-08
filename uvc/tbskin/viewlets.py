# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GMBH
# ck@novareto.de

import grok
import uvcsite

from skin import ITBSkinLayer
from dolmen.app.breadcrumbs import crumbs
from uvc.layout.viewlets.flashmessages import FlashMessages

grok.templatedir('templates')


class Breadcrumbs(crumbs.Breadcrumbs):
    grok.layer(ITBSkinLayer)
    grok.viewletmanager(uvcsite.IAboveContent)
    grok.order(19)


class FlashMessages(FlashMessages):
    grok.layer(ITBSkinLayer)
    grok.viewletmanager(uvcsite.IAboveContent)
