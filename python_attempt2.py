import pandas as pd
import numpy as np
import scipy as sp


df = pd.read_csv('merged_data.csv', low_memory=False)
df_2 = pd.read_csv('merged_data_2.csv', low_memory=False)
df_3 = pd.read_csv('merged_data_3.csv', low_memory=False)

#print(df.sample(10))
#print(df.columns)

'''
#Whole league, EPA
correlations = df.corr()['epa'][:]
print(correlations)
correlations.to_csv('correlations.csv')

#Chiefs only, EPA
chiefs_df = df.loc[df['posteam'] == 'KC']
correlations_chiefs = chiefs_df.corr()['epa'][:]
print(correlations_chiefs)
correlations_chiefs.to_csv('correlations_chiefs.csv')

#Whole league, EPA, group by box players
box_df = df.groupby(['box_players'])
correlations_box = box_df.corr()['epa'][:]
print(correlations_box)
correlations_box.to_csv('correlations_box.csv')

#Chiefs only, EPA, group by box players
chiefs_df = df.loc[df['posteam'] == 'KC']
chiefs_box_df = chiefs_df.groupby(['box_players'])
correlations_chiefs_box = chiefs_box_df.corr()['epa'][:]
print(correlations_chiefs_box)
correlations_chiefs_box.to_csv('correlations_chiefs_box.csv')

#Whole league, group by box players, counts
box_df_counts = df.groupby(['box_players'])["box_players"].count().reset_index(name="count")
print(box_df_counts)
box_df_counts.to_csv('box_df_counts.csv')

#Chiefs only, group by box players, counts
chiefs_df = df.loc[df['posteam'] == 'KC']
chiefs_box_df_counts = chiefs_df.groupby(['box_players'])["box_players"].count().reset_index(name="count")
print(chiefs_box_df_counts)
chiefs_box_df_counts.to_csv('chiefs_box_df_counts.csv')

#Left joining the correlations and counts tables
#The reason I'm loading in new csv's is I had to add a name to one of the columns in the df, or else it wouldn't show up
correlations_chiefs_box_2 = pd.read_csv('correlations_chiefs_box_2.csv', low_memory=False)
correlations_box_2 = pd.read_csv('correlations_box_2.csv', low_memory=False)

league_box_players = pd.merge(correlations_box_2, box_df_counts, on='box_players',how='left')
league_box_players.to_csv('league_box_players.csv')
chiefs_box_players = pd.merge(correlations_chiefs_box_2, chiefs_box_df_counts, on='box_players',how='left')
chiefs_box_players.to_csv('chiefs_box_players.csv')



#Chiefs only, EPA, grouped by offense personnel
chiefs_df_2 = df_2.loc[df_2['posteam'] == 'KC']
chiefs_offense_personnel_df = chiefs_df_2.groupby(['offense_personnel'])
correlations_chiefs_offense_personnel = chiefs_offense_personnel_df.corr()['epa'][:]
print(correlations_chiefs_offense_personnel)
correlations_chiefs_offense_personnel.to_csv('correlations_chiefs_offense_personnel.csv')

#Whole league, EPA, grouped by offense personnel
offense_personnel_df = df_2.groupby(['offense_personnel'])
correlations_offense_personnel = offense_personnel_df.corr()['epa'][:]
print(correlations_offense_personnel)
correlations_offense_personnel.to_csv('correlations_offense_personnel.csv')

#Whole league, group by offensive personnel, counts
offense_personnel_df_counts = df_2.groupby(['offense_personnel'])["offense_personnel"].count().reset_index(name="count")
print(offense_personnel_df_counts)
offense_personnel_df_counts.to_csv('offense_personnel_df_counts.csv')

#Chiefs only, group by offensive personnel, counts
chiefs_df = df_2.loc[df_2['posteam'] == 'KC']
chiefs_offense_personnel_df_counts = chiefs_df.groupby(['offense_personnel'])["offense_personnel"].count().reset_index(name="count")
print(chiefs_offense_personnel_df_counts)
chiefs_offense_personnel_df_counts.to_csv('chiefs_offense_personnel_df_counts.csv')

#Left joining to combine correlations and counts
correlations_chiefs_offense_personnel_2 = pd.read_csv('correlations_chiefs_offense_personnel_2.csv', low_memory=False)
correlations_offense_personnel_2 = pd.read_csv('correlations_offense_personnel_2.csv', low_memory=False)

league_offense_personnel = pd.merge(correlations_offense_personnel_2, offense_personnel_df_counts, on='offense_personnel',how='left')
league_offense_personnel.to_csv('league_offense_personnel.csv')
chiefs_offense_personnel = pd.merge(correlations_chiefs_offense_personnel_2, chiefs_offense_personnel_df_counts, on='offense_personnel',how='left')
chiefs_offense_personnel.to_csv('chiefs_offense_personnel_.csv')

#num_pass_rush_players (filter pass plays)

#Chiefs only, EPA, grouped by num_pass_rush_players
chiefs_pass_df = df.loc[(df['posteam'] == 'KC') & (df['pass'] == 1)]
chiefs_pass_rushers_df = chiefs_pass_df.groupby(['num_pass_rush_players'])
correlations_chiefs_pass_rushers = chiefs_pass_rushers_df.corr()['epa'][:]
print(correlations_chiefs_pass_rushers)
correlations_chiefs_pass_rushers.to_csv('correlations_chiefs_pass_rushers.csv')

#Whole league, EPA, grouped by num_pass_rush_players
pass_df = df.loc[df['pass'] == 1]
pass_rushers_df = pass_df.groupby(['num_pass_rush_players'])
correlations_pass_rushers = pass_rushers_df.corr()['epa'][:]
print(correlations_pass_rushers)
correlations_pass_rushers.to_csv('correlations_pass_rushers.csv')

#Whole league, group by pass rushers, counts
pass_df = df.loc[df['pass'] == 1]
pass_rushers_df_counts = pass_df.groupby(['num_pass_rush_players'])["num_pass_rush_players"].count().reset_index(name="count")
print(pass_rushers_df_counts)
pass_rushers_df_counts.to_csv('pass_rushers_df_counts.csv')

#Chiefs only, group by pass rushers, 
chiefs_pass_df = df.loc[(df['posteam'] == 'KC') & (df['pass'] == 1)]
chiefs_pass_rushers_df_counts = chiefs_pass_df.groupby(['num_pass_rush_players'])["num_pass_rush_players"].count().reset_index(name="count")
print(chiefs_pass_rushers_df_counts)
chiefs_pass_rushers_df_counts.to_csv('chiefs_pass_rushers_df_counts.csv')

#Left joining to combine correlations and counts
correlations_chiefs_pass_rushers_2 = pd.read_csv('correlations_chiefs_pass_rushers_2.csv', low_memory=False)
correlations_pass_rushers_2 = pd.read_csv('correlations_pass_rushers_2.csv', low_memory=False)

league_pass_rushers = pd.merge(correlations_pass_rushers_2, pass_rushers_df_counts, on='num_pass_rush_players',how='left')
league_pass_rushers.to_csv('league_pass_rushers.csv')
chiefs_pass_rushers = pd.merge(correlations_chiefs_pass_rushers_2, chiefs_pass_rushers_df_counts, on='num_pass_rush_players',how='left')
chiefs_pass_rushers.to_csv('chiefs_pass_rushers_.csv')

#blitz
#Whole league, EPA, group by blitz
blitz_df = df.groupby(['blitz'])
correlations_blitz = blitz_df.corr()['epa'][:]
print(correlations_blitz)
correlations_blitz.to_csv('correlations_blitz.csv')

#Chiefs only, EPA, group by blitz
chiefs_df = df.loc[df['posteam'] == 'KC']
chiefs_blitz_df = chiefs_df.groupby(['blitz'])
correlations_chiefs_blitz = chiefs_blitz_df.corr()['epa'][:]
print(correlations_chiefs_blitz)
correlations_chiefs_blitz.to_csv('correlations_chiefs_blitz.csv')

#Whole league, group by blitz, counts
blitz_df_counts = df.groupby(['blitz'])["blitz"].count().reset_index(name="count")
print(blitz_df_counts)
blitz_df_counts.to_csv('blitz_df_counts.csv')

#Chiefs only, group by blitz, counts
chiefs_df = df.loc[df['posteam'] == 'KC']
chiefs_blitz_df_counts = chiefs_df.groupby(['blitz'])["blitz"].count().reset_index(name="count")
print(chiefs_blitz_df_counts)
chiefs_blitz_df_counts.to_csv('chiefs_blitz_df_counts.csv')

#Left join to combine correlations and counts
correlations_chiefs_blitz_2 = pd.read_csv('correlations_chiefs_blitz_2.csv', low_memory=False)
correlations_blitz_2 = pd.read_csv('correlations_blitz_2.csv', low_memory=False)

league_blitz = pd.merge(correlations_blitz_2, blitz_df_counts, on='blitz',how='left')
league_blitz.to_csv('league_blitz.csv')
chiefs_blitz = pd.merge(correlations_chiefs_blitz_2, chiefs_blitz_df_counts, on='blitz',how='left')
chiefs_blitz.to_csv('chiefs_blitz.csv')

#no_huddle
#Whole league, EPA, group by no_huddle
no_huddle_df = df.groupby(['no_huddle'])
correlations_no_huddle = no_huddle_df.corr()['epa'][:]
print(correlations_no_huddle)
correlations_no_huddle.to_csv('correlations_no_huddle.csv')

#Chiefs only, EPA, group by no_huddle
chiefs_df = df.loc[df['posteam'] == 'KC']
chiefs_no_huddle_df = chiefs_df.groupby(['no_huddle'])
correlations_chiefs_no_huddle = chiefs_no_huddle_df.corr()['epa'][:]
print(correlations_chiefs_no_huddle)
correlations_chiefs_no_huddle.to_csv('correlations_chiefs_no_huddle.csv')

#Whole league, group by no_huddle, counts
no_huddle_df_counts = df.groupby(['no_huddle'])["no_huddle"].count().reset_index(name="count")
print(no_huddle_df_counts)
no_huddle_df_counts.to_csv('no_huddle_df_counts.csv')

#Chiefs only, group by no_huddle, counts
chiefs_df = df.loc[df['posteam'] == 'KC']
chiefs_no_huddle_df_counts = chiefs_df.groupby(['no_huddle'])["no_huddle"].count().reset_index(name="count")
print(chiefs_no_huddle_df_counts)
chiefs_no_huddle_df_counts.to_csv('chiefs_no_huddle_df_counts.csv')

#Left join to combine correlations and counts
correlations_chiefs_no_huddle_2 = pd.read_csv('correlations_chiefs_no_huddle_2.csv', low_memory=False)
correlations_no_huddle_2 = pd.read_csv('correlations_no_huddle_2.csv', low_memory=False)

league_no_huddle = pd.merge(correlations_no_huddle_2, no_huddle_df_counts, on='no_huddle',how='left')
league_no_huddle.to_csv('league_no_huddle.csv')
chiefs_no_huddle = pd.merge(correlations_chiefs_no_huddle_2, chiefs_no_huddle_df_counts, on='no_huddle',how='left')
chiefs_no_huddle.to_csv('chiefs_no_huddle.csv')

#screen
#Whole league, EPA, group by screen
screen_df = df.groupby(['screen'])
correlations_screen = screen_df.corr()['epa'][:]
print(correlations_screen)
correlations_screen.to_csv('correlations_screen.csv')

#Chiefs only, EPA, group by screen
chiefs_df = df.loc[df['posteam'] == 'KC']
chiefs_screen_df = chiefs_df.groupby(['screen'])
correlations_chiefs_screen = chiefs_screen_df.corr()['epa'][:]
print(correlations_chiefs_screen)
correlations_chiefs_screen.to_csv('correlations_chiefs_screen.csv')

#Whole league, group by screen, counts
screen_df_counts = df.groupby(['screen'])["screen"].count().reset_index(name="count")
print(screen_df_counts)
screen_df_counts.to_csv('screen_df_counts.csv')

#Chiefs only, group by screen, counts
chiefs_df = df.loc[df['posteam'] == 'KC']
chiefs_screen_df_counts = chiefs_df.groupby(['screen'])["screen"].count().reset_index(name="count")
print(chiefs_screen_df_counts)
chiefs_screen_df_counts.to_csv('chiefs_screen_df_counts.csv')

#Left join to combine correlations and counts
correlations_chiefs_screen_2 = pd.read_csv('correlations_chiefs_screen_2.csv', low_memory=False)
correlations_screen_2 = pd.read_csv('correlations_screen_2.csv', low_memory=False)

league_screen = pd.merge(correlations_screen_2, screen_df_counts, on='screen',how='left')
league_screen.to_csv('league_screen.csv')
chiefs_screen = pd.merge(correlations_chiefs_screen_2, chiefs_screen_df_counts, on='screen',how='left')
chiefs_screen.to_csv('chiefs_screen.csv')

#play_action
#Whole league, EPA, group by play_action
play_action_df = df.groupby(['play_action'])
correlations_play_action = play_action_df.corr()['epa'][:]
print(correlations_play_action)
correlations_play_action.to_csv('correlations_play_action.csv')

#Chiefs only, EPA, group by play_action
chiefs_df = df.loc[df['posteam'] == 'KC']
chiefs_play_action_df = chiefs_df.groupby(['play_action'])
correlations_chiefs_play_action = chiefs_play_action_df.corr()['epa'][:]
print(correlations_chiefs_play_action)
correlations_chiefs_play_action.to_csv('correlations_chiefs_play_action.csv')

#Whole league, group by play_action, counts
play_action_df_counts = df.groupby(['play_action'])["play_action"].count().reset_index(name="count")
print(play_action_df_counts)
play_action_df_counts.to_csv('play_action_df_counts.csv')

#Chiefs only, group by play_action, counts
chiefs_df = df.loc[df['posteam'] == 'KC']
chiefs_play_action_df_counts = chiefs_df.groupby(['play_action'])["play_action"].count().reset_index(name="count")
print(chiefs_play_action_df_counts)
chiefs_play_action_df_counts.to_csv('chiefs_play_action_df_counts.csv')

#Left join to combine correlations and counts
correlations_chiefs_play_action_2 = pd.read_csv('correlations_chiefs_play_action_2.csv', low_memory=False)
correlations_play_action_2 = pd.read_csv('correlations_play_action_2.csv', low_memory=False)

league_play_action = pd.merge(correlations_play_action_2, play_action_df_counts, on='play_action',how='left')
league_play_action.to_csv('league_play_action.csv')
chiefs_play_action = pd.merge(correlations_chiefs_play_action_2, chiefs_play_action_df_counts, on='play_action',how='left')
chiefs_play_action.to_csv('chiefs_play_action.csv')

#rpo
#Whole league, EPA, group by rpo
rpo_df = df.groupby(['rpo'])
correlations_rpo = rpo_df.corr()['epa'][:]
print(correlations_rpo)
correlations_rpo.to_csv('correlations_rpo.csv')

#Chiefs only, EPA, group by rpo
chiefs_df = df.loc[df['posteam'] == 'KC']
chiefs_rpo_df = chiefs_df.groupby(['rpo'])
correlations_chiefs_rpo = chiefs_rpo_df.corr()['epa'][:]
print(correlations_chiefs_rpo)
correlations_chiefs_rpo.to_csv('correlations_chiefs_rpo.csv')

#Whole league, group by rpo, counts
rpo_df_counts = df.groupby(['rpo'])["rpo"].count().reset_index(name="count")
print(rpo_df_counts)
rpo_df_counts.to_csv('rpo_df_counts.csv')

#Chiefs only, group by rpo, counts
chiefs_df = df.loc[df['posteam'] == 'KC']
chiefs_rpo_df_counts = chiefs_df.groupby(['rpo'])["rpo"].count().reset_index(name="count")
print(chiefs_rpo_df_counts)
chiefs_rpo_df_counts.to_csv('chiefs_rpo_df_counts.csv')

#Left join to combine correlations and counts
correlations_chiefs_rpo_2 = pd.read_csv('correlations_chiefs_rpo_2.csv', low_memory=False)
correlations_rpo_2 = pd.read_csv('correlations_rpo_2.csv', low_memory=False)

league_rpo = pd.merge(correlations_rpo_2, rpo_df_counts, on='rpo',how='left')
league_rpo.to_csv('league_rpo.csv')
chiefs_rpo = pd.merge(correlations_chiefs_rpo_2, chiefs_rpo_df_counts, on='rpo',how='left')
chiefs_rpo.to_csv('chiefs_rpo.csv')

#rpo
#Whole league, EPA, group by rpo
rpo_df = df.groupby(['rpo'])
correlations_rpo = rpo_df.corr()['epa'][:]
print(correlations_rpo)
correlations_rpo.to_csv('correlations_rpo.csv')

#coverage scheme (filter pass plays)

#Chiefs only, EPA, grouped by coverage_scheme
chiefs_pass_df = df.loc[(df['posteam'] == 'KC') & (df['pass'] == 1)]
chiefs_coverage_scheme_df = chiefs_pass_df.groupby(['coverage_scheme'])
correlations_chiefs_coverage_scheme = chiefs_coverage_scheme_df.corr()['epa'][:]
print(correlations_chiefs_coverage_scheme)
correlations_chiefs_coverage_scheme.to_csv('correlations_chiefs_coverage_scheme.csv')

#Whole league, EPA, grouped by coverage_scheme
pass_df = df.loc[df['pass'] == 1]
coverage_scheme_df = pass_df.groupby(['coverage_scheme'])
correlations_coverage_scheme = coverage_scheme_df.corr()['epa'][:]
print(correlations_coverage_scheme)
correlations_coverage_scheme.to_csv('correlations_coverage_scheme.csv')

#Whole league, group by coverage_scheme, counts
pass_df = df.loc[df['pass'] == 1]
coverage_scheme_df_counts = pass_df.groupby(['coverage_scheme'])["coverage_scheme"].count().reset_index(name="count")
print(coverage_scheme_df_counts)
coverage_scheme_df_counts.to_csv('coverage_scheme_df_counts.csv')

#Chiefs only, group by coverage_scheme, 
chiefs_pass_df = df.loc[(df['posteam'] == 'KC') & (df['pass'] == 1)]
chiefs_coverage_scheme_df_counts = chiefs_pass_df.groupby(['coverage_scheme'])["coverage_scheme"].count().reset_index(name="count")
print(chiefs_coverage_scheme_df_counts)
chiefs_coverage_scheme_df_counts.to_csv('chiefs_coverage_scheme_df_counts.csv')

#Left joining to combine correlations and counts
correlations_chiefs_coverage_scheme_2 = pd.read_csv('correlations_chiefs_coverage_scheme_2.csv', low_memory=False)
correlations_coverage_scheme_2 = pd.read_csv('correlations_coverage_scheme_2.csv', low_memory=False)

league_coverage_scheme = pd.merge(correlations_coverage_scheme_2, coverage_scheme_df_counts, on='coverage_scheme',how='left')
league_coverage_scheme.to_csv('league_coverage_scheme.csv')
chiefs_coverage_scheme = pd.merge(correlations_chiefs_coverage_scheme_2, chiefs_coverage_scheme_df_counts, on='coverage_scheme',how='left')
chiefs_coverage_scheme.to_csv('chiefs_coverage_scheme_.csv')

#mofo_coverage_played(filter pass plays)

#Chiefs only, EPA, grouped by mofo_coverage_played
chiefs_pass_df = df.loc[(df['posteam'] == 'KC') & (df['pass'] == 1)]
chiefs_mofo_coverage_played_df = chiefs_pass_df.groupby(['mofo_coverage_played'])
correlations_chiefs_mofo_coverage_played = chiefs_mofo_coverage_played_df.corr()['epa'][:]
print(correlations_chiefs_mofo_coverage_played)
correlations_chiefs_mofo_coverage_played.to_csv('correlations_chiefs_mofo_coverage_played.csv')

#Whole league, EPA, grouped by mofo_coverage_played
pass_df = df.loc[df['pass'] == 1]
mofo_coverage_played_df = pass_df.groupby(['mofo_coverage_played'])
correlations_mofo_coverage_played = mofo_coverage_played_df.corr()['epa'][:]
print(correlations_mofo_coverage_played)
correlations_mofo_coverage_played.to_csv('correlations_mofo_coverage_played.csv')

#Whole league, group by mofo_coverage_played, counts
pass_df = df.loc[df['pass'] == 1]
mofo_coverage_played_df_counts = pass_df.groupby(['mofo_coverage_played'])["mofo_coverage_played"].count().reset_index(name="count")
print(mofo_coverage_played_df_counts)
mofo_coverage_played_df_counts.to_csv('mofo_coverage_played_df_counts.csv')

#Chiefs only, group by mofo_coverage_played, 
chiefs_pass_df = df.loc[(df['posteam'] == 'KC') & (df['pass'] == 1)]
chiefs_mofo_coverage_played_df_counts = chiefs_pass_df.groupby(['mofo_coverage_played'])["mofo_coverage_played"].count().reset_index(name="count")
print(chiefs_mofo_coverage_played_df_counts)
chiefs_mofo_coverage_played_df_counts.to_csv('chiefs_mofo_coverage_played_df_counts.csv')

#Left joining to combine correlations and counts
correlations_chiefs_mofo_coverage_played_2 = pd.read_csv('correlations_chiefs_mofo_coverage_played_2.csv', low_memory=False)
correlations_mofo_coverage_played_2 = pd.read_csv('correlations_mofo_coverage_played_2.csv', low_memory=False)

league_mofo_coverage_played = pd.merge(correlations_mofo_coverage_played_2, mofo_coverage_played_df_counts, on='mofo_coverage_played',how='left')
league_mofo_coverage_played.to_csv('league_mofo_coverage_played.csv')
chiefs_mofo_coverage_played = pd.merge(correlations_chiefs_mofo_coverage_played_2, chiefs_mofo_coverage_played_df_counts, on='mofo_coverage_played',how='left')
chiefs_mofo_coverage_played.to_csv('chiefs_mofo_coverage_played_.csv')


#Defense_personnel
#Chiefs only, EPA, grouped by defense personnel
chiefs_df_3 = df_3.loc[df_3['posteam'] == 'KC']
chiefs_defense_personnel_df = chiefs_df_3.groupby(['defense_personnel'])
correlations_chiefs_defense_personnel = chiefs_defense_personnel_df.corr()['epa'][:]
print(correlations_chiefs_defense_personnel)
correlations_chiefs_defense_personnel.to_csv('correlations_chiefs_defense_personnel.csv')

#Whole league, EPA, grouped by defense personnel
defense_personnel_df = df_3.groupby(['defense_personnel'])
correlations_defense_personnel = defense_personnel_df.corr()['epa'][:]
print(correlations_defense_personnel)
correlations_defense_personnel.to_csv('correlations_defense_personnel.csv')

#Whole league, group by defense personnel, counts
defense_personnel_df_counts = df_3.groupby(['defense_personnel'])["defense_personnel"].count().reset_index(name="count")
print(defense_personnel_df_counts)
defense_personnel_df_counts.to_csv('defense_personnel_df_counts.csv')

#Chiefs only, group by defense personnel, counts
chiefs_df_3 = df_3.loc[df_3['posteam'] == 'KC']
chiefs_defense_personnel_df_counts = chiefs_df_3.groupby(['defense_personnel'])["defense_personnel"].count().reset_index(name="count")
print(chiefs_defense_personnel_df_counts)
chiefs_defense_personnel_df_counts.to_csv('chiefs_defense_personnel_df_counts.csv')

#Left joining to combine correlations and counts
correlations_chiefs_defense_personnel_2 = pd.read_csv('correlations_chiefs_defense_personnel_2.csv', low_memory=False)
correlations_defense_personnel_2 = pd.read_csv('correlations_defense_personnel_2.csv', low_memory=False)

league_defense_personnel = pd.merge(correlations_defense_personnel_2, defense_personnel_df_counts, on='defense_personnel',how='left')
league_defense_personnel.to_csv('league_defense_personnel.csv')
chiefs_defense_personnel = pd.merge(correlations_chiefs_defense_personnel_2, chiefs_defense_personnel_df_counts, on='defense_personnel',how='left')
chiefs_defense_personnel.to_csv('chiefs_defense_personnel_.csv')



#pass_direction (filter pass plays)

#Chiefs only, EPA, grouped by pass_direction
chiefs_pass_df = df.loc[(df['posteam'] == 'KC') & (df['pass'] == 1)]
chiefs_pass_direction_df = chiefs_pass_df.groupby(['pass_direction'])
correlations_chiefs_pass_direction = chiefs_pass_direction_df.corr()['epa'][:]
print(correlations_chiefs_pass_direction)
correlations_chiefs_pass_direction.to_csv('correlations_chiefs_pass_direction.csv')

#Whole league, EPA, grouped by pass_direction
pass_df = df.loc[df['pass'] == 1]
pass_direction_df = pass_df.groupby(['pass_direction'])
correlations_pass_direction = pass_direction_df.corr()['epa'][:]
print(correlations_pass_direction)
correlations_pass_direction.to_csv('correlations_pass_direction.csv')

#Whole league, group by pass_direction, counts
pass_df = df.loc[df['pass'] == 1]
pass_direction_df_counts = pass_df.groupby(['pass_direction'])["pass_direction"].count().reset_index(name="count")
print(pass_direction_df_counts)
pass_direction_df_counts.to_csv('pass_direction_df_counts.csv')

#Chiefs only, group by pass_direction, 
chiefs_pass_df = df.loc[(df['posteam'] == 'KC') & (df['pass'] == 1)]
chiefs_pass_direction_df_counts = chiefs_pass_df.groupby(['pass_direction'])["pass_direction"].count().reset_index(name="count")
print(chiefs_pass_direction_df_counts)
chiefs_pass_direction_df_counts.to_csv('chiefs_pass_direction_df_counts.csv')

#Left joining to combine correlations and counts
correlations_chiefs_pass_direction_2 = pd.read_csv('correlations_chiefs_pass_direction_2.csv', low_memory=False)
correlations_pass_direction_2 = pd.read_csv('correlations_pass_direction_2.csv', low_memory=False)

league_pass_direction = pd.merge(correlations_pass_direction_2, pass_direction_df_counts, on='pass_direction',how='left')
league_pass_direction.to_csv('league_pass_direction.csv')
chiefs_pass_direction = pd.merge(correlations_chiefs_pass_direction_2, chiefs_pass_direction_df_counts, on='pass_direction',how='left')
chiefs_pass_direction.to_csv('chiefs_pass_direction_.csv')


#run_direction (filter run plays)

#Chiefs only, EPA, grouped by run_direction
chiefs_run_df = df.loc[(df['posteam'] == 'KC') & (df['rush'] == 1)]
chiefs_run_direction_df = chiefs_run_df.groupby(['run_direction'])
correlations_chiefs_run_direction = chiefs_run_direction_df.corr()['epa'][:]
print(correlations_chiefs_run_direction)
correlations_chiefs_run_direction.to_csv('correlations_chiefs_run_direction.csv')

#Whole league, EPA, grouped by run_direction
run_df = df.loc[df['rush'] == 1]
run_direction_df = run_df.groupby(['run_direction'])
correlations_run_direction = run_direction_df.corr()['epa'][:]
print(correlations_run_direction)
correlations_run_direction.to_csv('correlations_run_direction.csv')

#Whole league, group by run_direction, counts
run_df = df.loc[df['rush'] == 1]
run_direction_df_counts = run_df.groupby(['run_direction'])["run_direction"].count().reset_index(name="count")
print(run_direction_df_counts)
run_direction_df_counts.to_csv('run_direction_df_counts.csv')

#Chiefs only, group by run_direction, 
chiefs_run_df = df.loc[(df['posteam'] == 'KC') & (df['rush'] == 1)]
chiefs_run_direction_df_counts = chiefs_run_df.groupby(['run_direction'])["run_direction"].count().reset_index(name="count")
print(chiefs_run_direction_df_counts)
chiefs_run_direction_df_counts.to_csv('chiefs_run_direction_df_counts.csv')

#Left joining to combine correlations and counts
correlations_chiefs_run_direction_2 = pd.read_csv('correlations_chiefs_run_direction_2.csv', low_memory=False)
correlations_run_direction_2 = pd.read_csv('correlations_run_direction_2.csv', low_memory=False)

league_run_direction = pd.merge(correlations_run_direction_2, run_direction_df_counts, on='run_direction',how='left')
league_run_direction.to_csv('league_run_direction.csv')
chiefs_run_direction = pd.merge(correlations_chiefs_run_direction_2, chiefs_run_direction_df_counts, on='run_direction',how='left')
chiefs_run_direction.to_csv('chiefs_run_direction_.csv')
'''

