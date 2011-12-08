# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GMBH
# ck@novareto.de

import grok

from skin import ITBSkin
from dolmen.app.breadcrumbs import crumbs

grok.templatedir('templates')


class Breadcrumbs(crumbs.Breadcrumbs):
    grok.layer(ITBSkin)