from instabot import Bot
import smtplib
from email.mime.text import MIMEText
from email import utils
import time

bot_user = "idk"
trakced_acc = "idk either"
email_of_receiver = "b@gmail.com"
sender = 'insta_activity_bot@outlook.com'
sender_password = "capybaras"
def send_email(peep, change):
    body = f'''Subject: {change} by {peep}\n \n\nYooooo,\n\n{peep} just {change} you 
    \nlmao, \nThe Instagram Bot'''
    try:
        smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
    except Exception as e:
        print(e)
        smtpObj = smtplib.SMTP_SSL('smtp-mail.outlook.com', 465)
    type(smtpObj)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(sender, sender_password) 
    smtpObj.sendmail(sender, email_of_receiver, body) 
    smtpObj.quit()

bot = Bot()
beeb = bot.login(username=bot_user, password="your_password")

my_followers = sorted(list(bot.get_user_followers(user_id=trakced_acc)))
state = True
while state:
    compare_list1 = []
    compare_list2 = []
    my_followers = sorted(list(bot.get_user_followers(user_id=trakced_acc)))
    time.sleep(10)
    current_followers = sorted(list(bot.get_user_followers(user_id=trakced_acc)))
    if current_followers != my_followers:
        print(my_followers)
        print(current_followers)
        for fo in my_followers:
            compare_list1.append(fo)
        print("----------------------------------------")
        for fo in current_followers:
            compare_list2.append(fo)
        set1 = set(compare_list1)
        set2 = set(compare_list2)
        unfollowed = list(sorted(set1 - set2))
        print(unfollowed)
        new_follower = list(sorted(set2 - set1))
        print(new_follower)
        try:
            print("reached Unfollowed")
            unfollowed = unfollowed[0]
            unfollowed = bot.get_username_from_user_id(unfollowed)
            send_email(unfollowed, "Unfollowed")
        except:
            print("reached new follower")
            new_follower = new_follower[0]
            new_follower = bot.get_username_from_user_id(new_follower)
            send_email(new_follower, "Followed")
        print('missing:', unfollowed)
        print('added:', new_follower)
    else:
        print("nothing so far")
    
bot.logout()