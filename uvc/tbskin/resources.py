# -*- coding: utf-8 -*-
# # Copyright (c) 2007-2011 NovaReto GmbH

import grok

from zope.interface import Interface
from megrok import resourceviewlet
from fanstatic import Library, Resource
from js.bootstrap import bootstrap

library = Library('nva.tbskin', 'static')
main_css = Resource(library, 'main.css')


class TBSkinViewlet(resourceviewlet.ResourceViewlet):
    grok.context(Interface)
    resources = [main_css, bootstrap]

    def update(self):
        [x.need() for x in self.resources]
