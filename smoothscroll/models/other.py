from typing import TypeVar

from easing_functions.easing import EasingBase

EasingFunction = TypeVar('EasingFunction', bound=EasingBase)
