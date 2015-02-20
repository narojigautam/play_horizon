from horizon import tabs

from openstack_dashboard.dashboards.sde.invitations import tabs as sde_tabs


class IndexView(tabs.TabbedTableView):
    tab_group_class = sde_tabs.MypanelTabs
    template_name = 'sde/invitations/index.html'

    def get_data(self, request, context, *args, **kwargs):
        # Add data to the context here...
        return context
