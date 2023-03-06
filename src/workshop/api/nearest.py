from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status

from ..models.auth import User
from ..models.nearest import Nearest, NearestCreate, NearestUpdate
from ..services.auth import get_current_user
from ..services.nearest import NearestService

router = APIRouter(
    prefix='/nearest',
    tags=['nearest'],
)

@router.get('/', response_model=List[Nearest])
def get_nearests(
        user: User = Depends(get_current_user),
        service: NearestService = Depends(),
):
        return service.get_list(user_id=user.id)

@router.post('/', response_model=Nearest)
def create_nearest(
        nearest_data: NearestCreate,
        user: User = Depends(get_current_user),
        service: NearestService = Depends(),
):
        print(user.id, nearest_data)
        return service.create(user_id=user.id, nearest_data=nearest_data)

@router.get('/{nearest_id}', response_model=Nearest)
def get_nearest(
        nearest_id: int,
        user: User = Depends(get_current_user),
        service: NearestService = Depends(),
):
        return service.get(user_id=user.id, nearest_id=nearest_id)

@router.put('/{nearest_id}', response_model=Nearest)
def update_nearests(
        nearest_id: int,
        nearest_data: NearestUpdate,
        user: User = Depends(get_current_user),
        service: NearestService = Depends()
):
        return service.update(
            user_id=user.id,
            nearest_id=nearest_id,
            nearest_data=nearest_data
        )

@router.delete('/{nearest_id}')
def delete_nearests(
        nearest_id: int,
        user: User = Depends(get_current_user),
        service: NearestService = Depends(),
):
    service.delete(user_id=user.id, nearest_id=nearest_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)