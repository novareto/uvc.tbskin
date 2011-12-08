# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GMBH
# ck@novareto.de

import grok

from zope.publisher.interfaces import browser
from uvc.layout.layout import IUVCSkin


class ITBSkinLayer(grok.IDefaultBrowserLayer):
    pass


class ITBSkin(IUVCSkin):
    grok.skin('tbskin')