# Copyright (c) FRC 1076 PiHi Samurai
# You may use, distribute, and modify this software under the terms of
# the license found in the root directory of this project

import robotpy_apriltag as apriltag
# A singleton class for maintaining global field configuration

_tag_size: float
_family: str
_layout: apriltag.AprilTagFieldLayout

def setTagSize(size: float) -> None:
    global _tag_size
    _tag_size = size

def getTagSize() -> float:
    global _tag_size
    return _tag_size


def setFamily(family: str) -> None:
    global _family
    _family = family

def getFamily() -> str:
    global _family
    return _family


def loadLayout(layoutName: str) -> None:
    global _layout
    _layout = apriltag.AprilTagFieldLayout("resources/fields/" + layoutName + ".json")

def setLayout(layout: apriltag.AprilTagFieldLayout) -> None:
    #For testing only
    global _layout
    _layout = layout

def getLayout() -> apriltag.AprilTagFieldLayout:
    global _layout
    return _layout




