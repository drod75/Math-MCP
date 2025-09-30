from fastapi import APIRouter, HTTPException
from typing import List
import numpy as np

basic_math_router = APIRouter(
    prefix="/basic_math",
    tags=["basic_math"],
    responses={404: {"description": "Not Found"}},
)


@basic_math_router.get("/addition")
async def addition(
    q: List[int | float],
):
    """Calculate the sum of a list of numbers.

    This endpoint takes a query parameter `q` which is a list of numbers
    and returns their sum.

    Parameters
    ----------
    q : List[int | float]
        A list of numbers (integers or floats) to be added together.

    Returns
    -------
    float
        The sum of all the numbers in the input list.

    Raises
    ------
    HTTPException
        If any error occurs during the summation process.
    """
    try:
        return np.sum(q)
    except Exception as E:
        raise HTTPException(status_code=400, detail=f"{E}")


@basic_math_router.get("/subtraction")
async def subtraction(
    q1: List[int | float],
    q2: List[int | float],
):
    """Perform element-wise subtraction of two lists of numbers.

    This endpoint takes two query parameters, `q1` and `q2`, which are two lists
    of numbers. It performs element-wise subtraction (q1 - q2).

    Parameters
    ----------
    q1 : List[int | float]
        A list of numbers from which to subtract.
    q2 : List[int | float]
        A list of numbers to subtract.

    Returns
    -------
    npt.NDArray[np.number]
        An array of numbers representing the result of the subtraction.
        This is serialized to a JSON list.

    Raises
    ------
    HTTPException
        If any error occurs during the subtraction, for example, if the
        lists have different lengths.
    """
    try:
        return np.subtract(q1, q2)
    except Exception as E:
        raise HTTPException(status_code=400, detail=f"{E}")
