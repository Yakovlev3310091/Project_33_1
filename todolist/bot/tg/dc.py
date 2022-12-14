from dataclasses import dataclass
from typing import List

import marshmallow
import marshmallow_dataclass




@dataclass
class GetUpdatesResponse:
    ok: bool
    result: List[UpdateObj]  # todo

    class Meta:
        unknown = EXCLUDE


@dataclass
class SendMessageResponse:
    ok: bool
    result: Message  # todo

    class Meta:
        unknown = EXCLUDE