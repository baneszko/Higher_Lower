import random
import replit
import art
from data import data

def get_random_account():
    """Get data from random account"""
    return random.choice(data)

def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account['name']
    description = account['description']
    country = account["country"]
    return f"{name}, {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """Check followers against user's guess and returns True if they got it right. Or False if the got it wrong."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'
    
def game():
    print(art.logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Comapare A: {format_data(account_a)}.")
        print(art.vs)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a['follower_count']
        b_follower_count = account_b['follower_count']
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        replit.clear()
        print(art.logo)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}.")

game()