from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaDocument
import os

api_id = 21634269
api_hash = '1d4a953f8e62afd6b512810e44ecbca0'
max_items = 1
kont = 1

download_path = '/d/NAS/Incoming'

if not os.path.exists(download_path):
	os.makedirs(download_path)

with TelegramClient('/d/NAS/scripts/session_name', api_id, api_hash) as client:
	saved_messages = client.get_messages('me', limit=30)

	for message in saved_messages:
		if isinstance(message.media, MessageMediaDocument):
			if message.media.document.mime_type.startswith('video'):
				file_name = message.file.name
				client.download_media(message, file=download_path)
				client.send_message('me', f"'{file_name}' bideue ondo deskarga da.")
				message.delete()
				kont = kont + 1
				if kont > max_items:
					break
