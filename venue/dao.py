from venue.models import Venue
from core.dao import BaseDAO


def VenueDAO(BaseDAO):
    """Venue implementation of the BaseDAO."""

    MODEL_CLASS = Venue
    BATCH_SIZE = 1000
