from instabot import Bot
import time
import customtkinter as ct

def entry_screen():
    for widgets in content.winfo_children():
      widgets.destroy()
    root.geometry("320x100")
    label_1 = ct.CTkLabel(master=content,text = "Instagram Username: ")
    label_1.grid(row = 0, column = 0, pady = 10, padx = 10)
    insta_entry = ct.CTkEntry(master=content)
    insta_entry.grid(row = 0, column = 1, pady = 10, padx = 10)
    submit = ct.CTkButton(master = content, text = "Continue",command= lambda:activity_screen(insta_entry.get()))
    submit.grid(row = 1, column = 1, pady = 10, padx = 10)


def activity_screen(insta_acc):
    print(insta_acc)
    for widgets in content.winfo_children():
      widgets.destroy()
    root.geometry("350x160")
    content.configure(height = 120, width = 340)
    label_2 = ct.CTkLabel(master=content,text = f"Hey {insta_acc}!, \nCheck your DMs. messages might be in the DM requests. \nAsk someone to unfollow you to test if it's working ")
    label_2.place(x = 10, y = 10)
    stop_tracking = ct.CTkButton(master = content, text = "stop tracking", command=lambda:entry_screen())
    stop_tracking.place(x = 10, y = 70)
    #start_tracking = ct.CTkButton(master = content, text = "start tracking", command=lambda:activity(insta_acc))
    #start_tracking.place(x = 190, y = 70)
    time.sleep(5)
    bot_user = "lordfarquaad.bot"
    insta_pass_bot = "easytoguesspassword"
    trakced_acc = insta_acc
    beeb = bot.login(username=bot_user, password=insta_pass_bot)
    my_followers = sorted(list(bot.get_user_followers(user_id=trakced_acc)))
    state = True
    while state:
        my_followers = sorted(list(bot.get_user_followers(user_id=trakced_acc)))
        time.sleep(10)
        current_followers = sorted(list(bot.get_user_followers(user_id=trakced_acc)))

        if my_followers != current_followers:
            set1 = set(my_followers)
            set2 = set(current_followers)
            unfollowed = list(sorted(set1 - set2))
            try:
                print("reached Unfollowed")
                print(f"unfollowed list: {unfollowed}")
                unfollowed = unfollowed[0]
                bot.send_message(text= f"@{bot.get_username_from_user_id(unfollowed)} just unfollowed you", user_ids=trakced_acc)
            except:
                print("reached exception")
                pass
            print('missing:', unfollowed)
        else:
            print("nothing so far")
        
    bot.logout()


def activity(insta_acc):
    bot_user = "username"
    insta_pass_bot = "password"
    trakced_acc = insta_acc
    beeb = bot.login(username=bot_user, password=insta_pass_bot)
    my_followers = sorted(list(bot.get_user_followers(user_id=trakced_acc)))
    state = True
    while state:
        my_followers = sorted(list(bot.get_user_followers(user_id=trakced_acc)))
        time.sleep(10)
        current_followers = sorted(list(bot.get_user_followers(user_id=trakced_acc)))

        if my_followers != current_followers:
            set1 = set(my_followers)
            set2 = set(current_followers)
            unfollowed = list(sorted(set1 - set2))
            try:
                print("reached Unfollowed")
                print(f"unfollowed list: {unfollowed}")
                unfollowed = unfollowed[0]
                bot.send_message(text= f"@{bot.get_username_from_user_id(unfollowed)} just unfollowed you", user_ids=trakced_acc)
            except:
                print("reached exception")
                pass
            print('missing:', unfollowed)
        else:
            print("nothing so far")
        
    bot.logout()


bot = Bot()

ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")
root = ct.CTk()
root.resizable(False, False)
root.title('Instagram Tracking Software')
content = ct.CTkFrame(master=root)
content.pack(expand = True, pady=5,padx=5)
entry_screen()
root.mainloop()





