from fastapi import APIRouter

api: APIRouter = APIRouter()

from . import controller
