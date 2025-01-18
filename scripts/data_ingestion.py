# data_ingestion.py
from telethon.sync import TelegramClient
import pandas as pd
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def fetch_telegram_data(api_id, api_hash, channel_list, output_file):
    """Fetch messages from Telegram channels and save to an Excel file."""
    try:
        client = TelegramClient("session", api_id, api_hash)
        client.start()

        all_messages = []
        for channel in channel_list:
            logging.info(f"Fetching messages from channel: {channel}")
            try:
                messages = client.get_messages(
                    channel, limit=100
                )  # Adjust limit as needed
                for msg in messages:
                    # Convert datetime to timezone-unaware format
                    msg_date = msg.date.replace(tzinfo=None) if msg.date else None
                    all_messages.append(
                        {
                            "channel": channel,
                            "message": msg.text,
                            "date": msg_date,
                            "sender": msg.sender_id if msg.sender_id else None,
                        }
                    )
            except Exception as e:
                logging.error(f"Error fetching messages from {channel}: {e}")

        # Save to Excel
        df = pd.DataFrame(all_messages)
        df.to_excel(output_file, index=False)
        logging.info(f"Data saved to {output_file}")
    except Exception as e:
        logging.error(f"Error during Telegram data ingestion: {e}")
    finally:
        client.disconnect()

    return output_file
