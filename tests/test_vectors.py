"""Test vectors

https://www.cosic.esat.kuleuven.be/nessie/testvectors/hash/sha/Sha-2-256.unverified.test-vectors
"""

import os
import unittest
from tempfile import mkstemp

from sha256sum import sha256sum


class TestVectors(unittest.TestCase):
    """Test with known values"""

    def setUp(self):
        self.handle, self.path = mkstemp(prefix="sha256sum")

    def tearDown(self):
        os.remove(self.path)

    def _sha256(self, data):
        with open(self.path, "wb") as file:
            file.write(data)
        return sha256sum(self.path)

    def test_empty(self):
        self.assertEqual(
            self._sha256(b""),
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        )

    def test_abc(self):
        self.assertEqual(
            self._sha256(b"abc"),
            "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
        )

    def test_one_million_times_a(self):
        self.assertEqual(
            self._sha256(b"a" * 1000000),
            "cdc76e5c9914fb9281a1c7e284d73e67f1809a48a497200e046d39ccc7112cd0",
        )

    def test_single_zero_byte(self):
        self.assertEqual(
            self._sha256(b"\0"),
            "6e340b9cffb37a989ca544e6bb780a2c78901d3fb33738768511a30617afa01d",
        )

    def test_32_zero_bytes(self):
        self.assertEqual(
            self._sha256(b"\0" * 32),
            "66687aadf862bd776c8fc18b8e9f8e20089714856ee233b3902a591d0d5f2925",
        )


if __name__ == "__main__":
    unittest.main()
