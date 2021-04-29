#!/usr/bin/env python3

import argparse
from datetime import datetime
from colorama import init, Fore, Back, Style
import itertools
import string
import time
from progress.bar import Bar
import threading
import random

# Global start time to keep track of process running time
start_time = time.time()

# Colorama init call
init()

# Globals for separators and attribute toggles
isPlain = False
isYears = True
isNotSep = False
isNoAttr = False
isLetter = False
isQuick = False

# Months list
months = [
"January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December"
]

# Seasons list
seasons = [
    "Fall",
    "Autumn",
    "Winter",
    "Spring",
    "Summer"
]


# Attributes list
attributes = [
    "!",
    "!!",
    "#",
    "##",
    "123",
    "1234",
    "1",
    "1!",
    "1#"
]

# Separators list
common_separators = [
    ".",
    "_",
    "-",
    "@",
    "+",
    "=",
    ","
]


# NFL Teams list
nfl_teams = [
    "Cardinals",
    "Falcons",
    "Ravens",
    "Bills",
    "Panthers",
    "Bears",
    "Bengals",
    "Browns",
    "Cowboys",
    "Broncos",
    "Lions",
    "Packers",
    "Texans",
    "Colts",
    "Jaguars",
    "Chiefs",
    "Chargers",
    "Rams",
    "Dolphins",
    "Vikings",
    "Patriots",
    "Saints",
    "Giants",
    "Jets",
    "Raiders",
    "Eagles",
    "Steelers",
    "49ers",
    "Seahawks",
    "Buccaneers",
    "Titans",
    "Redskins"
]

# NBA Teams list
nba_teams = [
    "Hawks",
    "Celtics",
    "Nets",
    "Hornets",
    "Bulls",
    "Cavaliers",
    "Mavericks",
    "Nuggets",
    "Pistons",
    "Warriors",
    "Rockets",
    "Pacers",
    "Clippers",
    "Lakers",
    "Grizzlies",
    "Heat",
    "Bucks",
    "Timberwolves",
    "Pelicans",
    "Knicks",
    "Thunder",
    "Magic",
    "76ers",
    "Suns",
    "Blazers",
    "Kings",
    "Spurs",
    "Raptors",
    "Jazz",
    "Wizards"
]

# MLB Teams list
mlb_teams = [
    "Diamondbacks",
    "Braves",
    "Orioles",
    "RedSox",
    "Cubs",
    "WhiteSox",
    "Reds",
    "Indians",
    "Rockies",
    "Tigers",
    "Astros",
    "Royals",
    "Angels",
    "Dodgers",
    "Marlins",
    "Brewers",
    "Twins",
    "Mets",
    "Yankees",
    "Athletics",
    "Phillies",
    "Pirates",
    "Padres",
    "Giants",
    "Mariners",
    "Cardinals",
    "Rays",
    "Rangers",
    "Jays",
    "Nationals"
]

# NHL Teams list
nhl_teams = [
    "Ducks",
    "Bruins",
    "Sabres",
    "Flames",
    "Hurricanes",
    "Blackhawks",
    "Avalanche",
    "BLUEJackets",
    "Stars",
    "RedWings",
    "Oilers",
    "Panthers",
    "Kings",
    "Wild",
    "Canadiens",
    "Predators",
    "Devils",
    "Islanders",
    "Rangers",
    "Senators",
    "Flyers",
    "Coyotes",
    "Penguins",
    "BLUEs",
    "Sharks",
    "Lighting",
    "Leafs",
    "Canucks",
    "GoldenKnights",
    "Capitals",
    "Jets"
]

# Common super bowl scores list
superbowl_scores = [
    "35",
    "33",
    "16",
    "23",
    "24",
    "14",
    "21",
    "32",
    "27",
    "31",
    "26",
    "38",
    "46",
    "39",
    "42",
    "20",
    "55",
    "52",
    "30",
    "49",
    "34",
    "48",
    "29",
    "17",
    "43",
    "41"
]

# Common nba finals scores list
nbafinals_scores = [
    "4"
]

# Common world series scores list
worldseries_scores = [
    "4",
    "5"
]

# Common stanley cup scores list
stanleycup_scores = [
    "3",
    "5",
    "2",
    "6",
    "15",
    "4",
    "9",
    "10",
    "12",
    "17",
    "22",
    "20",
    "21"
]

# Common permutations of "password" list
password_permutations = [
    "Password",
    "P4ssw0rd",
    "P@55w0rd",
    "Pa$$w0rd",
    "P@$$w0rd",
    "P455w0rd",
    "P4$$w0rd"
]

# Common misc passwords
common_words = {
    "Welcome",
    "Baseball",
    "Football",
    "Letmein",
    "Access",
    "Superman",
    "Batman",
    "Qwertyuiop",
    "Qwerty",
    "Jesus",
    "Coronavirus"
} 

# Global keyspace for random strings
ascii_keyspace = string.ascii_letters
numeral_keyspace = string.digits
special_keyspace = string.punctuation
ascii_numeral_keyspace = ascii_keyspace + numeral_keyspace
numeral_special_keyspace = numeral_keyspace + special_keyspace
ascii_special_keyspace = ascii_keyspace + special_keyspace
full_keyspace = ascii_numeral_keyspace + special_keyspace

# Global year list to keep track of and manipulate year permutations
year_list = []

# Global sports scores list to keep track of and manipulate sports score permutations
sports_scores_list = []

# Global attribute list to keep track of and manipulate attributes
attr_list = []
# Global separators list to keep track of and manipulate separators
sep_list = []
# Global combined attributes and separators list to keep track of and manipulate the concatenation of attribute + separator permutations
attr_sep_list = []

