"""REST client handling, including mailjetStream base class."""

from pathlib import Path
from typing import Optional, Iterable

from mailjet_rest import Client

from singer_sdk.streams import Stream


SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

class mailjetStream(Stream):
    """Stream class for mailjet streams."""
    page = 0
    limit = 1000
    # Request parameter used for filtering the replication state
    replication_request_param = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        api_key = self.config.get("api_key")
        api_secret = self.config.get("api_secret")
        self.conn = Client(
            auth=(api_key, api_secret),
            version = 'v3'
        )
        self.client = getattr(self.conn, self.name)

    def get_records(self, context: Optional[dict]) -> Iterable[dict]:
        """Return a generator of row-type dictionary objects.

        The optional `context` argument is used to identify a specific slice of the
        stream if partitioning is required for the stream. Most implementations do not
        require partitioning and should ignore the `context` argument.
        """
        filters = {
            'Limit': 1000
        }
        if self.replication_key and self.replication_request_param:
            filters[self.replication_request_param] = self.get_starting_replication_key_value(context)

        self.logger.info(filters)
        self.logger.info(self.get_starting_replication_key_value(context))

        has_more = True
        while has_more:
            filters['Offset'] = self.page * self.limit
            res = self.client.get(filters=filters)
            data = res.json()
            for row in data['Data']:
                yield row

            self.page += 1
            has_more = data.get('Count', 0) == self.limit

