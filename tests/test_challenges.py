# tests/test_challenges.py
import unittest
import sys
import os

# Ensure the tests can find the src folder
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from challenges import (funnyString, alternatingCharacters, caesarCipher, 
                        alternate, gridChallenge, StringProvider, CharacterService)

# --- THE STUB ---
class StubStringProvider(StringProvider):
    def fetch_data(self):
        return "AAABBB"

# --- THE TEST CASES ---
class TestHackerRankChallenges(unittest.TestCase):

    # --- Extra Credit Stub & Base Class Tests ---
    def test_string_provider_base_raises_error(self):
        # This test ensures we cover the 'raise NotImplementedError' line
        provider = StringProvider()
        with self.assertRaises(NotImplementedError):
            provider.fetch_data()

    def test_character_service_with_stub(self):
        stub = StubStringProvider()
        service = CharacterService(stub)
        self.assertEqual(service.process_alternating(), 4)

    # --- 1. Funny String Tests ---
    def test_funny_string_is_funny(self):
        self.assertEqual(funnyString("acxz"), "Funny")

    def test_funny_string_is_not_funny(self):
        self.assertEqual(funnyString("bcxz"), "Not Funny")

    # --- 2. Alternating Characters Tests ---
    def test_alternating_characters_no_deletions(self):
        self.assertEqual(alternatingCharacters("ABABABA"), 0)

    def test_alternating_characters_with_deletions(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)

    # --- 3. Caesar Cipher Tests ---
    def test_caesar_cipher_lowercase_and_uppercase_and_symbols(self):
        self.assertEqual(caesarCipher("middle-Outz", 2), "okffng-Qwvb")

    def test_caesar_cipher_large_k(self):
        self.assertEqual(caesarCipher("abc", 26), "abc")

    # --- 4. Two Characters (Alternate) Tests ---
    def test_alternate_valid_string(self):
        self.assertEqual(alternate("beabeefeab"), 5)

    def test_alternate_no_valid_string(self):
        self.assertEqual(alternate("ababaa"), 0)

    # --- 5. Grid Challenge Tests ---
    def test_grid_challenge_yes(self):
        grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_grid_challenge_no(self):
        grid = ["zyx", "wvu", "tsr"]
        self.assertEqual(gridChallenge(grid), "NO")