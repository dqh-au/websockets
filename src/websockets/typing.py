from __future__ import annotations

import http
import logging
from typing import Any, List, NewType, Optional, Tuple, Union


__all__ = [
    "Data",
    "LoggerLike",
    "StatusLike",
    "Origin",
    "Subprotocol",
    "ExtensionName",
    "ExtensionParameter",
]


# Public types used in the signature of public APIs

Data = Union[str, bytes]
"""Types supported in a WebSocket message:
:class:`str` for a Text_ frame, :class:`bytes` for a Binary_.

.. _Text: https://www.rfc-editor.org/rfc/rfc6455.html#section-5.6
.. _Binary : https://www.rfc-editor.org/rfc/rfc6455.html#section-5.6

"""


LoggerLike = Union[logging.Logger, logging.LoggerAdapter[Any]]
"""Types accepted where a :class:`~logging.Logger` is expected."""


StatusLike = Union[http.HTTPStatus, int]
"""
Types accepted where an :class:`~http.HTTPStatus` is expected."""


Origin = NewType("Origin", str)
"""Value of a ``Origin`` header."""


Subprotocol = NewType("Subprotocol", str)
"""Subprotocol in a ``Sec-WebSocket-Protocol`` header."""


ExtensionName = NewType("ExtensionName", str)
"""Name of a WebSocket extension."""


ExtensionParameter = Tuple[str, Optional[str]]
"""Parameter of a WebSocket extension."""


# Private types

ExtensionHeader = Tuple[ExtensionName, List[ExtensionParameter]]
"""Extension in a ``Sec-WebSocket-Extensions`` header."""


ConnectionOption = NewType("ConnectionOption", str)
"""Connection option in a ``Connection`` header."""


UpgradeProtocol = NewType("UpgradeProtocol", str)
"""Upgrade protocol in an ``Upgrade`` header."""
