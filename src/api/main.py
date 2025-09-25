from .routers.algebra import algebra_router
from .routers.basic_math import basic_math_router
from .routers.calculus import calculus_router
from .routers.linear_algebra import linear_algebra_router
from .routers.probability import probability_router
from .routers.statistics import statistics_router
from .routers.trigonometry import trigonometry_router
from fastapi import APIRouter

router_app = APIRouter()
router_app.include_router(algebra_router)
router_app.include_router(basic_math_router)
router_app.include_router(calculus_router)
router_app.include_router(linear_algebra_router)
router_app.include_router(probability_router)
router_app.include_router(statistics_router)
router_app.include_router(trigonometry_router)
