# -*- coding: utf-8 -*-
#
# This file is part of usb_protocol.
#
""" Convenience emitters for USB Audio Class 1 descriptors. """


from ...types.descriptors.uac1 import (
    AudioControlInterruptEndpointDescriptor,
)
from .. import emitter_for_format

AudioControlInterruptEndpointDescriptorEmitter  = emitter_for_format(AudioControlInterruptEndpointDescriptor)
