import time
from RedditBot import RedditBot, CEO, Worker, SearchBot

# theaspectcisco_bot = RedditBot('theaspectcisco', 'fhexyQnda7HYM37BCtKfCFCE','9TKxutUkJ5590Q',
#         'FS8pFxtyjeqoiFV27z-aJW73Lukk0A')

# theaspectcisco_bot.comment('n30usi', 'testing testing 12')

# Logging in bots
# Login theaspectcisco as the search bot
theaspectcisco_bot = RedditBot('theaspectcisco', 'fhexyQnda7HYM37BCtKfCFCE', '9TKxutUkJ5590Q',
                               'FS8pFxtyjeqoiFV27z-aJW73Lukk0A')
theaspectcisco_bot_search_bot = SearchBot()
theaspectcisco_bot_search_bot.search("n2l7cn")

# Login Memeslavebot3 (Worker for Company 1)
# memeslavebot3 = RedditBot('memeslavebot3', '([RS4kP&z)qEbdp&', '6sLVA6CKfW87VA',
                         # 'y9VPqi63gIkwU3kusYoZVAPnOAo')
# memeslavebot3 = Worker('Company 1')
# Login Memeslavebot4 (Worker for Company 2)
# memeslavebot4 = RedditBot('memeslavebot4', 's3WaF=dg(_)fr.Ev', 'jjkoDkh1wRQnnw',
                         # 'qORfWohGFTLfj7AZNKlivvC0E30')
# memeslavebot4 = Worker('Company 2')
# Login Lucid Dreaming Bot (CEO of Company 1)
# LucidDreaming_bot = RedditBot('LucidDreaming_bot', 'teet0kain-bup5SHEG', 'QgB5EYqXC1UaZQ',
                          #    'XBNJ7ISvCANsOXCNjtCyvA1z_Fs')
# LucidDreaming_bot = CEO('Company 1')
# Login SkynetMemeEconBot2 (CEO of Company 2)
# SkynetMemeEconBot2 = RedditBot('SkynetMemeEconBot2', 'huft9hach*SHUR.chum', 'AinhuT7sX1OoXw',
                            #   '4m_6E_LuWi9hPgXkiTSDF9DfAV0')
# SkynetMemeEconBot2 = CEO('Company 2')

Company1_bots = [theaspectcisco_bot]
# Company2_bots = [SkynetMemeEconBot2, memeslavebot4]
# all_company_bots = Company2_bots + Company1_bots
subreddit = theaspectcisco_bot.praw_instance.subreddit('MemeEconomy')
# while True:

# Search for post

for bot in Company1_bots:
    checking_boolean = False
    while not checking_boolean:
        for searching_submission in subreddit.hot(limit=15):
            searching_submission_post_id = searching_submission.id
            print(searching_submission_post_id)
            outcome = theaspectcisco_bot_search_bot.search(searching_submission_post_id)
            if outcome == 1:
                print("this the one bois    " + searching_submission.id + '  ' + searching_submission.title + '\n')
                checking_boolean = True
                bot.invest(searching_submission.id, bot.get_balance())
            else:
                print('this aint the one bois     ' + searching_submission.id + '    ' + searching_submission.title + '\n')
        # Wait 5 minutes to go again
        print('\nTaking a nap for a bit')
        time.sleep(300)


# If worthy of investing, invest into it with a bot
# Get upvotes before and store somewhere?

# Search for another post (could be same post)
# Wait the 4 hours (would start timer after last bot has invested in something)