# Global custom list to keep track of and manipulate and user supplied custom words
custom_wordlist = []
# Global custom list to keep track of and manipulate and user supplied custom attributes
custom_attr_list = []
# Global custom list to keep track of and manipulate and user supplied custom separators
custom_sep_list = []

# Global spray list, dictionary to make things fast cause that's what it should've been the whole time
spray_list = {}
# Global index tracker for the spray list dictionary keys, we don't actually need the keys since it's treated like a list so it's just a formality to satisfy the requirement
spray_list_index = 0

# Global max and min lengths for password sizes that are filtered into the final list
max_length = 999
min_length = 1

# Instead of "appending" directly we manually add in based on the global index, check if something exists already, add it if it doesn't and increment the global key
def update_spray_list(item):
    global spray_list_index

    if item in spray_list.values():
        # current item exists so just return and do not duplicate
        return

    if len(item) >= min_length and len(item) <= max_length:
        spray_list[spray_list_index] = item
        spray_list_index += 1


def generate_keyspace_list(mode, size, year_start, year_end):
    if mode == "ascii":
        ascii_items = list(itertools.product(ascii_keyspace, repeat=size))
        bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating " + mode + " keyspace list", suffix='%(percent)d%%', max=len(ascii_items))
        for item in ascii_items:
            update_spray_list(''.join(item))
            generate_years(''.join(item), year_start, year_end)
            bar.next()
        bar.finish()
    elif mode == "num":
        num_items = list(itertools.product(numeral_keyspace, repeat=size))
        bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating " + mode + " keyspace list", suffix='%(percent)d%%', max=len(num_items))
        for item in num_items:
            update_spray_list(''.join(item))
            generate_years(''.join(item), year_start, year_end)
            bar.next()
        bar.finish()
    elif mode == "spec":
        spec_items = list(itertools.product(special_keyspace, repeat=size))
        bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating " + mode + " keyspace list", suffix='%(percent)d%%', max=len(spec_items))
        for item in spec_items:
            update_spray_list(''.join(item))
            generate_years(''.join(item), year_start, year_end)
            bar.next()
        bar.finish()
    elif mode == "asciinum":
        asciinum_items = list(itertools.product(ascii_numeral_keyspace, repeat=size))
        bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating " + mode + " keyspace list", suffix='%(percent)d%%', max=len(asciinum_items))
        for item in asciinum_items:
            update_spray_list(''.join(item))
            generate_years(''.join(item), year_start, year_end)
            bar.next()
        bar.finish()
    elif mode == "asciispec":
        asciispec_items = list(itertools.product(ascii_special_keyspace, repeat=size))
        bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating " + mode + " keyspace list", suffix='%(percent)d%%', max=len(asciispec_items))
        for item in asciispec_items:
            update_spray_list(''.join(item))
            generate_years(''.join(item), year_start, year_end)
            bar.next()
        bar.finish()
    elif mode == "numspec":
        numspec_items = list(itertools.product(numeral_special_keyspace, repeat=size))
        bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating " + mode + " keyspace list", suffix='%(percent)d%%', max=len(numspec_items))
        for item in numspec_items:
            update_spray_list(''.join(item))
            generate_years(''.join(item), year_start, year_end)
            bar.next()
        bar.finish()
    elif mode == "full":
        full_items = list(itertools.product(full_keyspace, repeat=size))
        bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating " + mode + " keyspace list", suffix='%(percent)d%%', max=len(numspec_items))
        for item in full_items:
            update_spray_list(''.join(item))
            generate_years(''.join(item), year_start, year_end)
            bar.next()
        bar.finish()


def generate_custom(year_start, year_end):
    bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating custom list", suffix='%(percent)d%%', max=len(custom_wordlist))
    for word in custom_wordlist:
        # Add base word to list
        update_spray_list(word)
        update_spray_list(word.capitalize())
        update_spray_list(word.upper())
        update_spray_list(word.lower())
        # Get year permutation with base custom word
        generate_years(word, year_start, year_end)
        bar.next()
    bar.finish()

def generate_common(year_start, year_end):
    bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating common list", suffix='%(percent)d%%', max=len(common_words))
    for word in common_words:
        # Add base word to list
        update_spray_list(word)
        update_spray_list(word.capitalize())
        update_spray_list(word.upper())
        update_spray_list(word.lower())
        # Get year permutation with base common word
        generate_years(word, year_start, year_end)
        bar.next()
    bar.finish()

def generate_short(year_start, year_end):
    short_list = [*common_words, *seasons, *password_permutations, *months]
    if custom_wordlist:
        short_list += custom_wordlist
    bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating short list", suffix='%(percent)d%%', max=len(short_list))
    for word in short_list:
        # Add base word to list
        update_spray_list(word.capitalize())
        # Get year permutation with base word
        generate_years(word, year_start, year_end)
        bar.next()
    bar.finish()

def generate_password_perms(year_start, year_end):
    bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating 'password' list", suffix='%(percent)d%%', max=len(password_permutations))
    for password in password_permutations:
        # Add base word to list
        update_spray_list(password)
        update_spray_list(password.capitalize())
        update_spray_list(password.upper())
        update_spray_list(password.lower())
        # Get year permutation with base password permutation
        generate_years(password, year_start, year_end)
        bar.next()
    bar.finish()

