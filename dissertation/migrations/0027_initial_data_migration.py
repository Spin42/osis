# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-11 10:25
from __future__ import unicode_literals
from base.models.serializable_model import format_data_for_migration, LOGGER
import logging

from dissertation.models.adviser import Adviser
from dissertation.models.dissertation_location import DissertationLocation
from dissertation.models.offer_proposition import OfferProposition
from dissertation.models.proposition_dissertation import PropositionDissertation
from dissertation.models.proposition_document_file import PropositionDocumentFile
from dissertation.models.proposition_offer import PropositionOffer
from dissertation.models.proposition_role import PropositionRole
from django.conf import settings
from osis_common.models.document_file import DocumentFile
from pika.exceptions import ChannelClosed, ConnectionClosed
from backoffice.queue import queue_sender
from django.db import migrations

QUEUE_NAME = "osis_portal"
LOGGER = logging.getLogger(settings.DEFAULT_LOGGER)


def migrate_initial_data_adviser(apps, schema_editor):
    advisers = list(Adviser.objects.all())
    if advisers:
        try:
            queue_sender.send_message(QUEUE_NAME, format_data_for_migration(advisers))
        except (ChannelClosed, ConnectionClosed):
            LOGGER.warning('QueueServer is not installed or not launched')


def migrate_initial_data_offer_proposition(apps, schema_editor):
    offer_propositions = list(OfferProposition.objects.all())
    if offer_propositions:
        try:
            queue_sender.send_message(QUEUE_NAME, format_data_for_migration(offer_propositions))
        except (ChannelClosed, ConnectionClosed):
            LOGGER.warning('QueueServer is not installed or not launched')


def migrate_initial_data_proposition(apps, schema_editor):
    propositions = list(PropositionDissertation.objects.all())
    if propositions:
        try:
            queue_sender.send_message(QUEUE_NAME, format_data_for_migration(propositions))
        except (ChannelClosed, ConnectionClosed):
            LOGGER.warning('QueueServer is not installed or not launched')


def migrate_initial_data_proposition_offer(apps, schema_editor):
    proposition_offers = list(PropositionOffer.objects.all())
    if proposition_offers:
        try:
            queue_sender.send_message(QUEUE_NAME, format_data_for_migration(proposition_offers))
        except (ChannelClosed, ConnectionClosed):
            LOGGER.warning('QueueServer is not installed or not launched')


def migrate_initial_data_proposition_role(apps, schema_editor):
    proposition_roles = list(PropositionRole.objects.all())
    if proposition_roles:
        try:
            queue_sender.send_message(QUEUE_NAME, format_data_for_migration(proposition_roles))
        except (ChannelClosed, ConnectionClosed):
            LOGGER.warning('QueueServer is not installed or not launched')


def migrate_initial_data_document_file(apps, schema_editor):
    document_files = list(DocumentFile.objects.all())
    if document_files:
        try:
            queue_sender.send_message(QUEUE_NAME, format_data_for_migration(document_files))
        except (ChannelClosed, ConnectionClosed):
            LOGGER.warning('QueueServer is not installed or not launched')


def migrate_initial_data_proposition_document_files(apps, schema_editor):
    proposition_document_files = list(PropositionDocumentFile.objects.all())
    if proposition_document_files:
        try:
            queue_sender.send_message(QUEUE_NAME, format_data_for_migration(proposition_document_files))
        except (ChannelClosed, ConnectionClosed):
            LOGGER.warning('QueueServer is not installed or not launched')


def migrate_initial_data_dissertation_location(apps, schema_editor):
    dissertation_locations = list(DissertationLocation.objects.all())
    if dissertation_locations:
        try:
            queue_sender.send_message(QUEUE_NAME, format_data_for_migration(dissertation_locations))
        except (ChannelClosed, ConnectionClosed):
            LOGGER.warning('QueueServer is not installed or not launched')


class Migration(migrations.Migration):

    dependencies = [
        ('dissertation', '0026_remove_propositiondissertation_offer_proposition'),
    ]

    operations = [
        migrations.RunPython(migrate_initial_data_adviser),
        migrations.RunPython(migrate_initial_data_offer_proposition),
        migrations.RunPython(migrate_initial_data_proposition),
        migrations.RunPython(migrate_initial_data_proposition_offer),
        migrations.RunPython(migrate_initial_data_proposition_role),
        migrations.RunPython(migrate_initial_data_dissertation_location),
        migrations.RunPython(migrate_initial_data_document_file),
        migrations.RunPython(migrate_initial_data_proposition_document_files),
    ]
