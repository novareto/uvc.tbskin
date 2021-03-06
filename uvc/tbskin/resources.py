# -*- coding: utf-8 -*-
# # Copyright (c) 2007-2011 NovaReto GmbH

import grok

from zope.interface import Interface
from megrok import resourceviewlet
from fanstatic import Library, Resource
from js.bootstrap import bootstrap_js, bootstrap_css
from js.jquery_tablesorter import tablesorter


library = Library('uvc.tbskin', 'static')
main_css = Resource(library, 'main.css', depends=[bootstrap_css])
main_js = Resource(library, 'main.js', depends=[bootstrap_js, tablesorter])


class TBSkinViewlet(resourceviewlet.ResourceViewlet):
    grok.context(Interface)
    resources = [main_css, main_js]
    grok.baseclass()

    def update(self):
        [x.need() for x in self.resources]
