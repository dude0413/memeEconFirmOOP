import time
from RedditBot import RedditBot, CEO, Worker, SearchBot

# Logging in bots
# Login theaspectcisco as the search bot
theaspectcisco_bot = RedditBot('', '', '',
                               '')
theaspectcisco_bot_search_bot = SearchBot()


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
