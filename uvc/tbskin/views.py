# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GMBH
# ck@novareto.de

import uvclight
import megrok.pagetemplate as pt

from .skin import ITBSkinLayer
from cromlech.browser import ITemplate
from dolmen.location import get_absolute_url
from grokcore.component import adapter, implementer, MultiAdapter
from urllib import urlencode
from uvc.layout.forms import Form, GroupForm, SubForm, Wizard
from z3c.table.batch import BatchProvider
from z3c.table.interfaces import ITable
from zope.interface import Interface


class FormMacros(uvclight.View):
    uvclight.context(Interface)
    template = uvclight.get_template('formtemplate.cpt', __file__)


class FieldMacros(uvclight.View):
    uvclight.context(Interface)
    template = uvclight.get_template('fieldtemplates.cpt', __file__)


@adapter(Form, ITBSkinLayer)
@implementer(ITemplate)
def FormTemplate(context, request):
    return uvclight.get_template('formtemplate.cpt', __file__)


@adapter(SubForm, ITBSkinLayer)
@implementer(ITemplate)
def SubFormTemplate(context, request):
    return uvclight.get_template('subformtemplate.cpt', __file__)


@adapter(GroupForm, ITBSkinLayer)
@implementer(ITemplate)
def GroupFormTemplate(context, request):
    return uvclight.get_template('groupformtemplate.cpt', __file__)


@adapter(Wizard, ITBSkinLayer)
@implementer(ITemplate)
def WizardTemplate(context, request):
    return uvclight.get_template('wizardtemplate.cpt', __file__)


class CustomBatch(BatchProvider, MultiAdapter):
    uvclight.adapts(Interface, ITBSkinLayer, ITable)
    uvclight.name('batch')

    def renderBatchLink(self, batch, cssClass=None):
        args = self.getQueryStringArgs()
        args[self.table.prefix + '-batchStart'] = batch.start
        args[self.table.prefix + '-batchSize'] = batch.size
        query = urlencode(sorted(args.items()))
        tableURL = get_absolute_url(self.table, self.request)
        idx = batch.index + 1
        css = ' class="%s"' % cssClass
        cssClass = cssClass and css or u''
        return '<li %s><a href="%s?%s"%s>%s</a><li>' % (
            cssClass, tableURL, query, cssClass, idx)

    def render(self):
        self.update()
        res = []
        append = res.append
        idx = 0
        lastIdx = len(self.batchItems)
        for batch in self.batchItems:
            idx += 1
            # build css class
            cssClasses = []
            if batch and batch == self.batch:
                cssClasses.append('active')
            if idx == 1:
                cssClasses.append('first')
            if idx == lastIdx:
                cssClasses.append('last')

            if cssClasses:
                css = ' '.join(cssClasses)
            else:
                css = None

            # render spaces
            if batch is None:
                append(self.batchSpacer)
            elif idx == 1:
                # render first
                append(self.renderBatchLink(batch, css))
            elif batch == self.batch:
                # render current
                append(self.renderBatchLink(batch, css))
            elif idx == lastIdx:
                # render last
                append(self.renderBatchLink(batch, css))
            else:
                append(self.renderBatchLink(batch))
        return u'<ul>%s</ul>' % (''.join(res))