def generate_months(year_start, year_end):
    bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating months list", suffix='%(percent)d%%', max=len(months))
    for month in months:
        # Add base word to list
        update_spray_list(month)
        update_spray_list(month.capitalize())
        update_spray_list(month.upper())
        update_spray_list(month.lower())
        # Get year permutation with base month
        generate_years(month, year_start, year_end)


def generate_nfl(year_start, year_end):
    bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating nfl list", suffix='%(percent)d%%', max=len(nfl_teams))
    for team in nfl_teams:
        # Add base word to list
        update_spray_list(team)
        update_spray_list(team.capitalize())
        update_spray_list(team.upper())
        update_spray_list(team.lower())
        sports_scores_list.append(team)
        sports_scores_list.append(team.capitalize())
        sports_scores_list.append(team.upper())
        sports_scores_list.append(team.lower())

        # Get year permutation with base nfl team
        generate_years(team, year_start, year_end)
        bar.next()
    bar.finish()


def generate_nba(year_start, year_end):
    bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating nba list", suffix='%(percent)d%%', max=len(nba_teams))
    for team in nba_teams:
        # Add base word to list
        update_spray_list(team)
        update_spray_list(team.capitalize())
        update_spray_list(team.upper())
        update_spray_list(team.lower())
        sports_scores_list.append(team)
        sports_scores_list.append(team.capitalize())
        sports_scores_list.append(team.upper())
        sports_scores_list.append(team.lower())

        # Get year permutation with base nba team
        generate_years(team, year_start, year_end)
        bar.next()
    bar.finish()

def generate_mlb(year_start, year_end):
    bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating nfl list", suffix='%(percent)d%%', max=len(mlb_teams))
    for team in mlb_teams:
        # Add base word to list
        update_spray_list(team)
        update_spray_list(team.capitalize())
        update_spray_list(team.upper())
        update_spray_list(team.lower())
        sports_scores_list.append(team)
        sports_scores_list.append(team.capitalize())
        sports_scores_list.append(team.upper())
        sports_scores_list.append(team.lower())

        # Get year permutation with base mlb team
        generate_years(team, year_start, year_end)
        bar.next()
    bar.finish()

def generate_nhl(year_start, year_end):
    bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating nhl list", suffix='%(percent)d%%', max=len(nfl_teams))
    for team in nhl_teams:
        # Add base word to list
        update_spray_list(team)
        update_spray_list(team.capitalize())
        update_spray_list(team.upper())
        update_spray_list(team.lower())
        sports_scores_list.append(team)
        sports_scores_list.append(team.capitalize())
        sports_scores_list.append(team.upper())
        sports_scores_list.append(team.lower())

        # Get year permutation with base nhl team
        generate_years(team, year_start, year_end)
        bar.next()
    bar.finish()
        

def generate_seasons(year_start, year_end):
    bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating seasons list", suffix='%(percent)d%%', max=len(seasons))
    for season in seasons:
        # Add base word to list
        update_spray_list(season)
        update_spray_list(season.capitalize())
        update_spray_list(season.upper())
        update_spray_list(season.lower())

        # Get year permutation with base season
        generate_years(season, year_start, year_end)
        bar.next()
    bar.finish()

def generate_years(item, year_start, year_end, attr=None):
    
    # for quick mode just do simple concats with first letter capitalized
    if isYears and isQuick:
        
        for year in range(year_start, year_end+1):
            # Get basic year concat
            new_item = item + str(year)
            year_list.append(new_item.capitalize())

            # Cut year concat
            new_item = item + str(year)[-2:]
            year_list.append(new_item.capitalize())

            if attr:
                new_item = item + str(year) + attr
                year_list.append(new_item.capitalize())


    elif isYears and not isQuick:

        for year in range(year_start, year_end+1):
            # Get basic year concat
            new_item = item + str(year)
            year_list.append(new_item)
            year_list.append(new_item.capitalize())
            year_list.append(new_item.lower())
            year_list.append(new_item.upper())

            # Prepend year permutation
            new_item = str(year) + item
            year_list.append(new_item)
            year_list.append(new_item.capitalize())
            year_list.append(new_item.lower())
            year_list.append(new_item.upper())

            # Cut year concat
            new_item = item + str(year)[-2:]
            year_list.append(new_item)
            year_list.append(new_item.capitalize())
            year_list.append(new_item.lower())
            year_list.append(new_item.upper())

            # Prepend cut year concat
            new_item = str(year)[-2:] + item
            year_list.append(new_item)
            year_list.append(new_item.capitalize())
            year_list.append(new_item.lower())
            year_list.append(new_item.upper())

            if attr:
                new_item = item + str(year) + attr
                year_list.append(new_item)
                year_list.append(new_item.capitalize())
                year_list.append(new_item.lower())
                year_list.append(new_item.upper())

def generate_year_list_permutations():
    if isYears:
        bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Adding year permutations to final list", suffix='%(percent)d%%', max=len(year_list))
        for item in year_list:
            # Add base word to list
            update_spray_list(item)
            bar.next()
        bar.finish()

