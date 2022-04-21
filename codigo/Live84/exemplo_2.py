from typing import Union, Optional


def soma(
    x: Union[str, float],
    y: Union[int, float]
) -> Optional[float]:
    return None if isinstance(x, str) else x + y


# soma('x', 'y')  # error
# soma(1.0+1j, 2.0)  # error

soma('batatas', 2)  # ok
soma(1, 2)  # ok
soma(1.0, 2.0)  # ok
