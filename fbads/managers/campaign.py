# coding: utf-8
from fbads.managers.base import Manager
from fbads.resources.campaign import CampaignResource


class CampaignManager(Manager):
    resource_class = CampaignResource
    resource_name = 'adcampaign'

    def _get_api_path(self, object_id):
        return '{0}'.format(object_id)

    def list(self, fields=['id', 'name', 'start_time', 'end_time', 'daily_budget', 'lifetime_budget']):
        return super(CampaignManager, self).list(fields=fields)

    def add(self, name, campaign_status, daily_budget=None, lifetime_budget=None, start_time=None, end_time=None, redownload=False):
        assert not redownload  # if redownload is True, must instantiate a resource_class object... later

        payload = {
            'name': name,
            'campaign_status': campaign_status,
            'redownload': redownload,
        }

        # from decimal to cents
        if daily_budget:
            payload.update({
                'daily_budget': int(daily_budget * 100),
            })

        if lifetime_budget:
            payload.update({
                'lifetime_budget': int(lifetime_budget * 100),
            })

        # from datetime to ISO
        if start_time:
            payload.update({
                'start_time': start_time.isoformat(),
            })

        if end_time:
            payload.update({
                'end_time': end_time.isoformat(),
            })

        return super(CampaignManager, self).add(
            payload=payload
        )