def gen_sports_separators(list_mode, sport, year_start, year_end):
    bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating separators list for sports scores", suffix='%(percent)d%%', max=len(sports_scores_list))

    if sport == "all" or sport == "sports":
        sport = "all"

    temp_separators = []
    if list_mode == "custom":
        temp_separators = custom_sep_list
    else:
        temp_separators = common_separators

    for team in sports_scores_list:
        if sport == "nfl" or sport == "all":
            for score in superbowl_scores:
                # Basic concat with score
                item = team + score
                generate_years(item, year_start, year_end)
                update_spray_list(item)
                # Basic prepend with score
                item = score + team
                generate_years(item, year_start, year_end)
                update_spray_list(item)
                for sep in temp_separators:
                    # Get basic permutation with separators and just score
                    item = score + sep + team
                    generate_years(item, year_start, year_end)
                    update_spray_list(item)
                    # Get basic permutation with separators and just score
                    item = team + sep + score 
                    generate_years(item, year_start, year_end)
                    update_spray_list(item)
        if sport == "nba" or sport == "all":
            for score in nbafinals_scores:
                # Basic concat with score
                item = team + score
                generate_years(item, year_start, year_end)
                update_spray_list(item)
                # Basic prepend with score
                item = score + team
                generate_years(item, year_start, year_end)
                update_spray_list(item)
                for sep in temp_separators:
                    # Get basic permutation with separators and just score
                    item = score + sep + team
                    generate_years(item, year_start, year_end)
                    update_spray_list(item)
                    # Get basic permutation with separators and just score
                    item = team + sep + score 
                    generate_years(item, year_start, year_end)
                    update_spray_list(item)
        if sport == "mlb" or sport == "all":
            for score in worldseries_scores:
                # Basic concat with score
                item = team + score
                generate_years(item, year_start, year_end)
                update_spray_list(item)
                # Basic prepend with score
                item = score + team
                generate_years(item, year_start, year_end)
                update_spray_list(item)
                for sep in temp_separators:
                    # Get basic permutation with separators and just score
                    item = score + sep + team
                    generate_years(item, year_start, year_end)
                    update_spray_list(item)
                    # Get basic permutation with separators and just score
                    item = team + sep + score 
                    generate_years(item, year_start, year_end)
                    update_spray_list(item)
        if sport == "nhl" or sport == "all":
            for score in stanleycup_scores:
                # Basic concat with score
                item = team + score
                generate_years(item, year_start, year_end)
                update_spray_list(item)
                # Basic prepend with score
                item = score + team
                generate_years(item, year_start, year_end)
                update_spray_list(item)
                for sep in temp_separators:
                    # Get basic permutation with separators and just score
                    item = score + sep + team
                    generate_years(item, year_start, year_end)
                    update_spray_list(item)
                    # Get basic permutation with separators and just score
                    item = team + sep + score 
                    generate_years(item, year_start, year_end)
                    update_spray_list(item)
        bar.next()
    bar.finish()
                    

def gen_sports_attributes(list_mode, sport, year_start, year_end):
    bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating attributes list for sports scores", suffix='%(percent)d%%', max=len(sports_scores_list))
    if sport == "all" or sport == "sports":
        sport = "all"

    temp_attrs = []
    if list_mode == "custom":
        temp_attrs = custom_attr_list
    else:
        temp_attrs = attributes

    for team in sports_scores_list:
        if sport == "nfl" or sport == "all":
            for score in superbowl_scores:
                # Basic concat with score
                item = team + score
                generate_years(item, year_start, year_end)
                update_spray_list(item)
                # Basic prepend with score
                item = score + team
                generate_years(item, year_start, year_end)
                update_spray_list(item)
                for attr in temp_attrs:
                    # Get basic concat
                    item = team + score + attr
                    generate_years(item, year_start, year_end)
                    update_spray_list(item)
                    # Prepend permutation
                    item = score + attr + team
                    generate_years(item, year_start, year_end)
                    update_spray_list(item)
        if sport == "nba" or sport == "all":
            for score in nbafinals_scores:
                # Basic concat with score
                item = team + score
                generate_years(item, year_start, year_end)
                update_spray_list(item)
                # Basic prepend with score
                item = score + team
                generate_years(item, year_start, year_end)
                update_spray_list(item)
                for attr in temp_attrs:
                    # Get basic concat
                    item = team + score + attr
                    generate_years(item, year_start, year_end)
                    update_spray_list(item)
                    # Prepend permutation
                    item = score + attr + team
                    generate_years(item, year_start, year_end)
                    update_spray_list(item)
        if sport == "mlb" or sport == "all":
            for score in worldseries_scores:
                # Basic concat with score
                item = team + score
                generate_years(item, year_start, year_end)
                update_spray_list(item)
                # Basic prepend with score
                item = score + team
                generate_years(item, year_start, year_end)
                update_spray_list(item)
                for attr in temp_attrs:
                    # Get basic concat
                    item = team + score + attr
                    generate_years(item, year_start, year_end)
                    update_spray_list(item)
                    # Prepend permutation
                    item = score + attr + team
                    generate_years(item, year_start, year_end)
                    update_spray_list(item)
        if sport == "nhl" or sport == "all":
            for score in stanleycup_scores:
                # Basic concat with score
                item = team + score
                generate_years(item, year_start, year_end)
                update_spray_list(item)
                # Basic prepend with score
                item = score + team
                generate_years(item, year_start, year_end)
                update_spray_list(item)
                for attr in temp_attrs:
                    # Get basic concat
                    item = team + score + attr
                    generate_years(item, year_start, year_end)
                    update_spray_list(item)
                    # Prepend permutation
                    item = score + attr + team
                    generate_years(item, year_start, year_end)
                    update_spray_list(item)
        bar.next()
    bar.finish()

