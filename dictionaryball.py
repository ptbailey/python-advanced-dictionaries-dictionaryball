################################################################################
# make dictionary first

## do home team first
h_team_name = 'Brooklyn Nets'
h_colors = ['Black', "White"]

stats_aa_keys = ('number',"shoe","points","rebounds", "assists", \
"steals", "blocks", "slam_dunks")
stats_aa_values = (0, 16, 22, 12, 12, 3, 1, 1)
stats_aa = dict(zip(stats_aa_keys, stats_aa_values))

stats_re_keys = ('number',"shoe","points","rebounds", "assists", \
"steals", "blocks", "slam_dunks")
stats_re_values = (30, 14, 12, 12, 12, 12, 12, 7)
stats_re = dict(zip(stats_re_keys, stats_re_values))

stats_bl_keys = ('number',"shoe","points","rebounds", "assists", \
"steals", "blocks", "slam_dunks")
stats_bl_values = (11, 17, 17, 19, 10, 3, 1, 15)
stats_bl = dict(zip(stats_bl_keys, stats_bl_values))

stats_mp_keys = ('number',"shoe","points","rebounds", "assists", \
"steals", "blocks", "slam_dunks")
stats_mp_values = (1, 19, 26, 12, 6, 3, 8, 5)
stats_mp = dict(zip(stats_mp_keys, stats_mp_values))

stats_jt_keys = ('number',"shoe","points","rebounds", "assists", \
"steals", "blocks", "slam_dunks")
stats_jt_values = (31, 15, 19, 2, 2, 4, 11, 1)
stats_jt = dict(zip(stats_jt_keys, stats_jt_values))

h_players = {'Alan Anderson' : stats_aa, 'Reggie Evans' : stats_re, \
'Brook Lopez' : stats_bl, 'Mason Plumlee' : stats_mp, 'Jason Terry' : stats_jt}

home_team = {'team_name' : h_team_name, 'colors' : h_colors, \
'players' : h_players}

## now do same for away team
a_team_name = 'Charlotte Hornets'
a_colors = ['Turquoise', 'Purple']

stats_keys = ('number',"shoe","points","rebounds", "assists", \
"steals", "blocks", "slam_dunks")

stats_ja_values = (4,18,10,1,1,2,7,2)
stats_bb_values = (0,16,12,4,7,7,15,10)
stats_dd_values = (2,14,24,12,12,4,5,5)
stats_bg_values = (8,15,33,3,2,1,1,0)
stats_bh_values = (33,15,6,12,12,22,5,12)

stats_ja = dict(zip(stats_keys, stats_ja_values))
stats_bb = dict(zip(stats_keys, stats_bb_values))
stats_dd = dict(zip(stats_keys, stats_dd_values))
stats_bg = dict(zip(stats_keys, stats_bg_values))
stats_bh = dict(zip(stats_keys, stats_bh_values))

a_players = {
"Jeff Adrien" : stats_ja,
"Bismak Biyombo" : stats_bb,
"DeSagna Diop" : stats_dd,
"Ben Gordon" : stats_bg,
"Brendan Haywood" : stats_bh
}

away_team = {'team_name' : a_team_name, 'colors' : a_colors, \
'players' : a_players}

# combine to make one dictionary!
game_dictionary = {'home' : home_team, 'away' : away_team}

################################################################################
# we define our dictionary for reusable use. if we had another .py
# file and want to reference the dictionary in this library, you can
# just call the definition assigned to the dictionary
def game_dict():
    return game_dictionary

# given function for practice:
def home_team_name():
    return game_dict()['home']['team_name']

## build functions
def num_points_scored(player_name):
    try:
        return game_dict()['away']['players'][player_name]['points']
    except KeyError:
        return game_dict()['home']['players'][player_name]['points']

def shoe_size():
    pass

def team_colors():
    pass

def team_names():
    pass

def player_numbers():
    pass

def player_stats():
    pass

# # testing, testing
# def good_practices():
#     for location, team_stats in game_dict().items():
#     # are you ABSOLUTELY SURE what 'location' and 'team_stats' are? use pdb.set_trace() to find out!
#         import pdb; pdb.set_trace()
#         for stats, data in team_stats.items():
#         # are you ABSOLUTELY SURE what 'stats' and 'data' are? use pdb.set_trace() to find out!
#             import pdb; pdb.set_trace()
#         # what is 'data' at each level of the for loop block? when will we be able to iterate through a list?
#         # When would the following line of code break?
#             for item in data:
#                 print(item)
