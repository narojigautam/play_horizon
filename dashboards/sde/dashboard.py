from django.utils.translation import ugettext_lazy as _

import horizon

class Sdepanels(horizon.PanelGroup):
    slug = "sdepanels"
    name = _("Sde Panels")
    panels = ("invitations",)

class Sde(horizon.Dashboard):
    name = _("Sde")
    slug = "sde"
    panels = (Sdepanels,)  # Add your panels here.
    default_panel = 'invitations'  # Specify the slug of the dashboard's default panel.


horizon.register(Sde)
