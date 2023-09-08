"""
This module provides utility functions for working with strings.

It includes functions for string manipulation, checking for specific patterns,
and performing common string operations.

Author: Walter Manzanero
Version: 1.0
"""
# This program will help oraganize the game nights for the Abruptly gamers

gamers = []
game = "Abruptly Goblins!"

def add_gamer(gamer, gamers_list):
    """
    Add a gamer to the list of gamers.

    Args:
        gamer (dict): A dictionary containing gamer information.
            It should include the following keys:
            - "name" (str): The name of the gamer.
            - "availability" (list): A list of days the gamer is available to play.

        gamers_list (list): The list of gamers to add the gamer to.

    Returns:
        None

    Prints:
        - If gamer data is valid, it prints a message confirming the addition.
        - If gamer data is invalid, it prints an error message.

    Example:
        add_gamer({"name": "Alice", "availability": ["Monday", "Wednesday"]}, gamers)
    """
    if "name" in gamer and "availability" in gamer:
        gamers_list.append(gamer)
        print(f"Added gamer {gamer['name']} to the list.")
    else:
        print("Invalid gamer data. 'name' and 'availability' keys are required.")


gamers_list = []

kimberly = {"name": "Kimberly Warner",
            "availability": ["Monday", "Tuesday", "Friday"]}

add_gamer(kimberly, gamers)
add_gamer({'name': 'Thomas Nelson', 'availability': [
          "Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joyce Sellers', 'availability': [
          "Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name': 'Michelle Reyes', 'availability': [
          "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name': 'Stephen Adams', 'availability': [
          "Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': [
          "Monday", "Thursday"]}, gamers)
add_gamer({'name': 'Latasha Bryan', 'availability': [
          "Monday", "Sunday"]}, gamers)
add_gamer({'name': 'Crystal Brewer', 'availability': [
          "Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name': 'James Barnes Jr.', 'availability': [
          "Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name': 'Michel Trujillo', 'availability': [
          "Monday", "Tuesday", "Wednesday"]}, gamers)


def build_daily_frequency_table():
    """
    Build a daily frequency table with days of the week as keys and initial counts set to 0.

    Returns:
        dict: A dictionary with days of the week as keys and initial counts set to 0.

    Example:
        frequency_table = build_daily_frequency_table()
        # Output: {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0,
         'Saturday': 0, 'Sunday': 0}
    """
    return {
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 0,
        "Friday": 0,
        "Saturday": 0,
        "Sunday": 0
    }


count_availability = build_daily_frequency_table()

def calculate_availability(gamers_list, available_frequency):
    """
    Calculate availability frequency for gamers.

    This function takes a list of gamers and a frequency table, and it calculates the
    availability frequency for each day of the week based on the provided gamers' availability.

    Parameters:
    gamers_list (list of dict): A list of dictionaries, where each dictionary represents a gamer.
                                Each gamer dictionary should have a "name" and "availability" key.
    available_frequency (dict): A frequency table where keys are days of the week (e.g., "Monday"),
                               and values are integers representing the frequency of availability.

    Example:
    >>> gamers_list = [
    ...     {"name": "Alice", "availability": ["Monday", "Wednesday", "Friday"]},
    ...     {"name": "Bob", "availability": ["Tuesday", "Thursday"]},
    ... ]
    >>> available_frequency = {
    ...     "Monday": 0,
    ...     "Tuesday": 0,
    ...     "Wednesday": 0,
    ...     "Thursday": 0,
    ...     "Friday": 0,
    ...     "Saturday": 0,
    ...     "Sunday": 0
    ... }
    >>> calculate_availability(gamers_list, available_frequency)
    >>> print(available_frequency)
    {'Monday': 1, 'Tuesday': 1, 'Wednesday': 1, 'Thursday': 1, 'Friday': 1, 'Saturday': 0, 'Sunday': 0}
    """
    for gamer in gamers_list:
        for day in gamer["availability"]:
            available_frequency[day] += 1

calculate_availability(gamers, count_availability)
print(count_availability)


def find_best_night(availability_table):
    """
    Find the day with the highest availability frequency.

    Parameters:
    availability_table (dict): A dictionary where keys are days of the week and values are
                               integers representing availability frequency.

    Returns:
    str: The day of the week with the highest availability frequency.
    """
    best_night = max(availability_table, key=availability_table.get)
    return best_night


game_night = find_best_night(count_availability)
print(game_night)

def available_on_night(gamers_list, day):
    """
    Find gamers who are available on a specific day.

    Parameters:
    gamers_list (list): A list of dictionaries representing gamers.
    day (str): The day of the week to check availability.

    Returns:
    list: A list of gamers available on the specified day.
    """
    available_gamers = []
    for gamer in gamers_list:
        if day in gamer["availability"]:
            available_gamers.append(gamer["name"])
    return available_gamers

attending_game_night = available_on_night(gamers, game_night)
print(attending_game_night)

form_email = "Hi {name}, get ready for the battle. We have assigned this {day} to hold the event for {game}."

def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        email_message = form_email.format(name=gamer, day=day, game=game)
        print(email_message)

send_email(attending_game_night, game_night, game)

unable_to_attend_best_night = [gamer for gamer in gamers if game_night not in gamer["availability"]]
second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)


"""
Identify gamers unable to attend the best night, calculate availability for a second night,
and find the best night for the second night's game.

Parameters:
- gamers (list): A list of dictionaries representing gamers with availability information.
- game_night (str): The best night chosen for the initial game.

Returns:
- unable_to_attend_best_night (list): A list of gamers unable to attend the best night.
- second_night_availability (dict): A frequency table for the availability of the second night.
- second_night (str): The best night for the second night's game.
"""

print("Gamers unable to attend the best game night: " + str(unable_to_attend_best_night))
print("Second night availability frequency table: " + str(second_night_availability))
print("Best night for the second night: " + str(second_night))

available_on_night(gamers, second_night)
send_email(second_night_availability, second_night, game)