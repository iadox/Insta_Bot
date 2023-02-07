from instabot import Bot
import time


bot = Bot()
bot_user = "---"
insta_pass_bot = "---"
trakced_acc = "---"
beeb = bot.login(username=bot_user, password=insta_pass_bot)
old_followers = sorted(list(bot.get_user_followers(user_id=trakced_acc)))
state = True
while state:
    time.sleep(10)
    current_followers = sorted(list(bot.get_user_followers(user_id=trakced_acc)))
    if old_followers != current_followers:
        set1 = set(old_followers)
        set2 = set(current_followers)
        unfollowed = list(sorted(set1 - set2))
        try:
            print(f"reached Unfollowed  -- unfollowed list: {unfollowed}")
            unfollowed = unfollowed[0]
            bot.send_message(text= f"@{bot.get_username_from_user_id(unfollowed)} just unfollowed you", user_ids=trakced_acc)
            print("sent a message")
        except:
            print("reached exception")
    else:
        print("nothing so far")
    old_followers = current_followers
        
bot.logout()
