import unittest
from telethon import TelegramClient
from scripts.telegram_scraper import TelegramScraper
from unittest.mock import AsyncMock, patch
import os


class TestTelegramScraper(unittest.TestCase):
    def setUp(self):
        # Setup mock environment variables
        self.api_id = "mock_api_id"
        self.api_hash = "mock_api_hash"
        self.media_dir = "test_media"
        self.output_file = "test_output.xlsx"
        self.channels_csv = "test_channels.csv"

        # Create a temporary CSV file for testing
        with open(self.channels_csv, "w") as f:
            f.write("@test_channel\n")

        self.scraper = TelegramScraper(
            api_id=self.api_id,
            api_hash=self.api_hash,
            media_dir=self.media_dir,
            output_file=self.output_file,
        )

    @patch("telethon.TelegramClient")
    def test_scrape_channel(self, MockClient):
        # Mock the TelegramClient and its iter_messages
        mock_client = MockClient.return_value
        mock_client.iter_messages = AsyncMock(
            return_value=[
                AsyncMock(id=1, message="Test message", date="2025-01-01", media=None),
                AsyncMock(
                    id=2,
                    message="Test message with photo",
                    date="2025-01-01",
                    media=AsyncMock(photo=True),
                ),
            ]
        )

        # Run the async function
        async def run_test():
            await self.scraper.scrape_channel("@test_channel")
            self.assertTrue(os.path.exists(self.media_dir))

        self.scraper.client = mock_client
        mock_client.start = AsyncMock(return_value=None)
        mock_client.stop = AsyncMock(return_value=None)

        # Ensure no exceptions are raised
        unittest.TestCase.run(run_test())

    def tearDown(self):
        # Clean up test files
        if os.path.exists(self.channels_csv):
            os.remove(self.channels_csv)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
        if os.path.exists(self.media_dir):
            os.rmdir(self.media_dir)


if __name__ == "__main__":
    unittest.main()
