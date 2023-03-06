from typing import List

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from .. import tables
from ..database import get_session
from ..models.nearest import NearestCreate, NearestUpdate


class NearestService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, user_id: int, nearest_id: int) -> tables.Nearest:
        nearest = (
            self.session
            .query(tables.Nearest)
            .filter_by(
                id=nearest_id,
                user_id=user_id,
            )
            .first()
        )
        if not nearest:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return nearest

    def get_list(self, user_id: int) -> List[tables.Nearest]:
        query = (
            self.session
            .query(tables.Nearest)
            .filter_by(user_id=user_id))
        nearests = query.all()
        return nearests

    def get(self, user_id: int, nearest_id: int) -> tables.Nearest:
        return self._get(user_id, nearest_id)

    def create_many(self, user_id: int, nearests_data: List[NearestCreate]) -> List[tables.Operation]:
        nearests = [
            tables.Nearest(
                **nearest_data.dict(),
                user_id=user_id,
            )
            for nearest_data in nearests_data
        ]
        self.session.add_all(nearests)
        self.session.commit()
        return nearests
    def create(self, user_id: int, nearest_data: NearestCreate) -> tables.Nearest:
        nearest = tables.Nearest(
            **nearest_data.dict(),
            user_id=user_id,
        )
        self.session.add(nearest)
        self.session.commit()
        return nearest

    def update(self, user_id: int, nearest_id: int, nearest_data: NearestUpdate) -> tables.Nearest:
        nearest = self._get(user_id, nearest_id)
        for field, value in nearest_data:
            setattr(nearest, field, value)
        self.session.commit()
        return nearest

    def delete(self, user_id: int, nearest_id: int):
        nearest = self._get(user_id, nearest_id)
        self.session.delete(nearest)
        self.session.commit()
