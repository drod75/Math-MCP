from fastapi import APIRouter, Query, HTTPException
from typing import Annotated, List, Union
import numpy as np

basic_math_router = APIRouter(
    prefix="/basic_math",
    tags=["basic_math"],
    responses={404: {"description": "Not Found"}},
)


@basic_math_router.get("/addition")
async def addition(
    q: Annotated[
        List[Union[int, float]],
        Query(alias="numerical-array", title="List of numerical values"),
    ],
):
    """This Python function calculates the sum of a list of numerical values provided as a query parameter.

    Parameters
    ----------
    q : Annotated[
            List[Union[int, float]],
            Query(alias="numerical-array", title="List of numerical values"),
        ]
        The parameter `q` is a list of numerical values that are passed as a query parameter to the
    endpoint `/addition`. The values in the list can be integers or floats. The endpoint calculates the
    sum of all the numerical values in the list using NumPy's `np.sum` function.

    Returns
    -------
        The code defines a route for performing addition operation on a list of numerical values provided
    as a query parameter. The function takes a list of numerical values as input, converts it to a NumPy
    array, calculates the sum of the array elements, and returns the result.

    """
    try:
        array = np.array(q)
        return np.sum(array)
    except Exception as E:
        raise HTTPException(status_code=400, detail=f"{E}")


@basic_math_router.get("/subtraction")
async def subtraction(
    q1: Annotated[
        List[Union[int, float]],
        Query(alias="numerical-array-1", title="List of numerical values 1."),
    ],
    q2: Annotated[
        List[Union[int, float]],
        Query(alias="numerical-array-2", title="List of numerical values 2"),
    ],
):
    """This Python function performs subtraction on two arrays of numerical values provided as input.

    Parameters
    ----------
    q1 : Annotated[
            List[Union[int, float]],
            Query(alias="numerical-array-1", title="List of numerical values 1."),
        ]
        The parameter `q2` in the code snippet represents a list of numerical values 1. It is defined as a
    query parameter with an alias of "numerical-array-1" and a title of "List of numerical values 1".
    This parameter is expected to be a list containing elements that are either floats or ints.
    q2 : Annotated[
            List[Union[int, float]],
            Query(alias="numerical-array-2", title="List of numerical values 2"),
        ]
        The parameter `q2` in the code snippet represents a list of numerical values 2. It is defined as a
    query parameter with an alias of "numerical-array-2" and a title of "List of numerical values 2".
    This parameter is expected to be a list containing elements that are either floats or ints.

    Returns
    -------
        The code snippet defines an endpoint for subtraction operation where it takes two lists of
    numerical values as input and returns the result of subtracting the elements of the second list from
    the elements of the first list. The result returned is the element-wise subtraction of the two input
    arrays.

    """
    try:
        array1 = np.array(q1)
        array2 = np.array(q2)
        return np.subtract(array1, array2)
    except Exception as E:
        raise HTTPException(status_code=400, detail=f"{E}")
