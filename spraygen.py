#!/usr/bin/env python3

import argparse
from datetime import datetime
from colorama import init, Fore, Back, Style

# Colorama init call
init()

# Globals for separators and attribute toggles
isPlain = False
isNotSep = False
isNoAttr = False

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

# Global spray list, this is the final password list everything is appended to
spray_list = []

def generate_custom(year_start, year_end):
    for word in custom_wordlist:
        # Add base word to list
        spray_list.append(word)
        spray_list.append(word.upper())
        spray_list.append(word.lower())
        # Get year permutation with base month
        generate_years(word, year_start, year_end)


def generate_password_perms(year_start, year_end):
    for password in password_permutations:
        # Add base word to list
        spray_list.append(password)
        spray_list.append(password.upper())
        spray_list.append(password.lower())
        # Get year permutation with base month
        generate_years(password, year_start, year_end)

def generate_months(year_start, year_end):
    for month in months:
        # Add base word to list
        spray_list.append(month)
        spray_list.append(month.upper())
        spray_list.append(month.lower())
        # Get year permutation with base month
        generate_years(month, year_start, year_end)


def generate_nfl(year_start, year_end):
    for team in nfl_teams:
        # Add base word to list
        spray_list.append(team)
        spray_list.append(team.upper())
        spray_list.append(team.lower())
        sports_scores_list.append(team)
        sports_scores_list.append(team.upper())
        sports_scores_list.append(team.lower())

        # Get year permutation with base month
        generate_years(team, year_start, year_end)


def generate_nba(year_start, year_end):
    for team in nba_teams:
        # Add base word to list
        spray_list.append(team)
        spray_list.append(team.upper())
        spray_list.append(team.lower())
        sports_scores_list.append(team)
        sports_scores_list.append(team.upper())
        sports_scores_list.append(team.lower())

        # Get year permutation with base month
        generate_years(team, year_start, year_end)

def generate_mlb(year_start, year_end):
    for team in mlb_teams:
        # Add base word to list
        spray_list.append(team)
        spray_list.append(team.upper())
        spray_list.append(team.lower())
        sports_scores_list.append(team)
        sports_scores_list.append(team.upper())
        sports_scores_list.append(team.lower())

        # Get year permutation with base month
        generate_years(team, year_start, year_end)

def generate_nhl(year_start, year_end):
    for team in nhl_teams:
        # Add base word to list
        spray_list.append(team)
        spray_list.append(team.upper())
        spray_list.append(team.lower())
        sports_scores_list.append(team)
        sports_scores_list.append(team.upper())
        sports_scores_list.append(team.lower())

        # Get year permutation with base month
        generate_years(team, year_start, year_end)

def generate_seasons(year_start, year_end):
    for season in seasons:
        # Add base word to list
        spray_list.append(season)
        spray_list.append(season.upper())
        spray_list.append(season.lower())

        # Get year permutation with base month
        generate_years(season, year_start, year_end)

def generate_years(item, year_start, year_end):
    for year in range(year_start, year_end+1):
        # Get basic year concat
        new_item = item + str(year)
        year_list.append(new_item)
        year_list.append(new_item.lower())
        year_list.append(new_item.upper())

        # Prepend year permutation
        new_item = str(year) + item
        year_list.append(new_item.lower())
        year_list.append(new_item.upper())
        year_list.append(new_item)

        # Cut year concat
        new_item = item + str(year)[-2:]
        year_list.append(new_item.lower())
        year_list.append(new_item.upper())
        year_list.append(new_item)

        # Prepend cut year concat
        new_item = str(year)[-2:] + item
        year_list.append(new_item.lower())
        year_list.append(new_item.upper())
        year_list.append(new_item)

def generate_year_list_permutations():
    for item in year_list:
        # Add base word to list
        spray_list.append(item)

def gen_sports_separators(year_start, year_end):
    for team in sports_scores_list:
        for score in superbowl_scores:
            # Basic concat with score
            item = team + score
            generate_years(item, year_start, year_end)
            spray_list.append(item)
            # Basic prepend with score
            item = score + team
            generate_years(item, year_start, year_end)
            spray_list.append(item)
        for score in nbafinals_scores:
            # Basic concat with score
            item = team + score
            generate_years(item, year_start, year_end)
            spray_list.append(item)
            # Basic prepend with score
            item = score + team
            generate_years(item, year_start, year_end)
            spray_list.append(item)
        for score in worldseries_scores:
            # Basic concat with score
            item = team + score
            generate_years(item, year_start, year_end)
            spray_list.append(item)
            # Basic prepend with score
            item = score + team
            generate_years(item, year_start, year_end)
            spray_list.append(item)
        for score in stanleycup_scores:
            # Basic concat with score
            item = team + score
            generate_years(item, year_start, year_end)
            spray_list.append(item)
            # Basic prepend with score
            item = score + team
            generate_years(item, year_start, year_end)
            spray_list.append(item)
            for sep in common_separators:
                # Get basic permutation with separators and just score
                item = score + sep + team
                generate_years(item, year_start, year_end)
                spray_list.append(item)
                # Get basic permutation with separators and just score
                item = team + sep + score 
                generate_years(item, year_start, year_end)
                spray_list.append(item)
                    

