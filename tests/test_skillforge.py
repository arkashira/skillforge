from skillforge import Skillforge, Update
import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta

class TestSkillforge(unittest.TestCase):
    def test_get_top_updates(self):
        skillforge = Skillforge([])
        updates = skillforge.get_top_updates()
        self.assertEqual(len(updates), 5)

    @patch('smtplib.SMTP')
    def test_send_email(self, mock_smtp):
        skillforge = Skillforge([])
        updates = [Update("Update 1", "Summary 1. This is a summary.", "https://example.com/update1")]
        skillforge.send_email(updates, 'subscriber@example.com')
        mock_smtp.assert_called_once_with('smtp.example.com', 587)

    def test_track_open_rate(self):
        skillforge = Skillforge([])
        open_rate = skillforge.track_open_rate('subscriber@example.com')
        self.assertEqual(open_rate, 0.5)

    def test_unsubscribe(self):
        db = ['subscriber1@example.com', 'subscriber2@example.com']
        skillforge = Skillforge(db)
        skillforge.unsubscribe('subscriber2@example.com')
        self.assertEqual(len(db), 1)

if __name__ == '__main__':
    unittest.main()
