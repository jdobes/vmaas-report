import json

from vmaas_report.rpm_backend import RpmBackend
from vmaas_report.vmaas_api import VmaasApi


class Evaluator:
    def __init__(self):
        self.vmaas_api = VmaasApi()
        self.rpm_backend = RpmBackend()

    def print_status(self):
        print("VMAAS_SERVER: %s" % self.vmaas_api.server)
        print("VMaaS server version: %s" % self.vmaas_api.get_version())
        db_change = json.loads(self.vmaas_api.get_db_change())
        print("Database data:")
        print("  CVEs changed: %s" % str(db_change["cve_changes"]))
        print("  Errata changed: %s" % str(db_change["errata_changes"]))
        print("  Repositories changed: %s" % str(db_change["repository_changes"]))
        print("  Last change: %s" % str(db_change["last_change"]))
        print("  Exported: %s" % str(db_change["exported"]))
    
    def evaluate_updates(self):
        pass