def gen_sports_attributes(year_start, year_end):
    for team in sports_scores_list:
        for score in superbowl_scores:
            # Basic concat with score
            item = team + score
            generate_years(item, year_start, year_end)
            spray_list.append(item)
            # Basic prepend with score
            item = score + team
            generate_years(item, year_start, year_end)
            spray_list.append(item)
        for score in nbafinals_scores:
            # Basic concat with score
            item = team + score
            generate_years(item, year_start, year_end)
            spray_list.append(item)
            # Basic prepend with score
            item = score + team
            generate_years(item, year_start, year_end)
            spray_list.append(item)
        for score in worldseries_scores:
            # Basic concat with score
            item = team + score
            generate_years(item, year_start, year_end)
            spray_list.append(item)
            # Basic prepend with score
            item = score + team
            generate_years(item, year_start, year_end)
            spray_list.append(item)
        for score in stanleycup_scores:
            # Basic concat with score
            item = team + score
            generate_years(item, year_start, year_end)
            spray_list.append(item)
            # Basic prepend with score
            item = score + team
            generate_years(item, year_start, year_end)
            spray_list.append(item)
            for attr in attributes:
                # Get basic concat
                item = team + score + attr
                generate_years(item, year_start, year_end)
                spray_list.append(item)
                # Prepend permutation
                item = score + attr + team
                generate_years(item, year_start, year_end)
                spray_list.append(item)

def gen_sports_attrs_separators(year_start, year_end):
    for team in sports_scores_list:
        for score in superbowl_scores:
            # Basic concat with score
            item = team + score
            generate_years(item, year_start, year_end)
            spray_list.append(item)
            # Basic prepend with score
            item = score + team
            generate_years(item, year_start, year_end)
            spray_list.append(item)
        for score in nbafinals_scores:
            # Basic concat with score
            item = team + score
            generate_years(item, year_start, year_end)
            spray_list.append(item)
            # Basic prepend with score
            item = score + team
            generate_years(item, year_start, year_end)
            spray_list.append(item)
        for score in worldseries_scores:
            # Basic concat with score
            item = team + score
            generate_years(item, year_start, year_end)
            spray_list.append(item)
            # Basic prepend with score
            item = score + team
            generate_years(item, year_start, year_end)
            spray_list.append(item)
        for score in stanleycup_scores:
            # Basic concat with score
            item = team + score
            generate_years(item, year_start, year_end)
            spray_list.append(item)
            # Basic prepend with score
            item = score + team
            generate_years(item, year_start, year_end)
            spray_list.append(item)
            for attr in attributes:
                for sep in common_separators:
                    # Get basic permutation with separators
                    item = team + sep + score + attr
                    generate_years(item, year_start, year_end)
                    spray_list.append(item)
                    # Get basic permutation with separators
                    item = score + attr + sep + team
                    generate_years(item, year_start, year_end)
                    spray_list.append(item)


def gen_separators(year_start, year_end):
    temp_list = spray_list.copy()
    for item in temp_list:
        for sep in common_separators:
            # Get year permutation with separators
            new_item = item + sep
            generate_years(new_item, year_start, year_end)
            sep_list.append(new_item)
            # Get year permutation with separators prepend
            new_item = sep + item
            generate_years(new_item, year_start, year_end)
            sep_list.append(new_item)

def gen_attributes(year_start, year_end):
    temp_list = spray_list.copy()
    for item in temp_list:
        for attr in attributes:
            # Get basic concat
            new_item = item + attr
            generate_years(new_item, year_start, year_end)
            attr_list.append(new_item)

            # Prepend permutation
            new_item = attr + item
            generate_years(new_item, year_start, year_end)
            attr_list.append(new_item)

def gen_attrs_separtors(year_start, year_end):
    temp_list = spray_list.copy()
    for item in temp_list:
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

