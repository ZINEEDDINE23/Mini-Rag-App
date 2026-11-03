from fastapi import APIRouter
from helpers.config import get_settings
router=APIRouter()

@router.get('/welcom')
def welcom():
    app_settings=get_settings()
    return {
        'app_name':app_settings.APP_NAME.value,
        'app-version':app_settings.APP_VERSION.value

    }