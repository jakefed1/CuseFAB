library(nflfastR)
library(tidyverse)
scheme_data <- read_csv("scheme_data.csv")
pbp_data <- nflfastR::load_pbp(2021)

# Edit team names for later merging
scheme_data <- scheme_data %>%
  mutate(posteam = case_when(
    offense %in% c("ATL", "BUF", "CAR", "CHI", "CIN", "DAL", "DEN", "DET", "GB", "IND", "JAX", "KC", "LA", "LAC", "LV", "MIA", "MIN", "NE", "NO", "NYG", "NYJ", "PHI", "PIT", "SEA", "SF", "TB", "TEN", "WAS") ~ offense,
    offense == "ARZ" ~ "ARI",
    offense == "BLT"~ "BAL",
    offense == "CLV" ~ "CLE",
    offense == "HST" ~ "HOU",
    offense == "OAK" ~ "LV",
    offense == "SD" ~ "LAC",
    offense == "SL" ~ "LA"
  ),
  defteam = case_when(
    defense %in% c("ATL", "BUF", "CAR", "CHI", "CIN", "DAL", "DEN", "DET", "GB", "IND", "JAX", "KC", "LA", "LAC", "LV", "MIA", "MIN", "NE", "NO", "NYG", "NYJ", "PHI", "PIT", "SEA", "SF", "TB", "TEN", "WAS") ~ defense,
    defense == "ARZ" ~ "ARI",
    defense == "BLT"~ "BAL",
    defense == "CLV" ~ "CLE",
    defense == "HST" ~ "HOU",
    defense == "OAK" ~ "LV",
    defense == "SD" ~ "LAC",
    defense == "SL" ~ "LA"
  )) %>%
  rename(yardline_100 = yards_to_go, ydstogo = distance, qtr = quarter, quarter_seconds_remaining = seconds_left_in_quarter) %>%
  mutate(game_seconds_remaining = quarter_seconds_remaining+(4-qtr)*900,
         week = case_when(
           week < 19 ~ week,
           week == 28 ~ 19,
           week == 29 ~ 20,
           week == 30 ~ 21,
           week == 32 ~ 22
         )) %>%
  filter(down > 0, rps %in% c("R", "P")) %>%
  group_by(season, week, posteam, defteam, qtr, down, ydstogo, yardline_100) %>%
  arrange(desc(game_seconds_remaining)) %>%
  mutate(dupe_number = 1:n()) %>%
  ungroup()

pbp_data <- pbp_data %>%
  filter(down > 0) %>%
  ungroup() %>%
  select(season, week, posteam, defteam, yardline_100, quarter_seconds_remaining:game_seconds_remaining, qtr:goal_to_go, ydstogo, yards_gained, shotgun:run_gap, ep, epa, wp, wpa, qb_hit:sack, passer, rusher, receiver, pass, rush) %>%
  group_by(season, week, posteam, defteam, qtr, down, ydstogo, yardline_100) %>%
  arrange(desc(game_seconds_remaining)) %>%
  mutate(dupe_number = 1:n()) %>%
  ungroup()

# Use posteam, defteam, and other play information to merge scheme_data with pbp_data
merged_data <- left_join(scheme_data, pbp_data, by = c("season", "week", "posteam", "defteam", "qtr", "down", "ydstogo", "yardline_100", "dupe_number")) %>%
  filter(down > 0, rps %in% c("R", "P"))

merged_data <- merged_data %>%
  mutate(score_diff = off_score_before - def_score_before)


KC_off <- merged_data %>%
  filter(posteam == "KC") %>%
  filter(rps %in% c("R", "P"))

KC_off <- KC_off %>%
  filter(offense_personnel %in% c("2-0-1-2", "2-1-1-1", "3-0-1-1", "1-0-1-3")) %>%
  filter(defense_personnel %in% c("1/4/06", "2/3/06", "2/4/05", "3/2/06", "3/3/05", "3/4/04", "4/1/06", "4/2/05", "4/3/04"))

KC_off %>%
  filter(yardline_100 <= 90 & yardline_100 >= 60) %>%
  filter(offense_personnel == "3-0-1-1") %>%
  filter(down == 1 & abs(score_diff) < 8) %>%
  summarize(down_yards = mean(ydstogo), mean_rush = mean(rush), mean_epa = mean(epa), count = n(), target_depth = mean(target_depth), play_action = mean(play_action), time_throw = mean(time_to_throw), time_pressure = mean(time_to_pressure), yac = mean(yards_after_catch, na.rm = TRUE), mean_yards_to_go = mean(yardline_100), mean_down = mean(down), m_screen = mean(screen), ypp = mean(yards_gained)) %>%
  arrange(desc(mean_epa)) %>%
  ungroup()

