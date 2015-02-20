from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.sde import dashboard


class Invitations(horizon.Panel):
    name = _("Invitations")
    slug = "invitations"


dashboard.Sde.register(Invitations)
