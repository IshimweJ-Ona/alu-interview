# Rain

This project calculates how much rainwater is retained between walls
represented as a list of non-negative integers.

## Function
### def rain(walls)
- `walls`: List of non-negative integers representing wall heights
  > """
        if not walls or len(walls) < 3:
         return 0
     """
    - if the list is empty or has fewer than 3 walls, then there is no water trapped so we return 0.

  > """ 
       left = 0
       right = len(walls) - 1
       left_max = 0
       right_max = 0
       total_water = 0
    """
    These are pointers and varialble initialization
    **left**: starts at the beginning of the list
    **right**: starts at the end of the list
    **left_max**: tallest wall seen so far from the left
    **right_max**: tallest wall seen so far on the right
    **total**: accumulator for trapped water

  > """whie left < right:
    loop continues until the two pointers meet.
  > """if walls[left] < walls[right]:
    we always move the pointer on the shorter side, to help us determine how much water can be trapped.
  > """
       if walls[left] >= left_max:
          left_max = walls[left]
       else:
          total_water += left_max - walls[left]
       left += 1
    """
    If the current left wall is taller than anything before: 
      - Update **left_max**.
    Otherwise, water can be trapped: **left_max - walls[left]**
    Move the `left` pointer to the right
  > """
       if walls[right] >= right_max:
           right_max = walls[right]
       else:
           total_water += right_max - walls[right]
        right -= 1
    """
    Same logic but on the opposite side meaning the **right** side.
    Update **right_max** or trap water.
    Move the right **right** pointer to left.


- **Returns**: integer amount of water retained after the loop finishes, then we return the total trapped water.