KC_1013_goalline <- KC_off %>%
  filter(offense_personnel == "1-0-1-3") %>%
  filter(yardline_100 <= 5) %>% 
  #summarize(down_yards = mean(ydstogo), mean_rush = mean(rush), mean_epa = mean(epa), count = n(), play_action = mean(play_action), time_throw = mean(time_to_throw), time_pressure = mean(time_to_pressure), mean_yards_to_go = mean(yardline_100), mean_down = mean(down), m_screen = mean(screen), ypp = mean(yards_gained)) %>%
  #arrange(desc(mean_epa)) %>%
  ungroup()
view(KC_1013_goalline)
#LMFAO THEY SCORED ALL 7 INSTANCES
#So let's look at what defenses did against these, and just do what they didn't do

KC_1013_goalline_spec <- KC_1013_goalline %>% 
  select(week, game_seconds_remaining.x, shotgun.x, play_action, pass_direction, screen,
         rpo, run_position, intended_run_position, run_direction,
         defense_personnel, blitz, num_pass_rush_players, coverage_scheme,
         mofo_coverage_played, box_players)
view(KC_1013_goalline_spec)

#Lol the defense never stunted so maybe we should stunt

KC_under1 <- KC_off %>% 
  filter(game_seconds_remaining.x < 60) %>% 
  filter(game_seconds_remaining.x > 0) %>% 
  filter(yardline_100 > 50) %>% 
  filter(score_diff < 1) %>% 
  filter(score_diff > -9)
view(KC_under1)

#Not only did the Chiefs never run this personnel, but they never ran an empty backfield, ever, according to my teammates.
#So, let's look at other teams in this personnel and in 5-0-0-0 and in 3-0-0-2 in this situation

empty <- merged_data %>% 
  filter(game_seconds_remaining.x < 60) %>% 
  filter(game_seconds_remaining.x > 10) %>%
  filter(offense_personnel %in% c("4-0-0-1", "5-0-0-0", "3-0-0-2")) %>% 
  filter(yardline_100 > 50) %>% 
  filter(score_diff < 1)
  #summarize(down_yards = mean(ydstogo), mean_rush = mean(rush), mean_epa = mean(epa), count = n(), target_depth = mean(target_depth), play_action = mean(play_action), time_throw = mean(time_to_throw), time_pressure = mean(time_to_pressure), yac = mean(yards_after_catch, na.rm = TRUE), mean_yards_to_go = mean(yardline_100), mean_down = mean(down), m_screen = mean(screen), ypp = mean(yards_gained))
view(empty)

empty_2 <- merged_data %>% 
  filter(game_seconds_remaining.x < 1860) %>% 
  filter(game_seconds_remaining.x > 1810) %>%
  filter(offense_personnel %in% c("4-0-0-1", "5-0-0-0", "3-0-0-2")) %>% 
  filter(yardline_100 > 50)
#summarize(down_yards = mean(ydstogo), mean_rush = mean(rush), mean_epa = mean(epa), count = n(), target_depth = mean(target_depth), play_action = mean(play_action), time_throw = mean(time_to_throw), time_pressure = mean(time_to_pressure), yac = mean(yards_after_catch, na.rm = TRUE), mean_yards_to_go = mean(yardline_100), mean_down = mean(down), m_screen = mean(screen), ypp = mean(yards_gained))
view(empty_2)

empty_full <- rbind(empty, empty_2)

view(summary(empty_full))

empty_full %>% 
  group_by(defense_personnel) %>% 
  summarize(down_yards = mean(ydstogo), mean_rush = mean(rush), mean_epa = mean(epa), count = n(), target_depth = mean(target_depth), play_action = mean(play_action), time_throw = mean(time_to_throw), time_pressure = mean(time_to_pressure), yac = mean(yards_after_catch, na.rm = TRUE), mean_yards_to_go = mean(yardline_100), mean_down = mean(down), m_screen = mean(screen), ypp = mean(yards_gained)) %>% 
  ungroup()

#With 6 DBs there is a negative average epa (-0.032)

empty_full %>% 
  filter(defense_personnel %in% c("1/4/06",'2/3/06', '3/2/06', '4/1/06')) %>% 
  group_by(coverage_scheme) %>% 
  summarize(down_yards = mean(ydstogo), mean_rush = mean(rush), mean_epa = mean(epa), count = n(), target_depth = mean(target_depth), play_action = mean(play_action), time_throw = mean(time_to_throw), time_pressure = mean(time_to_pressure), yac = mean(yards_after_catch, na.rm = TRUE), mean_yards_to_go = mean(yardline_100), mean_down = mean(down), m_screen = mean(screen), ypp = mean(yards_gained)) %>% 
  ungroup()

