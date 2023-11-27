#  Copyright (C) 2021-2023 pytest-qgis Contributors.
#
#
#  This file is part of pytest-qgis.
#
#  pytest-qgis is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 2 of the License, or
#  (at your option) any later version.
#
#  pytest-qgis is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with pytest-qgis.  If not, see <https://www.gnu.org/licenses/>.
import typing
from typing import Dict, List

from qgis import _core
from qgis.core import Qgis
from qgis.gui import QgsMessageBar as QgsMessageBarOriginal
from qgis.PyQt.QtCore import QObject


class MockMessageBar(QgsMessageBarOriginal):
    """Mocked message bar to hold the messages."""

    def __init__(self) -> None:
        super().__init__()
        self.messages: Dict[int, List[str]] = {
            Qgis.Info: [],
            Qgis.Warning: [],
            Qgis.Critical: [],
            Qgis.Success: [],
        }

    def get_messages(self, level: int) -> List[str]:
        """Used to test which messages have been logged."""
        return self.messages[level]

    @typing.overload
    def pushMessage(self, text: typing.Optional[str], level: _core.Qgis.MessageLevel = ..., duration: int = ...) -> None: ...

    @typing.overload
    def pushMessage(self, title: typing.Optional[str], text: typing.Optional[str], level: _core.Qgis.MessageLevel = ..., duration: int = ...) -> None: ...

    @typing.overload
    def pushMessage(self, title: typing.Optional[str], text: typing.Optional[str], showMore: typing.Optional[str], level: _core.Qgis.MessageLevel = ..., duration: int = ...) -> None: ...

    def pushMessage(self, text: typing.Optional[str], level: _core.Qgis.MessageLevel = ...,
                    duration: int = ...) -> None:
        super().pushMessage(text, level, duration)

    # def pushMessage(  # noqa: N802
    #     self, title: str, text: str, level: int, duration: int
    # ) -> None:
    #     """A mocked method for pushing a message to the bar."""
    #     msg = f"{title}:{text}"
    #     self.messages[level].append(msg)