def gen_sports_attrs_separators(list_mode, sport, year_start, year_end):
    bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating attributes + separators list for sports scores", suffix='%(percent)d%%', max=len(sports_scores_list))
    if sport == "all" or sport == "sports":
        sport = "all"

    temp_separators = []
    temp_attrs = []
    if list_mode == "custom":
        temp_separators = custom_sep_list
        temp_attrs = custom_attr_list
    else:
        temp_separators = common_separators
        temp_attrs = attributes

    for team in sports_scores_list:
        if sport == "nfl" or sport == "all":
            for score in superbowl_scores:
                # Basic concat with score
                item = team + score
                generate_years(item, year_start, year_end)
                update_spray_list(item)
                # Basic prepend with score
                item = score + team
                generate_years(item, year_start, year_end)
                update_spray_list(item)
                for attr in temp_attrs:
                    for sep in temp_separators:
                        # Get basic permutation with separators
                        item = team + sep + score + attr
                        generate_years(item, year_start, year_end)
                        update_spray_list(item)
                        # Get basic permutation with separators
                        item = score + attr + sep + team
                        generate_years(item, year_start, year_end)
                        update_spray_list(item)
        elif sport == "nba" or sport == "all":
            for score in nbafinals_scores:
                # Basic concat with score
                item = team + score
                generate_years(item, year_start, year_end)
                update_spray_list(item)
                # Basic prepend with score
                item = score + team
                generate_years(item, year_start, year_end)
                update_spray_list(item)
                for attr in temp_attrs:
                    for sep in temp_separators:
                        # Get basic permutation with separators
                        item = team + sep + score + attr
                        generate_years(item, year_start, year_end)
                        update_spray_list(item)
                        # Get basic permutation with separators
                        item = score + attr + sep + team
                        generate_years(item, year_start, year_end)
                        update_spray_list(item)
        elif sport == "mlb" or sport == "all":
            for score in worldseries_scores:
                # Basic concat with score
                item = team + score
                generate_years(item, year_start, year_end)
                update_spray_list(item)
                # Basic prepend with score
                item = score + team
                generate_years(item, year_start, year_end)
                update_spray_list(item)
                for attr in temp_attrs:
                    for sep in temp_separators:
                        # Get basic permutation with separators
                        item = team + sep + score + attr
                        generate_years(item, year_start, year_end)
                        update_spray_list(item)
                        # Get basic permutation with separators
                        item = score + attr + sep + team
                        generate_years(item, year_start, year_end)
                        update_spray_list(item)
        elif sport == "nhl" or sport == "all":
            for score in stanleycup_scores:
                # Basic concat with score
                item = team + score
                generate_years(item, year_start, year_end)
                update_spray_list(item)
                # Basic prepend with score
                item = score + team
                generate_years(item, year_start, year_end)
                update_spray_list(item)
                for attr in temp_attrs:
                    for sep in temp_separators:
                        # Get basic permutation with separators
                        item = team + sep + score + attr
                        generate_years(item, year_start, year_end)
                        update_spray_list(item)
                        # Get basic permutation with separators
                        item = score + attr + sep + team
                        generate_years(item, year_start, year_end)
                        update_spray_list(item)
        bar.next()
    bar.finish()


def gen_separators(list_mode, year_start, year_end):
    temp_list = spray_list.copy()
    bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating separators list", suffix='%(percent)d%%', max=len(temp_list))
    if list_mode == "custom":
        for item in temp_list.values():
            for sep in custom_sep_list:
                # Get year permutation with separators
                new_item = item + sep
                generate_years(new_item, year_start, year_end)
                sep_list.append(new_item)
                # Get year permutation with separators prepend
                new_item = sep + item
                generate_years(new_item, year_start, year_end)
                sep_list.append(new_item)
            bar.next()
    else:
        for item in temp_list.values():
            for sep in common_separators:
                # Get year permutation with separators
                new_item = item + sep
                generate_years(new_item, year_start, year_end)
                sep_list.append(new_item)
                # Get year permutation with separators prepend
                new_item = sep + item
                generate_years(new_item, year_start, year_end)
                sep_list.append(new_item)
            bar.next()
    bar.finish()

def gen_attributes(list_mode, year_start, year_end):
    temp_list = spray_list.copy()
    bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating attributes list", suffix='%(percent)d%%', max=len(temp_list))
    if list_mode == "custom":
        for item in temp_list.values():
            for attr in custom_attr_list:
                # Get basic concat
                new_item = item + attr
                generate_years(new_item, year_start, year_end)
                attr_list.append(new_item)

                # Prepend custom permutation
                new_item = attr + item
                generate_years(new_item, year_start, year_end)
                attr_list.append(new_item)

                # Append custom permutation
                generate_years(item, year_start, year_end, attr)
                attr_list.append(item)
            bar.next()
    else:
        for item in temp_list.values():
            for attr in attributes:
                # Get basic concat
                new_item = item + attr
                # only concat with ! before the year for quick mode
                if isQuick and attr in ("!"):
                    generate_years(new_item, year_start, year_end)
                elif not isQuick:
                    generate_years(new_item, year_start, year_end)
                
                # only add just the raw concat if the item is not a month or season for quick mode
                if isQuick and item not in months and item not in seasons:
                    attr_list.append(new_item)
                elif not isQuick:
                    attr_list.append(new_item)

                # Prepend permutation if quick mode isn't selected
                if not isQuick:
                    new_item = attr + item
                    generate_years(new_item, year_start, year_end)
                    attr_list.append(new_item)

                # Append permutation but just use the default '!' or '#' variations since they make the most sense when combined with years
                if attr in ("!", "!!", "#", "##"):
                    generate_years(item, year_start, year_end, attr)
            bar.next()
    bar.finish()

