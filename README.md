# Nostr Bot Poster

These instructions will help you to get started with creating your own nostr bot to automate posting your predefined posts. Just follow: npub1wuj7ent0p42n9v8awdzl2sfanfj4u2k7dwz09ranqd7fwsz5qpgquc92rq to see it in action.

As an option, you can also setup a Telegram bot alert when you are running out of content to post.

## Pre-requsites

1. Noscl

We will use Noscl, Fiatjaf's command line client for Nostr. See here: https://github.com/fiatjaf/noscl

You can also use the following tutorial to set it up properly: https://habla.news/a/naddr1qqnkummnw3ez6ut4da6x2uedvfhhgtts096xsmmw94eksetvdskhvetj0ykk2ctn0yq3uamnwvaz7tmwdaehgu3dwp6kytnhv4kxcmmjv3jhytnwv46z7qgwwaehxw309ahx7uewd3hkctcpzamhxue69uhhyetvv9ujumn0wd68ytnzv9hxgtcpzdmhxue69uhk7enxvd5xz6tw9ec82c30qy0hwumn8ghj7mn0wd68yttjv4kxz7fwdehkkmm5v9ex7tnrdakj7q3q7rlc0emedw5xljztfqrmykjaacsx6ujvdas64zznjadrnhhwlavqxpqqqp65wvt7ddx

2. Python Telegram library

To get the library, run this command:
```
pip install python-telegram-bot
```

3. Telegram bot (https://core.telegram.org/bots/tutorial) - this is where you will get bot token and chat id


## The script

Modify the "input.txt" file to contain your content.
```
pico -w input.txt
```

Modify the "nostrbot.py" file with your Telegram Token and Chat ID and any custom messages you want to send. This Python script will basically read a line from your content file and sends it to telegram. It will also record the last line number read in the "last_output_position.txt" file, so next time it runs, the script knows to read the next line of content. Finally, when you are almost at the end of the file or when you came to the end of the file, it will notify you on Telegram.
```
pico -w nostrbot.py
```
Adjust these:
```
  # Telegram Bot API token
  TOKEN = 'ADD YOUR OWN TOKEN'

  # Telegram chat ID to send the notifications to
  CHAT_ID = 'ADD YOUR OWN CHAT ID'
```

and these:
```
  if next_input == "":
    # Send a different Telegram message if the next_input function returns empty.
    asyncio.run(send_telegram_notification("❌❌❌ File empty or end of file ❌❌❌"))
  else:
    # Check if there are 5 lines left to print.
    if len(open(filename, "r").readlines()) - current_line_number <= 5:
      #logging.info("5 lines left")
      # Execute the send_telegram_notification coroutine using asyncio.run()
      asyncio.run(send_telegram_notification("❌ 5 lines left to print ❌"))
```

Adjust the "nostrpost.sh" bash script to include the correct paths to your files.
```
pico -w nostrpost.sh
```

Make sure that your Noscl has the correct hex private key (probably some testing account first). Note: it is the hex key not the nsec. Replace <key> with your own.
```
noscl setprivate <key>
```

When you are ready, just run:
```
./nostrpost.sh
```

## Automating the notifications
  
When the script correctly posts to Nostr and notifies you on Telegram, the next step is to automate it. 

Run the following command to open your crontab.

```
crontab -e
```

Add the following into it.

```
30 * * * * /ABSOLUTE PATH TO YOUR PYTHON FILE/./nostrpost.sh >> /ABSOLUTE PATH TO YOUR CRONLOG FILE 2>&1
```

Don't forget to replace the path to your python file and to the location where you want the log. 

This cron schedule will execute the specified command at the 30th minute of every hour.

# Extras

When you post a lot of content, maybe you'd like to style it, so it has a similar look and feel. For example: append something to each content or pre-pend some data. 
In the repo, you will also find a script: "addtopost.py" which will help you to do this in bulk.

# End Notes

Now go out there and create your own bot. Sky is the limit. It is by no means perfect, but it will do the job.

If you found this guide useful, why not let it be known by [sending me a few sats](https://360swim.com/ln-donate-github) or via LN address⚡swmtr@360swim.com .
<br />
<img src="https://360swim.com/user/themes/swimquark/images/ln_git.png" width="400" />

Finally, if you are into swimming, checkout some [swimming tips](https://360swim.com/tips).






