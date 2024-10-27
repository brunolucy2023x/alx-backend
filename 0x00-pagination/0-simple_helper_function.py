#!/usr/bin/env python3
"""
Simple helper function named index_range
takes two arguments page and page_size.
Returns a tuple of size two (start index, end index)
corresponding to the range of indexes to return in a list
for those particular pagination parameters.

Author: Bruno Owino
"""
from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of size two (start index, end index)
    for the given page and page size.
    
    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.
    
    Returns:
        Tuple[int, int]: A tuple containing the start and end indexes.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
