import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')


# The Indian Premier League (IPL) is a professional T20 cricket league in India, featuring franchises representing cities. This project explores IPL 2022 match-level data to derive meaningful insights and understand match outcomes, player performances, and team dynamics.

# These are some of the important columns that we'll focus on for meaningful insights in this project.

# column names: Variable Type

# date : string
# venue : string
# stage : string
# team1 : string
# team2 : string
# toss_winner : string
# toss_decision : string
# first_ings_score : integer
# second_ings_score : integer
# match_winner : string
# won_by : string
# margin : integer
# player_of_the_match : string
# top_scorer : string
# highscore : integer
# best_bowling : string
# best_bowling_fgure : string
# gure : string

df = pd.read_csv('IPL.csv')
df.head()
df['match_winner'].value_counts()

match_wins = df['match_winner'].value_counts()
plt.figure(figsize=(14,6))
sns.barplot(x = match_wins.index, y= match_wins.values, palette='rainbow' )
plt.title('Most matched wins by each team')

count_toss = df[df['toss_winner'] == df['match_winner']] ['match_id'].count()
perent = (count_toss * 100)/df.shape[0]
perent.round(2)
sns.barplot(x= df['toss_winner'], y=df['match_id'])

player_of_match = df['player_of_the_match'].value_counts().head(5)
plt.figure(figsize=(10,8))
sns.barplot(y= player_of_match.index, x= player_of_match.values, palette='rainbow')
plt.title('Most player of the match')
plt.xlabel('total wins')
plt.ylabel('player name')

max_score = df.groupby('top_scorer')['highscore'].sum().sort_values(ascending=False).head(4)
max_score.plot(kind='barh')
plt.title("most runs across all batting by the players")
plt.xlabel('total runs')
plt.ylabel('Player name')