empty_full %>% 
  filter(defense_personnel %in% c("1/4/06",'2/3/06', '3/2/06', '4/1/06')) %>% 
  group_by(mofo_coverage_played) %>% 
  summarize(down_yards = mean(ydstogo), mean_rush = mean(rush), mean_epa = mean(epa), count = n(), target_depth = mean(target_depth), play_action = mean(play_action), time_throw = mean(time_to_throw), time_pressure = mean(time_to_pressure), yac = mean(yards_after_catch, na.rm = TRUE), mean_yards_to_go = mean(yardline_100), mean_down = mean(down), m_screen = mean(screen), ypp = mean(yards_gained)) %>% 
  ungroup()

empty_full %>% 
  filter(defense_personnel %in% c("1/4/06",'2/3/06', '3/2/06', '4/1/06')) %>% 
  group_by(blitz, mofo_coverage_played) %>% 
  summarize(down_yards = mean(ydstogo), mean_rush = mean(rush), mean_epa = mean(epa), count = n(), target_depth = mean(target_depth), play_action = mean(play_action), time_throw = mean(time_to_throw), time_pressure = mean(time_to_pressure), yac = mean(yards_after_catch, na.rm = TRUE), mean_yards_to_go = mean(yardline_100), mean_down = mean(down), m_screen = mean(screen), ypp = mean(yards_gained)) %>% 
  ungroup()


empty_anytime <- merged_data %>% 
  filter(offense_personnel %in% c("4-0-0-1", "5-0-0-0", "3-0-0-2")) %>% 
  filter(yardline_100 > 50) %>% 
  filter(defense_personnel %in% c("1/4/06",'2/3/06', '3/2/06', '4/1/06')) %>% 
  filter(rps == 'P')

empty_saints <- empty_anytime %>% 
  filter(defteam == "NO")

empty_saints %>% 
  group_by(defense_personnel) %>% 
  summarize(down_yards = mean(ydstogo), mean_rush = mean(rush), mean_epa = mean(epa), count = n(), target_depth = mean(target_depth), play_action = mean(play_action), time_throw = mean(time_to_throw), time_pressure = mean(time_to_pressure), yac = mean(yards_after_catch, na.rm = TRUE), mean_yards_to_go = mean(yardline_100), mean_down = mean(down), m_screen = mean(screen), ypp = mean(yards_gained)) %>% 
  ungroup()

empty_saints %>% 
  group_by(coverage_scheme) %>% 
  summarize(mean_epa = mean(epa), count = n()) %>% 
  ungroup()

empty_rams <- empty_anytime %>% 
  filter(defteam == "LA")

empty_rams %>% 
  group_by(defense_personnel) %>% 
  summarize(mean_epa = mean(epa), count = n()) %>% 
  ungroup()

empty_rams %>% 
  filter(defense_personnel != "3/2/06") %>% 
  group_by(coverage_scheme) %>% 
  summarize(mean_epa = mean(epa), count = n()) %>%
  ungroup()

chiefs_fourth <-
  merged_data %>% 
  filter(posteam == 'KC') %>% 
  filter(down == 3 | down == 4) %>%
  filter(ydstogo < 4) %>% 
  filter(offense_personnel == "2-0-1-2")
view(chiefs_fourth)

chiefs_fourth %>% 
  group_by(defense_personnel) %>% 
  summarize(mean_epa = mean(epa), count = n()) %>% 
  ungroup()

rams_fourth <-
  merged_data %>% 
  filter(defteam == 'LA') %>% 
  filter(down == 3 | down == 4) %>%
  filter(ydstogo < 4) %>% 
  filter(offense_personnel == "2-0-1-2")
view(rams_fourth)

rams_fourth %>% 
  group_by(defense_personnel) %>% 
  summarize(mean_epa = mean(epa), count = n()) %>% 
  ungroup()

rams_fourth %>% 
  filter(defense_personnel == "4/2/05") %>% 
  view()

saints_fourth <-
  merged_data %>% 
  filter(defteam == 'NO') %>% 
  filter(down == 3 | down == 4) %>%
  filter(ydstogo < 4) %>% 
  filter(offense_personnel == "2-0-1-2")
view(saints_fourth)

saints_fourth %>% 
  group_by(defense_personnel) %>% 
  summarize(mean_epa = mean(epa), count = n()) %>% 
  ungroup()

saints_fourth %>% 
  filter(defense_personnel == "4/2/05") %>% 
  view()
  
write_csv(merged_data, file = "merged_data.csv")

merged_data
