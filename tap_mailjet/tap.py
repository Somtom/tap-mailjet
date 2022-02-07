"""mailjet tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers
from tap_mailjet.streams import (
    MessageStream,
    ContactStream, ClickStatisticsStream, OpenInformationStream, BounceStatisticsStream,
    TemplateStream, ContactFilterStream, CampaignStream, ContactsListStream,
    CampaignDraftStream,
)
STREAM_TYPES = [
    ContactStream,
    MessageStream,
    ContactsListStream,
    ContactFilterStream,
    CampaignDraftStream,
    CampaignStream,
    TemplateStream,
    BounceStatisticsStream,
    ClickStatisticsStream,
    OpenInformationStream,
]


class Tapmailjet(Tap):
    """mailjet tap class."""
    name = "tap-mailjet"
    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            description="API key to authenticate against the API service"
        ),
        th.Property(
            "api_secret",
            th.StringType,
            required=True,
            description="API secret to authenticate against the API service"
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync"
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
