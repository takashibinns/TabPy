import json
from tabpy.tabpy_server.app.app_parameters import SettingsParameters
from tabpy.tabpy_server.handlers import ManagementHandler


class ServiceInfoHandler(ManagementHandler):
    def initialize(self, app):
        super(ServiceInfoHandler, self).initialize(app)

    def get(self):
        if self.should_fail_with_not_authorized():
            self.fail_with_not_authorized()
            return

        self._add_CORS_header()
        info = self.settings
        info["description"] = self.tabpy_state.get_description()
        info["creation_time"] = self.tabpy_state.creation_time
        info["name"] = self.tabpy_state.name
        info["versions"] = self.settings[SettingsParameters.ApiVersions]
        self.write(json.dumps(info))
