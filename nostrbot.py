import os
import telegram
import asyncio
import logging

def read_next_input(filename, last_output_position_file, current_line_number):
  """Reads the next line from a file, one text per line, tracking the last output position in a separate file.

  Args:
    filename: The name of the file to read.
    last_output_position_file: The name of the file to track the last output position in.

  Returns:
    The next text in the file.
  """

  # Check if the last output position file exists.
  if not os.path.exists(last_output_position_file):
    # Create the last output position file and initialize it to 0.
    with open(last_output_position_file, "w") as f:
      f.write("0")

  # Check if the file is empty.
  if os.path.getsize(filename) == 0:
    return "", current_line_number

  # Check if the end of the file has been reached.
  if current_line_number == len(open(filename, "r").readlines()):
    return "", current_line_number

  # Open the file and read the line at the last output position.
  with open(filename, "r") as f:
    next_input = f.readlines()[current_line_number].strip()

  # Update the last output position in the file.
  with open(last_output_position_file, "w") as f:
    f.write(str(current_line_number + 1))

  return next_input, current_line_number + 1

async def send_telegram_notification(message):
  """Sends a Telegram notification.

  Args:
    message: The message to send.
  """

  # Telegram Bot API token
  TOKEN = 'ADD YOUR OWN TOKEN'

  # Telegram chat ID to send the notifications to
  CHAT_ID = 'ADD YOUR OWN CHAT ID'

  # Create a Telegram bot.
  bot = telegram.Bot(token=TOKEN)

  # Try to send the message to the bot.
  try:
    await bot.send_message(chat_id=CHAT_ID, text=message)
  except Exception as e:
    logging.error("Failed to send Telegram notification: %s", e)

  # Wait for the notification to be sent before exiting the script.
  await asyncio.sleep(1)

def main():

  # Configure logging
  logging.basicConfig(filename='script.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
  filename = "input.txt"
  last_output_position_file = "last_output_position.txt"

  # Get the last output position from the file.
  with open(last_output_position_file, "r") as f:
    current_line_number = int(f.read())

  # Read the next line from the file.
  next_input, current_line_number = read_next_input(filename, last_output_position_file, current_line_number)

  if next_input == "":
    # Send a different Telegram message if the next_input function returns empty.
    asyncio.run(send_telegram_notification("❌❌❌ File empty or end of file ❌❌❌"))
  else:
    # Check if there are 5 lines left to print.
    if len(open(filename, "r").readlines()) - current_line_number <= 5:
      #logging.info("5 lines left")
      # Execute the send_telegram_notification coroutine using asyncio.run()
      asyncio.run(send_telegram_notification("❌ 5 lines left to print ❌"))

  # Print the next line to the terminal.
  print(next_input)

if __name__ == "__main__":
  main()
