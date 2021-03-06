# -*- coding: utf-8 -*-
#
from rest_framework import serializers

from common.fields import ChoiceDisplayField
from common.serializers import AdaptedBulkListSerializer
from ..models import CommandFilter, CommandFilterRule, SystemUser
from orgs.mixins import BulkOrgResourceModelSerializer


class CommandFilterSerializer(BulkOrgResourceModelSerializer):
    rules = serializers.PrimaryKeyRelatedField(queryset=CommandFilterRule.objects.all(), many=True)
    system_users = serializers.PrimaryKeyRelatedField(queryset=SystemUser.objects.all(), many=True)

    class Meta:
        model = CommandFilter
        list_serializer_class = AdaptedBulkListSerializer
        fields = '__all__'


class CommandFilterRuleSerializer(BulkOrgResourceModelSerializer):
    serializer_choice_field = ChoiceDisplayField

    class Meta:
        model = CommandFilterRule
        fields = '__all__'
        list_serializer_class = AdaptedBulkListSerializer