def gen_attrs_separators(list_mode, year_start, year_end):
    temp_list = spray_list.copy()
    bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating attributes + separators list", suffix='%(percent)d%%', max=len(temp_list))
    if list_mode == "custom":
        for item in temp_list.values():
            for attr in custom_attr_list:
                for sep in custom_sep_list:
                    # Permutation separator and attribute
                    new_item = item + sep + attr
                    generate_years(new_item, year_start, year_end)
                    attr_sep_list.append(new_item)
                    # Prepend separator and attribute
                    new_item = attr + sep + item
                    generate_years(new_item, year_start, year_end)
                    attr_sep_list.append(new_item)
            bar.next()
    else: 
        for item in temp_list.values():
            for attr in attributes:
                for sep in common_separators:
                    # Permutation separator and attribute
                    new_item = item + sep + attr
                    generate_years(new_item, year_start, year_end)
                    attr_sep_list.append(new_item)
                    # Prepend separator and attribute
                    new_item = attr + sep + item
                    generate_years(new_item, year_start, year_end)
                    attr_sep_list.append(new_item)
            bar.next()
    bar.finish()


# If the letter mode is enabled this will iterate over all generated items and do a replacement on common letters for 1337 speak or other common substitutes
def gen_letter_replacement():
    # Letters list, mostly common vowels with some common consonants
    letters = "AEIOSaeios"
    temp_list = spray_list.copy()
    bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating letter replacement list", suffix='%(percent)d%%', max=len(temp_list))
    for item in temp_list.values():
        for l in letters:
            if l.lower() == "a":
                new_item = item.replace(l.lower(), "4")
                update_spray_list(new_item)
                new_item = item.replace(l.lower(), "@")
                update_spray_list(new_item)
            if l.lower() == "e":
                new_item = item.replace(l.lower(), "3")
                update_spray_list(new_item)
            if l.lower() == "i":
                new_item = item.replace(l.lower(), "1")
                update_spray_list(new_item)
                new_item = item.replace(l.lower(), "!")
                update_spray_list(new_item)
            if l.lower() == "o":
                new_item = item.replace(l.lower(), "0")
                update_spray_list(new_item)
            if l.lower() == "s":
                new_item = item.replace(l.lower(), "5")
                update_spray_list(new_item)
                new_item = item.replace(l.lower(), "$")
                update_spray_list(new_item)
        bar.next()

def combine_attrs_separators():

    print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Adding relevant attribute/separator permutations to final list, this could take some time...")

    bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Progress", suffix='%(percent)d%%', max=3)

    # Multi threading each call to speed things up since each of these steps is independent of the other
    sep_thread = threading.Thread(target=combine_seps, args=[])
    attr_thread = threading.Thread(target=combine_attrs, args=[])
    attr_sep_thread= threading.Thread(target=cobmine_attr_seps, args=[])

    sep_thread.start()
    attr_thread.start()
    attr_sep_thread.start()

    sep_thread.join()
    bar.next()
    attr_thread.join()
    bar.next()
    attr_sep_thread.join()
    bar.next()
    bar.finish()


def combine_seps():
    if len(sep_list) > 0:
        for sep in sep_list:
            update_spray_list(sep)
def combine_attrs():
    if len(attr_list) > 0:
        for attr in attr_list:
            update_spray_list(attr)
def cobmine_attr_seps():
    if len(attr_sep_list) > 0:
        for item in attr_sep_list:
            update_spray_list(item)

def add_separators(separator):
    common_separators.append(separator)

def add_attributes(attr):
    attributes.append(attr)

def generate_sports(year_start, year_end):
    generate_nfl(year_start, year_end)
    generate_nba(year_start, year_end)
    generate_mlb(year_start, year_end)
    generate_nhl(year_start, year_end)

def generate_all(year_start, year_end):
    if len(custom_wordlist) > 0:
        generate_custom(year_start, year_end)
    generate_months(year_start, year_end)
    generate_seasons(year_start, year_end)
    generate_password_perms(year_start, year_end)
    generate_sports(year_start, year_end)


