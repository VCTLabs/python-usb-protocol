# -*- coding: utf-8 -*-
#
# This file is part of usb-protocol.
#
""" USB-related emitters. """

from .construct_interop import ConstructEmitter, emitter_for_format
from .descriptors.standard import (
    DeviceDescriptorCollection,
    SuperSpeedDeviceDescriptorCollection,
)
