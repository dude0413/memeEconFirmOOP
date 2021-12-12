import praw, datetime


# Insert the submission post id, the contents and the bot that you would like to use #
def comment(interested_submission_post_id, contents, bot):
    submission = bot.submission(id=interested_submission_post_id)
    for submission_comment in submission.comments:
        if submission_comment.author == 'MemeInvestor_bot':
            try:
                submission_comment.reply(contents)
            except praw.exceptions.APIException:
                print('Got the rate limit, exiting now...')
                exit()


def has_numbers(input_string):
    return any(char.isdigit() for char in input_string)


class RedditBot:
    def __init__(self, bot_username, bot_password, bot_client_id, bot_client_secret):
        self.username = bot_username
        self.password = bot_password
        self.client_id = bot_client_id
        self.client_secret = bot_client_secret
        self.current_balance_message = ''
        RedditBot.praw_instance = praw.Reddit(user_agent='testing testing 33',
                                              client_id=bot_client_id,
                                              client_secret=bot_client_secret,
                                              username=bot_username,
                                              password=bot_password)

    # Get balance from RedditBot's portfolio message
    def get_balance(self):
        inbox_comment_reply_list = []
        for item in RedditBot.praw_instance.inbox.comment_replies(limit=5):
            body = item.body
            author = item.author
            print(body + str(author))
            # Find portfolio message
            if item.author == "MemeInvestor_bot" and body.split(' ', 1)[0] == 'Your':
                current_balance_message = body
        split_current_balance_message = current_balance_message.split()
        balance = float(split_current_balance_message[11].replace('**', ''))
        return balance

    # Invest in a post with a certain number of shares
    def invest(self, post_id, bot_balance):
        # Get the flair from the post
        checking_flair = RedditBot.praw_instance.submission(id=post_id).link_flair_text
        # Some magic with the flair to extract the price
        if has_numbers(checking_flair):
            extracted_flair = checking_flair.replace("M¢", '')
            global price
            price = round(float(extracted_flair))
            print(price)
        shares = .75*(bot_balance / price)
        shares = round(shares)
        invest_message = "!buy " + str(shares)

        comment(post_id, invest_message, RedditBot.praw_instance)
        print("invested in " +
              RedditBot.praw_instance.submission(id=post_id).title + " with " + str(shares) + shares)

    def comment(self, post_id, message):
        comment(post_id, message, RedditBot.praw_instance)


class CEO(RedditBot):
    def __init__(self, company):
        self.company = company


class Worker(RedditBot):
    def __init__(self, company):
        self.company = company


class SearchBot(RedditBot):
    def __init__(self):
        pass

    def search(self, post_id_checking):
        post_searching = RedditBot.praw_instance.submission(id=post_id_checking)
        upvotes_on_checking_post = post_searching.score
        print('da upvotes on this shit: ' + str(upvotes_on_checking_post) + '\n')
        checking_flair = post_searching.link_flair_text
        checking_submission_created_formatted = post_searching.created_utc
        submission_time = datetime.datetime.utcfromtimestamp(checking_submission_created_formatted)
        checking_age = (datetime.datetime.now() - submission_time)
        time_boolean_sixty = checking_age < datetime.timedelta(minutes=60)
        if time_boolean_sixty and upvotes_on_checking_post > 450:
            return 1
        else:
            return 0


