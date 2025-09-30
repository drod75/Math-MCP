from src.api.routers.algebra import algebra_router
from src.api.routers.basic_math import basic_math_router
from src.api.routers.calculus import calculus_router
from src.api.routers.linear_algebra import linear_algebra_router
from src.api.routers.probability import probability_router
from src.api.routers.statistics import statistics_router
from src.api.routers.trigonometry import trigonometry_router
from fastapi import APIRouter

router_app = APIRouter(prefix="/api")
router_app.include_router(algebra_router)
router_app.include_router(basic_math_router)
router_app.include_router(calculus_router)
router_app.include_router(linear_algebra_router)
router_app.include_router(probability_router)
router_app.include_router(statistics_router)
router_app.include_router(trigonometry_router)
