from __future__ import absolute_import, division, print_function

from stripe import api_requestor, util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import ListableAPIResource


class Invoice(
    CreateableAPIResource,
    UpdateableAPIResource,
    ListableAPIResource,
):
    OBJECT_NAME = "invoice"

    def attach(self, idempotency_key=None, **params):
        url = self.instance_url() + "/attach"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def detach(self, idempotency_key=None, **params):
        url = self.instance_url() + "/detach"
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self