def main():

    banner = '''
     _
    (  \_
    (    \_
    (       \_  
    (         \_            ___
    ( Password   \         |   |
    (   Spray     |คคคคคคคค|___|
    (           _ /          |
    (       _ /         /~~~~~~~~~\\
    (   _ /            (  Spray    )
    (_/                 |  This   |
                        |         |
                        | Get     |
                        |  Creds  |
                        |_________|

    Original Art by Alex Chudnovsky (Unaffiliated)
    Spraygen tool by 3ndG4me
    Version 1.6
    '''

    print(Fore.BLUE + banner + Style.RESET_ALL)

    parser = argparse.ArgumentParser(description='Parse Spray List Arguments.')
    parser.add_argument('--year_start', help="starting year for a range of years", type=int)
    parser.add_argument('--year_end', help="ending year for a range of years", type=int)
    parser.add_argument('-s', metavar='separators', help="a comma delimited list of one or more separators", type=str)
    parser.add_argument('-a', metavar='attributes', help="a comma delimited list of one or more attributes", type=str)
    parser.add_argument('-w', metavar='wordlist', help="path to a custom wordlist", type=str)
    parser.add_argument('-n', metavar='single word', help="single custom word to generate a custom wordlist with", type=str)
    parser.add_argument('--mode', help="Mode for list generation. Can be all, no separators, no attributes, only years, plain, letter, quick, or custom (will only use parameters passed into -s or -a).", choices=['all', 'nosep', 'noattr', 'years', 'plain', 'letter', 'quick', 'custom'], default="all", type=str)
    parser.add_argument('--type', help="Type of list to generate. Can be all, iterative, sports, nfl, nba, mlb, nhl, months, seasons, password, common, short, or custom. Choosing 'all' executes all options except for 'iterative' which must be run manually.", choices=['all', 'iterative', 'sports', 'nfl', 'nba', 'mlb', 'nhl', 'months', 'seasons', 'password', 'common', 'short', 'custom'], default="all", type=str, nargs="+")
    parser.add_argument('--iter', help="Keyspace mode for iterative list generation. Only works when --type is set to 'iterative'. Can be ascii, num, spec, asciinum, asciispec, numspec, or full. Will generate all permutations of the selected keyspace with a given length set with the --size parameter.", choices=['ascii', 'num', 'spec', 'asciinum', 'asciispec', 'numspec', 'full'], default="full", type=str)
    parser.add_argument('--size', help="Length of passwords generated by a set keyspace. Only works when --type is set to 'iterative' and an --iter keyspace mode is set.", default="4", type=int)
    parser.add_argument('--min_length', help="Minimum length of passwords to include in the list. (Default: 1)", default=1, type=int)
    parser.add_argument('--max_length', help="Maximum length of passwords to include in the list (Default: 999)", default=999, type=int)
    parser.add_argument('-o', metavar='output file', help="name of a file to create and write the final output to", type=str)
    parser.add_argument('-p', action="store_true", help="prints the output line by line as plaintext", dest="p")
    parser.add_argument('--sort', help="Sort final output. Sorting methods supported are nosort, asc, desc, random.", choices=['nosort', 'asc', 'desc', 'random'], default="nosort", type=str)
    parser.add_argument('-v', action="store_true", help="prints the current version of spraygen and exits", dest="v")

    args = parser.parse_args()

    if args.v:
        print("Spraygen Version: 1.6")
        return

    if args.year_start == None:
        print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Year Start not provided, setting to current year...")
        args.year_start = datetime.now().year

    if args.year_end == None:
        print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Year End not provided, setting to current year...")
        args.year_end = datetime.now().year

    if args.s != None:
        print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Adding custom separators to list...")
        temp_list = args.s.split(",")
        bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Progress", suffix='%(percent)d%%', max=len(temp_list))
        if args.mode == "custom":
            for sep in temp_list:
                custom_sep_list.append(sep)
                bar.next()
        else:
            for sep in temp_list:
                common_separators.append(sep)
                bar.next()
        bar.finish()
        print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL +  "--- custom separators added in %s seconds ---" % (time.time() - start_time))
    if args.a != None:
        print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Adding custom attributes to list...")
        temp_list = args.a.split(",")
        bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Progress", suffix='%(percent)d%%', max=len(temp_list))
        if args.mode == "custom":
            for attr in temp_list:
                custom_attr_list.append(attr)
                bar.next()
        else:
            for attr in temp_list:
                attr_list.append(attr)
                bar.next()
        bar.finish()
        print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL +  "--- custom attributes added in %s seconds ---" % (time.time() - start_time))
    if args.w != None:
        print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Creating custom wordlist...")
        fileSize = open(args.w, "r")
        bar = Bar(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Progress", suffix='%(percent)d%%', max=len(fileSize.readlines()))
        fileSize.close()

        global custom_wordlist

        customFile = open(args.w, "r")
        for item in customFile:
            custom_wordlist.append(item.strip())
            bar.next()
        customFile.close()
        bar.finish()
        # Filter any blank lines
        custom_wordlist = list(filter(None, custom_wordlist))

        print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL +  "--- custom wordlist loaded in %s seconds ---" % (time.time() - start_time))
    if args.n != None:
        custom_wordlist.append(args.n)
        
    # Set password length filters
    global max_length
    global min_length
    max_length = args.max_length
    min_length = args.min_length
    
    if args.mode != "all":
        global isPlain
        global isYears
        global isNotSep
        global isNoAttr
        global isLetter
        global isQuick
        if args.mode == "plain":
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating PLAIN list...")
            isPlain = True
            isYears = False
            isNotSep = True
            isNoAttr = True
        elif args.mode == "nosep":
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating NO SEPARATOR list...")
            isNotSep = True
        elif args.mode == "noattr":
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating NO ATTRIBUTE list...")
            isNoAttr = True
        elif args.mode == "years":
            isPlain = False
            isYears = True
            isNotSep = True
            isNoAttr = True
        elif args.mode == "letter":
            isLetter = True
        elif args.mode == "custom":
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating CUSTOM SEPARATOR/ATTRIBUTE list...")
            isPlain = True
            isYears = True
            isNotSep = True
            isNoAttr = True
        elif args.mode == "quick":
            isQuick = True
            isPlain = False
            isNotSep = True
            isYears = True
    
    if "all" not in args.type:
        if "months" in args.type:
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating MONTHS list...")
            generate_months(args.year_start, args.year_end)
            print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL +  "--- generated months in %s seconds ---" % (time.time() - start_time))
        if "iterative" in args.type:
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating ITERATIVE list...")
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "List size will be: " + str(args.size))
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "List keyspace will be: " + args.iter)
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "This is generating literally every permutation in that keyspace, this will take some time...")
            generate_keyspace_list(args.iter, args.size, args.year_start, args.year_end)
            print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL +  "--- generated iterative in %s seconds ---" % (time.time() - start_time))
        if "sports" in args.type:
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating SPORTS list...")
            generate_sports(args.year_start, args.year_end)
            print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL +  "--- generated sports in %s seconds ---" % (time.time() - start_time))
        if "nfl" in args.type:
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating NFL list...")
            generate_nfl(args.year_start, args.year_end)
            print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL +  "--- generated nfl in %s seconds ---" % (time.time() - start_time))
        if "nba" in args.type:
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating NBA list...")
            generate_nba(args.year_start, args.year_end)
            print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL +  "--- generated nba in %s seconds ---" % (time.time() - start_time))
        if "mlb" in args.type:
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating MLB list...")
            generate_mlb(args.year_start, args.year_end)
            print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL +  "--- generated mlb in %s seconds ---" % (time.time() - start_time))
        if "nhl" in args.type:
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating NHL list...")
            generate_nhl(args.year_start, args.year_end)
            print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL +  "--- generated nhl in %s seconds ---" % (time.time() - start_time))
        if "seasons" in args.type:
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating SEASONS list...")
            generate_seasons(args.year_start, args.year_end)
            print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL +  "--- generated seasons in %s seconds ---" % (time.time() - start_time))
        if "password" in args.type:
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating PASSWORD list...")
            generate_password_perms(args.year_start, args.year_end)
            print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL +  "--- generated 'password' in %s seconds ---" % (time.time() - start_time))
        if "custom" in args.type:
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating CUSTOM list...")
            generate_custom(args.year_start, args.year_end)
            print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL +  "--- generated custom in %s seconds ---" % (time.time() - start_time))
        if "common" in args.type:
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating COMMON list...")
            generate_common(args.year_start, args.year_end)
            print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL +  "--- generated common list in %s seconds ---" % (time.time() - start_time))
        if "short" in args.type:
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating SHORT list...")
            generate_short(args.year_start, args.year_end)
            print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL +  "--- generated short list in %s seconds ---" % (time.time() - start_time))
    else:
        print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating ALL list...(If a custom wordlist is specified it will be used)")
        generate_all(args.year_start, args.year_end)
        print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL +  "--- generated all in %s seconds ---" % (time.time() - start_time))

    if isNotSep == False:
        print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating separators...")
        gen_separators(args.mode, args.year_start, args.year_end)
        if len(sports_scores_list) > 0:
            gen_sports_separators(args.mode, args.type, args.year_start, args.year_end)
        print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL +  "--- separators generated in %s seconds ---" % (time.time() - start_time))
    if isNoAttr == False:
        print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating attributes...")
        gen_attributes(args.mode, args.year_start, args.year_end)
        if len(sports_scores_list) > 0:
            gen_sports_attributes(args.mode, args.type, args.year_start, args.year_end)
        print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL +  "--- attributes generated in %s seconds ---" % (time.time() - start_time))
    if isNotSep == False and isNoAttr == False:
        print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating attributes + separators...")
        gen_attrs_separators(args.mode, args.year_start, args.year_end)
        if len(sports_scores_list) > 0:
            gen_sports_attrs_separators(args.mode, args.type, args.year_start, args.year_end)
        print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL +  "--- attribute + separators generated in %s seconds ---" % (time.time() - start_time))
    if args.mode == "custom":
        if len(custom_sep_list) > 0:
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating custom separators list...")
            gen_separators(args.mode, args.year_start, args.year_end)
            if len(sports_scores_list) > 0:
                gen_sports_separators(args.mode, args.type, args.year_start, args.year_end)
            print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL +  "--- custom separators generated in %s seconds ---" % (time.time() - start_time))
        if len(custom_attr_list) > 0:
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating custom attributes list...")
            gen_attributes(args.mode, args.year_start, args.year_end)
            if len(sports_scores_list) > 0:
                gen_sports_attributes(args.mode, args.type, args.year_start, args.year_end)
            print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL +  "--- custom attributes generated in %s seconds ---" % (time.time() - start_time))
        if len(custom_sep_list) > 0:
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating custom attributes + separators list...")
            gen_attrs_separators(args.mode, args.year_start, args.year_end)
            if len(sports_scores_list) > 0:
                gen_sports_attrs_separators(args.mode, args.type, args.year_start, args.year_end)
            print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL +  "--- custom attributes + separators generated in %s seconds ---" % (time.time() - start_time))
    elif isPlain == True or (isNotSep == True and isNoAttr == True):
        print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Skipping separators and attributes...")

    print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Adding new generated items to the list...")
    combine_attrs_separators()
    generate_year_list_permutations()
   
    if isLetter:
        print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating letter replacement...")
        gen_letter_replacement()
        print(Fore.GREEN + "\n[+] Success: " + Style.RESET_ALL +  "--- letter replacement generated in %s seconds ---" % (time.time() - start_time))

    print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL +  "--- initial list built in %s seconds ---" % (time.time() - start_time))
    print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL + "Bulding final list!")

    final_list = list(spray_list.values())
    if args.sort == "asc":
        final_list.sort()
    elif args.sort == "desc":
        final_list.sort(reverse=True)
    elif args.sort == "random":
        random.shuffle(final_list)


    if args.o != None:
        print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL + "Writing output to: " + args.o)
        f = open(args.o, "a")
        bar = Bar(Fore.GREEN + "[*] Success: " + Style.RESET_ALL + "Progress", suffix='%(percent)d%%', max=len(final_list))
        for password in final_list:
            f.write(password + "\n")
            bar.next()
        f.close()
        bar.finish()

    if args.p == True:
        print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL + "Printing final list:")
        for password in final_list:
            print(password)

    print(Fore.GREEN + "\n[+] Success: " + Style.RESET_ALL +  "--- finished in %s seconds ---" % (time.time() - start_time))
    print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL + "Done!")


try:
    main()
except Exception as e:
    print(Fore.RED + "\n[!] Error: " + Style.RESET_ALL + str(e))