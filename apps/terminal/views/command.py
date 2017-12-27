# -*- coding: utf-8 -*-
#

from django.views.generic import ListView
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext as _

from common.mixins import DatetimeSearchMixin
from ..models import Command
from .. import utils
from ..backends import get_command_store

__all__ = ['CommandListView']
command_store = get_command_store()


class CommandListView(DatetimeSearchMixin, ListView):
    model = Command
    template_name = "terminal/command_list.html"
    context_object_name = 'command_list'
    paginate_by = settings.CONFIG.DISPLAY_PER_PAGE
    command = user = asset = system_user = ""
    date_from = date_to = None
    date_format = '%m/%d/%Y'

    def get_queryset(self):
        filter_kwargs = dict()
        filter_kwargs['date_from'] = self.date_from
        filter_kwargs['date_to'] = self.date_to
        if self.user:
            filter_kwargs['user'] = self.user
        if self.asset:
            filter_kwargs['asset'] = self.asset
        if self.system_user:
            filter_kwargs['system_user'] = self.system_user
        if self.command:
            filter_kwargs['input'] = self.command
        if filter_kwargs:
            self.queryset = command_store.filter(**filter_kwargs)
        return self.queryset

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Terminal'),
            'action': _('Command list'),
            'user_list': utils.get_user_list_from_cache(),
            'asset_list': utils.get_asset_list_from_cache(),
            'system_user_list': utils.get_system_user_list_from_cache(),
            'command': self.command,
            'date_from': self.date_from,
            'date_to': self.date_to,
            'username': self.user,
            'asset': self.asset,
            'system_user': self.system_user,
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)





