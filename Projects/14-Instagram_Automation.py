from instabot import Bot

bot = Bot() # this is just refrencing you can directly use Bot().

usr="your_username"
pss="your_password"

bot.login(username=usr,password=pss)
bot.upload_photo("Projects/Assets/ghost.jpg",caption="I Uploaded using instabot")