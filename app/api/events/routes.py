import uuid
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, Query, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.events.schemas import (
    EventCreateRequest,
    EventListAPIResponse,
    EventStatus,
    EventUpdateRequest,
    SingleEventAPIResponse,
)
from app.api.events.services import EventService
from app.api.events.views import event_list_response, single_event_response
from app.core.db.database import get_db_session

router = APIRouter(prefix="/events", tags=["Events"])


@router.post("", response_model=SingleEventAPIResponse, status_code=201)
async def create_event(
    payload: EventCreateRequest,
    session: AsyncSession = Depends(get_db_session),
) -> SingleEventAPIResponse:
    event = await EventService(session).create(payload)
    return single_event_response(event)


@router.get("", response_model=EventListAPIResponse)
async def list_events(
    status: Optional[EventStatus] = Query(default=None),
    start_from: Optional[datetime] = Query(default=None),
    start_to: Optional[datetime] = Query(default=None),
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    session: AsyncSession = Depends(get_db_session),
) -> EventListAPIResponse:
    events, total = await EventService(session).list_all(
        status, start_from, start_to, limit, offset
    )
    return event_list_response(events, total)


@router.get("/{event_id}", response_model=SingleEventAPIResponse)
async def get_event(
    event_id: uuid.UUID,
    session: AsyncSession = Depends(get_db_session),
) -> SingleEventAPIResponse:
    event = await EventService(session).get(event_id)
    return single_event_response(event)


@router.patch("/{event_id}", response_model=SingleEventAPIResponse)
async def update_event(
    event_id: uuid.UUID,
    payload: EventUpdateRequest,
    session: AsyncSession = Depends(get_db_session),
) -> SingleEventAPIResponse:
    event = await EventService(session).update(event_id, payload)
    return single_event_response(event)


@router.delete("/{event_id}", status_code=204)
async def delete_event(
    event_id: uuid.UUID,
    session: AsyncSession = Depends(get_db_session),
) -> Response:
    await EventService(session).delete(event_id)
    return Response(status_code=204)
