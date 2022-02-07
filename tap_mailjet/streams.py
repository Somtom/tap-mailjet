"""Stream type classes for tap-mailjet."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_mailjet.client import mailjetStream

class MessageStream(mailjetStream):
    """Define custom stream."""
    primary_keys = ["ID"]
    name = "message"
    replication_key = "ArrivedAt"
    replication_request_param = "FromTS"
    schema = th.PropertiesList(
        th.Property(
            "ID",
            th.IntegerType,
            description="Unique numeric ID of this message.",
            required=True
        ),
        th.Property(
            "ArrivedAt",
            th.DateTimeType,
            description="Timestamp indicating when the message arrived in the recipient's mailbox.",
        ),
        th.Property(
            "AttachmentCount",
            th.IntegerType,
            description="Number of attachments detected for this message."
        ),
        th.Property(
            "AttemptCount",
            th.IntegerType,
            description="Number of attempts made to deliver this message."
        ),
        th.Property(
            "CampaignID",
            th.IntegerType,
            description="Unique numeric ID for the campaign this message is part of."
        ),
        th.Property(
            "ContactAlt",
            th.StringType,
            description="The email address of the contact, to which the message was sent. Displayed only when ShowContactAlt=true."
        ),
        th.Property(
            "ContactID",
            th.IntegerType,
            description="Unique numeric ID for the contact, to which the message was sent."
        ),
        th.Property(
            "Delay",
            th.NumberType,
            description="Delay between the message being processed and it being delivered (in milliseconds)."
        ),
        th.Property(
            "DestinationID",
            th.IntegerType,
            description="Unique numeric ID of the recipient email's domain."
        ),
        th.Property(
            "FilterTime",
            th.IntegerType,
            description="Time spent processing the text of the message (in milliseconds)."
        ),
        th.Property(
            "IsClickTracked",
            th.BooleanType,
            description="Indicates whether clicks are tracked for this message or not."
        ),
        th.Property(
            "IsHTMLPartIncluded",
            th.BooleanType,
            description="Indicates whether the message includes any HTML content (Html-part!=null) or not."
        ),
        th.Property(
            "IsOpenTracked",
            th.BooleanType,
            description="Indicates whether opens are tracked for this message or not."
        ),
        th.Property(
            "IsTextPartIncluded",
            th.BooleanType,
            description="Indicates whether the message includes a plain text part (Text-part!=null) or not."
        ),
        th.Property(
            "IsUnsubTracked",
            th.BooleanType,
            description="Indicates whether unsubscriptions are tracked for this message or not."
        ),
        th.Property(
            "MessageSize",
            th.IntegerType,
            description="Indicates the message size (in bytes)."
        ),
        th.Property(
            "SenderID",
            th.IntegerType,
            description="Unique numeric ID of the sender email address."
        ),
        th.Property(
            "SpamassassinScore",
            th.NumberType,
            description="SpamAssassin score for this message."
        ),
        th.Property(
            "SpamassRules",
            th.StringType,
            description="Matched SpamAssassin rules."
        ),
        th.Property(
            "StateID",
            th.IntegerType,
            description="""
            Unique numeric ID explaining why the message was not delivered successfully to the recipient. Only returned if the message was not delivered successfully.

            Possible values:
            
            1 = user unknown (recipient)
            2 = mailbox inactive (recipient)
            3 = quota exceeded (recipient)
            4 = invalid domain (domain)
            5 = no mail host (domain)
            6 = relay/access denied (domain)
            7 = sender blocked (spam)
            8 = content blocked (spam)
            9 = policy issue (spam)
            10 = system issue (system)
            11 = protocol issue (system)
            12 = connection issue (system)
            13 = greylisted (domain)
            14 = preblocked (Mailjet)
            15 = duplicate in campaign (Mailjet)
            16 = spam preblocked (Mailjet)
            17 = bad or empty template (content)
            18 = error in template language (content)
            19 = typofix (domain)
            20 = blacklisted (recipient)
            21 = spam reporter (recipient)
            """
        ),
        th.Property(
            "StatePermanent",
            th.BooleanType,
            description="Indicates whether the current state of the message is permanent (i.e. cannot be changed anymore) or not."
        ),
        th.Property(
            "Status",
            th.StringType,
            description="Current message status."
        ),
        th.Property(
            "Subject",
            th.StringType,
            description="The subject line for this message. Displayed only when ShowSubject=true."
        ),
        th.Property(
            "UUID",
            th.StringType,
            description="Unique 128-bit ID for this message."
        ),
    ).to_dict()


class ContactStream(mailjetStream):
    """Define custom stream."""
    primary_keys = ["ID"]
    name = "contact"
    # There is no way of filtering by updated timestamp so we always extract everything
    # in case records changed
    replication_key = None
    schema = th.PropertiesList(
        th.Property(
            "ID",
            th.IntegerType,
            description="Unique numeric ID of this contact.",
            required=True
        ),
        th.Property(
            "IsExcludedFromCampaigns",
            th.BooleanType,
            description="Indicates whether the contact is added to the exclusion list for campaigns or not. An excluded contact will not be receiving any marketing emails."
        ),
        th.Property(
            "Name",
            th.StringType,
            description="User-selected name for this contact."
        ),
        th.Property(
            "IsExcludedFromCampaigns",
            th.StringType,
            description="User-selected name for this contact."
        ),
        th.Property(
            "CreatedAt",
            th.DateTimeType,
            description="Indicates when the contact was added to the global contact list."
        ),
        th.Property(
            "DeliveredCount",
            th.IntegerType,
            description="Number of messages delivered to this contact."
        ),
        th.Property(
            "Email",
            th.StringType,
            description="Contact email address."
        ),
        th.Property(
            "ExclusionFromCampaignsUpdatedAt",
            th.StringType,
            description="Timestamp of the last time the exclusion status of this contact has changed."
        ),
        th.Property(
            "IsOptInPending",
            th.BooleanType,
            description="Indicates whether the contact's subscription to a contact list is pending or not."
        ),
        th.Property(
            "IsSpamComplaining",
            th.BooleanType,
            description="Indicates whether any spam complaints have been received for this contact or not."
        ),
        th.Property(
            "DeliveredCount",
            th.IntegerType,
            description="Number of messages delivered to this contact."
        ),
        th.Property(
            "LastActivityAt",
            th.DateTimeType,
            description="Timestamp of last registered activity for this contact - receiving an email, open, click, unsubscribe etc."
        ),
        th.Property(
            "LastUpdateAt",
            th.DateTimeType,
            description="Timestamp of the last time this contact's name or exclusion status was changed.",
        ),
    ).to_dict()


class ContactsListStream(mailjetStream):
    """Define custom stream."""
    primary_keys = ["ID"]
    name = "contactslist"
    # There is no way of filtering by updated timestamp so we always extract everything
    # in case records changed
    replication_key = None
    schema = th.PropertiesList(
        th.Property(
            "ID",
            th.IntegerType,
            description="Unique numeric ID of this contact list.",
            required=True
        ),
        th.Property(
            "IsDeleted",
            th.BooleanType,
            description="When true, the contact list will be marked as Deleted. Deleted lists can later be reinstated by updating this value to False."
        ),
        th.Property(
            "Name",
            th.StringType,
            description="User-specified name for this contact list (must be unique)."
        ),
        th.Property(
            "Address",
            th.StringType,
            description="Unique email address generated by Mailjet, which can be used only via Mailjet's SMTP server to reach all contacts in the list. The full address will be {address}@lists.mailjet.com."
        ),
        th.Property(
            "CreatedAt",
            th.DateTimeType,
            description="Timestamp of when the contact list was created.",
        ),
        th.Property(
            "SubscriberCount",
            th.IntegerType,
            description="Number of contacts registered in this contact list. Includes contacts that were unsubscribed from the list, as well as excluded ones."
        ),
    ).to_dict()


class CampaignDraftStream(mailjetStream):
    """Define custom stream."""
    primary_keys = ["ID"]
    name = "campaigndraft"
    # There is no way of filtering by updated timestamp so we always extract everything
    # in case records changed
    replication_key = None
    schema = th.PropertiesList(
        th.Property(
            "ID",
            th.IntegerType,
            description="Unique numeric ID of this campaign draft.",
            required=True
        ),
        th.Property(
            "AXFraction",
            th.NumberType,
            description="Fraction of an AB Testing campaign as a percentage of the total emails. Zero indicates the remainder."
        ),
        th.Property(
            "AXFractionName",
            th.StringType,
            description="Name of the AB Testing fraction."
        ),
        th.Property(
            "AXTesting",
            th.IntegerType,
            description="An ID reference to the respective AXTesting object."
        ),
        th.Property(
            "Current",
            th.IntegerType,
            description="Data ID of the current content."
        ),
        th.Property(
            "EditMode",
            th.StringType,
            description="""
            Edit mode for the campaign draft.

            Possible values:
            
            tool2 - Passport drag-and-drop template editor
            html2 - HTML editor in Passport
            mjml - MJML editor in Passport
            """
        ),
        th.Property(
            "IsStarred",
            th.BooleanType,
            description="Indicates whether the campaign draft is marked as Starred or not."
        ),
        th.Property(
            "IsTextPartIncluded",
            th.BooleanType,
            description="Indicates whether the draft email contains a text version or not."
        ),
        th.Property(
            "ReplyEmail",
            th.StringType,
            description="Reply-to email address for the campaign. Returned only if a reply-to email was specified."
        ),
        th.Property(
            "SenderName",
            th.StringType,
            description="Name of the sender, which will be visible to recipients."
        ),
        th.Property(
            "TemplateID",
            th.IntegerType,
            description="Unique numeric ID of the template the CampaignDraft was generated from, or as which it was last saved. Changing the template ID will not update the content of the CampaignDraft."
        ),
        th.Property(
            "Title",
            th.StringType,
            description="Internal title for this campaign draft."
        ),
        th.Property(
            "CampaignID",
            th.IntegerType,
            description="Unique numeric ID of the campaign linked to this campaign draft. Will only be returned if the draft is already sent."
        ),
        th.Property(
            "ContactsListID",
            th.IntegerType,
            description="Unique numeric ID for the contact list linked to this draft. Required for successful sending of the campaign."
        ),
        th.Property(
            "CreatedAt",
            th.DateTimeType,
            description="Timestamp indicating when the campaigndraft was created."
        ),
        th.Property(
            "DeliveredAt",
            th.DateTimeType,
            description="Timestamp indicating when the campaigndraft was delivered."
        ),
        th.Property(
            "Locale",
            th.StringType,
            description="Locale, in which the information is saved."
        ),
        th.Property(
            "ModifiedAt",
            th.DateTimeType,
            description="Timestamp indicating when the campaign draft was last modified."
        ),
        th.Property(
            "Preset",
            th.StringType,
            description="String, representing a JSON array of styles for this campaign draft. The API does not interpret the styles."
        ),
        th.Property(
            "SegmentationID",
            th.IntegerType,
            description="ID of the segment configuration (contactfilter) used for this campaign draft."
        ),
        th.Property(
            "Sender",
            th.StringType,
            description="Unique numeric ID of the sender email address."
        ),
        th.Property(
            "SenderEmail",
            th.StringType,
            description="Email address of the sender."
        ),
        th.Property(
            "Status",
            th.IntegerType,
            description="""
            Status of the campaign draft. Only campaign drafts in status Draft or Programmed can be scheduled and sent out via /campaigndraft/{draft_id}/schedule or /campaigndraft/{draft_id}/send.
            
            Possible values:
            
            -3 - AXCanceled
            -2 - Deleted
            -1 - Archived
            0 - Draft
            1 - Programmed (scheduled)
            2 - Sent
            3 - AXTested (AB Testing versions sent, but winning version not selected yet)
            4 - AXSelected (AB Testing winning version selected and sent)
            """
        ),
        th.Property(
            "Subject",
            th.StringType,
            description="Subject line for the campaign emails."
        ),
        th.Property(
            "Url",
            th.StringType,
            description="The URL, where an online version of the template can be found. A URL is automatically generated by Mailjet for marketing templates, after the campaign draft is sent."
        ),
        th.Property(
            "Used",
            th.BooleanType,
            description="Indicates whether the campaign draft (or a test email of it) has been sent or not."
        ),
    ).to_dict()


class CampaignStream(mailjetStream):
    """Define custom stream."""
    primary_keys = ["ID"]
    name = "campaign"
    replication_key = "CreatedAt"
    replication_request_param = 'FromTS'
    schema = th.PropertiesList(
        th.Property(
            "ID",
            th.IntegerType,
            description="Unique numeric ID of this campaign.",
            required=True
        ),
        th.Property(
            "CreatedAt",
            th.DateTimeType,
            description="Timestamp indicating when the campaign was created."
        ),
        th.Property(
            "CustomValue",
            th.StringType,
            description="Custom unique tag for this campaign."
        ),
        th.Property(
            "FirstMessageID",
            th.IntegerType,
            description="Unique numeric ID of the first sent message for this campaign."
        ),
        th.Property(
            "FromEmail",
            th.StringType,
            description="Sender email address for this campaign."
        ),
        th.Property(
            "FromID",
            th.IntegerType,
            description="Unique numeric ID for the sender email address."
        ),
        th.Property(
            "FromName",
            th.StringType,
            description="Sender name selected for this campaign."
        ),
        th.Property(
            "HasHtmlCount",
            th.IntegerType,
            description="Indicates whether the emails in this campaign have HTML content (1) or not (0)."
        ),
        th.Property(
            "HasTxtCount",
            th.IntegerType,
            description="Indicates whether the emails in this campaign have plain text content (1) or not (0)."
        ),
        th.Property(
            "ListID",
            th.IntegerType,
            description="Unique numeric ID of the contact list, to which this campaign was sent."
        ),
        th.Property(
            "NewsLetterID",
            th.IntegerType,
            description="Unique numeric ID of this campaign draft object linked to this campaign."
        ),
        th.Property(
            "SegmentationID",
            th.IntegerType,
            description="Unique numeric ID for the segmentation used for this campaign (see /contactfilter). Returned only if a segmentation is used for the campaign."
        ),
        th.Property(
            "SendEndAt",
            th.DateTimeType,
            description="Timestamp indicating when last message in this campaign was sent."
        ),
        th.Property(
            "SendStartAt",
            th.DateTimeType,
            description="Timestamp indicating when first message in this campaign was sent."
        ),
        th.Property(
            "SpamassScore",
            th.NumberType,
            description="SpamAssassin score for this campaign."
        ),
        th.Property(
            "Subject",
            th.StringType,
            description="Subject line used for the emails in this campaign."
        ),
        th.Property(
            "WorkflowID",
            th.IntegerType,
            description="Unique numeric ID of the automation workflow that triggered this campaign. Returned only if a workflow is used for the campaign."
        ),
    ).to_dict()


class ContactFilterStream(mailjetStream):
    """Define custom stream."""
    primary_keys = ["ID"]
    name = "contactfilter"
    # There is no way of filtering by updated timestamp so we always extract everything
    # in case records changed
    replication_key = None
    schema = th.PropertiesList(
        th.Property(
            "ID",
            th.IntegerType,
            description="Unique numeric ID of this segment.",
            required=True
        ),
        th.Property(
            "Description",
            th.StringType,
            description="A description of the segment you can add for convenience, or to easier understand its functionality."
        ),
        th.Property(
            "Expression",
            th.StringType,
            description="The rule, based on which the segment is calculated. Refer to our Segmentation Guide for detailed information on the syntax."
        ),
        th.Property(
            "Name",
            th.StringType,
            description="User-selected name for this segment."
        ),
        th.Property(
            "Status",
            th.StringType,
            description="Status of this segment. Indicates whether a segment was used for sending or not, or if it was deleted."
        ),
    ).to_dict()


class TemplateStream(mailjetStream):
    """Define custom stream."""
    primary_keys = ["ID"]
    name = "template"
    # There is no way of filtering by updated timestamp so we always extract everything
    # in case records changed
    replication_key = None
    schema = th.PropertiesList(
        th.Property(
            "ID",
            th.IntegerType,
            description="Unique numeric ID of this template.",
            required=True
        ),
        th.Property(
            "Author",
            th.StringType,
            description="The name of the template author."
        ),
        th.Property(
            "Categories",
            th.StringType,
            description="An array containing a list of strings indicating the categories, to which the template is associated."
        ),
        th.Property(
            "Copyright",
            th.StringType,
            description="The Copyright message."
        ),
        th.Property(
            "Description",
            th.StringType,
            description="Free text used as a description for this template."
        ),
        th.Property(
            "EditMode",
            th.IntegerType,
            description="""
            Edit mode for this template:
            
            1 - Passport drag-and-drop builder
            2 - Passport HTML builder
            3 - Passport Saved Section (snippet) builder
            4 - Passport MJML builder
            Default value: 2
            """
        ),
        th.Property(
            "IsStarred",
            th.BooleanType,
            description="Indicates whether this campaign is marked as starred or not."
        ),
        th.Property(
            "IsTextPartGenerationEnabled",
            th.BooleanType,
            description="Indicates whether the generation of a text version of the template will be enabled or not."
        ),
        th.Property(
            "Locale",
            th.StringType,
            description="The locale for this template (AnsiString)."
        ),
        th.Property(
            "Name",
            th.StringType,
            description="Internal name for this template."
        ),
        th.Property(
            "OwnerType",
            th.StringType,
            description="""
            Indicates the type of the template owner.
            
            Possible values:
            
            apikey - Templates and their content can be retrieved, edited and used only by the API Key they were created from.
            user - Templates created by the Master API Key. Templates and their content can be retrieved by the Master API Key, as well as all subaccount API Keys. However, they can be edited and used only by the Master API Key.
            global - Generic templates created by Mailjet visible in the Passport Template Gallery.
            """
        ),
        th.Property(
            "Presets",
            th.StringType,
            description="A JSON string containing the different pre-defined styles for this template."
        ),
        th.Property(
            "Purposes",
            th.StringType,
            description="An array indicating whether the template is a marketing, transactional or automation one. Upon POST request only the first value in the array is taken into account."
        ),
        th.Property(
            "OwnerId",
            th.IntegerType,
            description="The UserID associated with the owner of this template."
        ),
        th.Property(
            "Previews",
            th.StringType,
            description="A JSON array containing Data ID's for the previews."
        ),
        th.Property(
            "CreatedAt",
            th.DateTimeType,
            description="Timestamp indicating when the template was created."
        ),
        th.Property(
            "LastUpdatedAt",
            th.DateTimeType,
            description="Timestamp indicating when the template was last updated."
        ),
    ).to_dict()


class BounceStatisticsStream(mailjetStream):
    """Define custom stream."""
    primary_keys = ["ID"]
    name = "bouncestatistics"
    replication_key = "BouncedAt"
    replication_request_param = "FromTS"
    schema = th.PropertiesList(
        th.Property(
            "ID",
            th.IntegerType,
            description="Unique numeric ID of this template.",
            required=True
        ),
        th.Property(
            "BouncedAt",
            th.DateTimeType,
            description="Timestamp indicating when the bounce event occurred."
        ),
        th.Property(
            "CampaignID",
            th.IntegerType,
            description="Unique numeric ID of the campaign this bounce event is linked to."
        ),
        th.Property(
            "ContactID",
            th.IntegerType,
            description="Unique numeric ID of the contact this bounce event is linked to."
        ),
        th.Property(
            "IsBlocked",
            th.BooleanType,
            description="Indicates whether the contact was blocked as a result of this bounce or not."
        ),
        th.Property(
            "IsStatePermanent",
            th.BooleanType,
            description="Indicates whether this is a permanent (hard) bounce or not."
        ),
        th.Property(
            "StateID",
            th.IntegerType,
            description="""
            State of the message after the bounce event:
            
            1 = user unknown (recipient)
            2 = mailbox inactive (recipient)
            3 = quota exceeded (recipient)
            4 = invalid domain (domain)
            5 = no mail host (domain)
            6 = relay/access denied (domain)
            7 = sender blocked (spam)
            8 = content blocked (spam)
            9 = policy issue (spam)
            10 = system issue (system)
            11 = protocol issue (system)
            12 = connection issue (system)
            13 = greylisted (domain)
            14 = preblocked (Mailjet)
            15 = duplicate in campaign (Mailjet)
            16 = spam preblocked (Mailjet)
            17 = bad or empty template (content)
            18 = error in template language (content)
            19 = typofix (domain)
            20 = blacklisted (recipient)
            21 = spam reporter (recipient)
            """
        ),
    ).to_dict()


class ClickStatisticsStream(mailjetStream):
    """Define custom stream."""
    primary_keys = ["ID"]
    name = "clickstatistics"
    replication_key = "ClickedAt"
    replication_request_param = "FromTS"
    schema = th.PropertiesList(
        th.Property(
            "ID",
            th.IntegerType,
            description="Unique numeric ID of this template.",
            required=True
        ),
        th.Property(
            "ClickedAt",
            th.DateTimeType,
            description="Timestamp indicating when the click event occurred."
        ),
        th.Property(
            "ClickedDelay",
            th.IntegerType,
            description="Delay (in seconds) between the message being opened and the URL link being clicked."
        ),
        th.Property(
            "ContactID",
            th.IntegerType,
            description="Unique numeric ID of the contact this click event is linked to."
        ),
        th.Property(
            "MessageID",
            th.IntegerType,
            description="Unique numeric ID of the message this click event is linked to."
        ),
        th.Property(
            "Url",
            th.StringType,
            description="The URL that generated this click event."
        ),
        th.Property(
            "UserAgentID",
            th.IntegerType,
            description="Unique numeric ID for the user agent (browser) used for this click event."
        ),
    ).to_dict()


class OpenInformationStream(mailjetStream):
    """Define custom stream."""
    primary_keys = ["ID"]
    name = "openinformation"
    replication_key = "OpenedAt"
    replication_request_param = "FromTS"
    schema = th.PropertiesList(
        th.Property(
            "ID",
            th.IntegerType,
            description="Unique numeric ID of this template.",
            required=True
        ),
        th.Property(
            "ArrivedAt",
            th.IntegerType,
            description="Timestamp indicating when the message arrived in the recipient's mailbox."
        ),
        th.Property(
            "CampaignID",
            th.IntegerType,
            description="Unique numeric ID of the campaign this open event is linked to."
        ),
        th.Property(
            "ContactID",
            th.IntegerType,
            description="Unique numeric ID of the contact this open event is linked to."
        ),
        th.Property(
            "MessageID",
            th.IntegerType,
            description="Unique numeric ID of the message this open event is linked to."
        ),
        th.Property(
            "OpenedAt",
            th.IntegerType,
            description="Timestamp indicating when the message was opened by the reader for the first time."
        ),
        th.Property(
            "UserAgentFull",
            th.IntegerType,
            description="Original User Agent String used to view this message."
        ),
        th.Property(
            "UserAgentID",
            th.IntegerType,
            description="Unique numeric ID for the user agent (browser) used for this click event."
        ),
    ).to_dict()
