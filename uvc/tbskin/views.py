# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GMBH
# ck@novareto.de

import grok

import megrok.pagetemplate as pt
from skin import ITBSkin

from dolmen.forms.base import ApplicationForm 

grok.templatedir('templates')


class FormTemplate(pt.PageTemplate):
    grok.layer(ITBSkin)
    grok.view(ApplicationForm)