def combine_attrs_separators():
    if len(sep_list) > 0:
        for sep in sep_list:
            spray_list.append(sep)
    if len(attr_list) > 0:
        for attr in attr_list:
            spray_list.append(attr)
    if len(attr_sep_list) > 0:
        for item in attr_sep_list:
            spray_list.append(item)

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
    Tool by 3ndG4me
    '''

    print(Fore.BLUE + banner + Style.RESET_ALL)

    parser = argparse.ArgumentParser(description='Parse Spray List Arguments.')
    parser.add_argument('--year_start', help="starting year for a range of years", type=int)
    parser.add_argument('--year_end', help="ending year for a range of years", type=int)
    parser.add_argument('-s', metavar='separators', help="a comma delimited list of one or more separators", type=str)
    parser.add_argument('-a', metavar='attributes', help="a comma delimited list of one or more attributes", type=str)
    parser.add_argument('-w', metavar='wordlist', help="path to a custom wordlist", type=str)
    parser.add_argument('-n', metavar='single word', help="single custom word to generate a custom wordlist with", type=str)
    parser.add_argument('--mode', help="Mode for list generation. Can be all, no separators, no attributes, or plain.", choices=['all', 'nosep', 'noattr', 'plain'], default="all", type=str)
    parser.add_argument('--type', help="Type of list to generate. Can be all, sports, months, seasons, password, or custom", choices=['all', 'sports', 'months', 'seasons', 'password', 'custom'], default="all", type=str)
    parser.add_argument('-o', metavar='output file', help="name of a file to create and write the final output to", type=str)
    parser.add_argument('-p', metavar='plaintext output', action=argparse.BooleanOptionalAction, help="prints the output line by line as plaintext", type=str)

    args = parser.parse_args()

    if args.year_start == None:
        print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Year Start not provided, setting to current year...")
        args.year_start = datetime.now().year

    if args.year_end == None:
        print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Year End not provided, setting to current year...")
        args.year_end = datetime.now().year

    if args.s != None:
        print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Adding custom separators to list...")
        temp_list = args.s.split(",")
        for sep in temp_list:
            common_separators.append(sep)

    if args.a != None:
        print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Adding custom attributes to list...")
        temp_list = args.a.split(",")
        for attr in temp_list:
            attributes.append(attr)

    if args.w != None:
        customFile = open(args.w, "r")
        for item in customFile:
            custom_wordlist.append(item)

    if args.n != None:
        custom_wordlist.append(args.n)
        

    if args.mode != "all":
        global isPlain
        global isNotSep
        global isNoAttr
        if args.mode == "plain":
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating PLAIN list...")
            isPlain = True
            isNotSep = True
            isNoAttr = True
        elif args.mode == "nosep":
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating NO SEPARATOR list...")
            isNotSep = True
        elif args.mode == "noattr":
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating NO ATTRIBUTE list...")
            isNoAttr = True

    if args.type != "all":
        if args.type == "months":
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating MONTHS list...")
            generate_months(args.year_start, args.year_end)
            generate_year_list_permutations()
        elif args.type == "sports":
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating SPORTS list...")
            generate_sports(args.year_start, year_end)
            generate_year_list_permutations()
        elif args.type == "seasons":
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating SEASONS list...")
            generate_seasons(args.year_start, args.year_end)
            generate_year_list_permutations()
        elif args.type == "password":
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating PASSWORD list...")
            generate_password_perms(args.year_start, args.year_end)
            generate_year_list_permutations()
        elif args.type == "custom":
            print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating CUSTOM list...")
            generate_custom(args.year_start, args.year_end)
            generate_year_list_permutations()
    else:
        print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating ALL list...(If a custom wordlist is specified it will be used)")
        generate_all(args.year_start, args.year_end)
        generate_year_list_permutations()

    if isNotSep == False:
        print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating separators...")
        gen_separators(args.year_start, args.year_end)
        if len(sports_scores_list) > 0:
            gen_sports_separators(args.year_start, args.year_end)
    if isNoAttr == False:
        print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating attributes...")
        gen_attributes(args.year_start, args.year_end)
        if len(sports_scores_list) > 0:
            gen_sports_attributes(args.year_start, args.year_end)
    if isNotSep == False and isNoAttr == False:
        print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Generating attributes + separators...")
        gen_attrs_separtors(args.year_start, args.year_end)
        if len(sports_scores_list) > 0:
            gen_sports_attrs_separators(args.year_start, args.year_end)
    elif isPlain == True or (isNotSep == True and isNoAttr == True):
        print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Skipping separators and attributes...")

    print(Fore.BLUE + "[*] Info: " + Style.RESET_ALL + "Adding new generated items to the list...")
    combine_attrs_separators()
    generate_year_list_permutations()


    print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL + "Bulding final list!")

    if args.o != None:
        print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL + "Writing output to: " + args.o)
        f = open(args.o, "a")
        for password in spray_list:
            f.write(password + "\n")
        f.close()

    if args.p == True:
        print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL + "Printing final list:")
        for password in spray_list:
            print(password)

    print(Fore.GREEN + "[+] Success: " + Style.RESET_ALL + "Done!")

try:
    main()
except Exception as e:
    print(Fore.RED + "[!] Error: " + Style.RESET_ALL + str(e))