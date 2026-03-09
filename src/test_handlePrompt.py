from unittest import TestCase, mock
from handle_prompt import handle_user_prompt
import sys
from io import StringIO

class TestPrompt(TestCase):
    def test_flag_help(self):
        with mock.patch('sys.argv', ['main.py', '-h']):
            with mock.patch('sys.stdout', new=StringIO()) as captured_output:
                handle_user_prompt()
                self.assertEqual(captured_output.getvalue().strip(), "get_help called")

