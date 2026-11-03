from fastapi import APIRouter
import os
router=APIRouter()

@router.get('/welcom')
def welcom():
    app_name=os.getenv('APP_NAME'),
    app_version=os.getenv('APP_VERSION')
    return {
        'app_name':app_name,
        'app-version':app_version

    }