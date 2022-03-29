# -*- coding: utf-8 -*-
"""
From usb_protocol/emitters/construct_interop.py
"""

import unittest

from usb_protocol.emitters.construct_interop import *


class ConstructEmitterTest(unittest.TestCase):

    def test_simple_emitter(self):

        test_struct = construct.Struct(
            "a" / construct.Int8ul,
            "b" / construct.Int8ul
        )

        emitter   = ConstructEmitter(test_struct)
        emitter.a = 0xab
        emitter.b = 0xcd

        self.assertEqual(emitter.emit(), b"\xab\xcd")


if __name__ == "__main__":
    unittest.main()
