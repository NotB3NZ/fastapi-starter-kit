from app.api.events.models import Event
from app.api.events.schemas import (
    EventListAPIResponse,
    EventListResponse,
    EventResponse,
    SingleEventAPIResponse,
)


def single_event_response(event: Event) -> SingleEventAPIResponse:
    return SingleEventAPIResponse(data=EventResponse.model_validate(event))


def event_list_response(events: list[Event], total: int) -> EventListAPIResponse:
    return EventListAPIResponse(
        data=EventListResponse(
            items=[EventResponse.model_validate(e) for e in events],
            total=total,
        )
    )
