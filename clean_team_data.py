import pandas as pd
import os

"""Deprecated. Use not recommended. Functionality moved to new clean_team_data file"""

def team_stats_and_rank(file):
    df = pd.read_csv(file, index_col=0)
    df.fillna(0, inplace=True)
    df.drop(0, axis=0, inplace=True)

    for x in range(3,6):
        df.rename(columns={df.columns[x]:"Tot Yds & TO"}, inplace=True)

    for x in range(8,15):
        df.rename(columns={df.columns[x]:"Passing"}, inplace=True)

    for x in range(15, 20):
        df.rename(columns={df.columns[x]: "Rushing"}, inplace=True)

    for x in range(20,23):
        df.rename(columns={df.columns[x]:"Penalties"}, inplace=True)

    for x in range(26, 31):
        df.rename(columns={df.columns[x]: "Average Drive"}, inplace=True)
    # Use os.rename to overwrite the original file to prevent duplicate data
    df.to_csv(os.path.dirname(file) + "/0.csv")
    os.rename(os.path.dirname(file) + "/0.csv", os.path.dirname(file) + "/stats_and_rank.csv")

def schedule_and_results(file):
    df = pd.read_csv(file, index_col=0)
    df.fillna(0, inplace=True)
    df.drop(0, axis=0, inplace=True)

    for x in range(10,12):
        df.rename(columns={df.columns[x]:"Score"}, inplace=True)

    for x in range(12,17):
        df.rename(columns={df.columns[x]:"Offense"}, inplace=True)

    for x in range(17,22):
        df.rename(columns={df.columns[x]:"Defense"}, inplace=True)

    for x in range(22,25):
        df.rename(columns={df.columns[x]:"Expected Points"}, inplace=True)
    # Use os.rename to overwrite the original file to prevent duplicate data
    df.to_csv(os.path.dirname(file) + "/1.csv")
    os.rename(os.path.dirname(file) + "/1.csv", os.path.dirname(file) + "/schedule_and_results.csv")


def team_conversions(file):
    df = pd.read_csv(file, index_col=0)
    df.fillna(0, inplace=True)
    df.drop(0, axis=0, inplace=True)

    for x in range(1, 7):
        df.rename(columns={df.columns[x]: "Downs"}, inplace=True)

    for x in range(7, 10):
        df.rename(columns={df.columns[x]: "Red Zone"}, inplace=True)
    # Use os.rename to overwrite the original file to prevent duplicate data
    df.to_csv(os.path.dirname(file) + "/2.csv")
    os.rename(os.path.dirname(file) + "/2.csv", os.path.dirname(file) + "/team_conversions.csv")


def passing(file):
    df = pd.read_csv(file, index_col=0)
    df.fillna(0, inplace=True)
    df.columns = df.iloc[0]
    df.drop(0, axis=0, inplace=True)

    df.to_csv(os.path.dirname(file) + "/3.csv")
    os.rename(os.path.dirname(file) + "/3.csv", os.path.dirname(file) + "/passing.csv")


def rushing_receiving(file):
    df = pd.read_csv(file, index_col=0)
    df.fillna(0, inplace=True)
    df.drop(0, axis=0, inplace=True)

    for x in range(4, 6):
        df.rename(columns={df.columns[x]: "Games"}, inplace=True)

    for x in range(6, 13):
        df.rename(columns={df.columns[x]: "Rushing"}, inplace=True)

    for x in range(13, 23):
        df.rename(columns={df.columns[x]: "Receiving"}, inplace=True)

    for x in range(23, 26):
        df.rename(columns={df.columns[x]: "Total Yds"}, inplace=True)

    df.to_csv(os.path.dirname(file) + "/4.csv")
    os.rename(os.path.dirname(file) + "/4.csv", os.path.dirname(file) + "/rushing_and_receiving.csv")

def kick_punt_return(file):
    df = pd.read_csv(file, index_col=0)
    df.fillna(0, inplace=True)
    df.drop(0, axis=0, inplace=True)

    for x in range(4, 6):
        df.rename(columns={df.columns[x]: "Games"}, inplace=True)

    for x in range(6, 11):
        df.rename(columns={df.columns[x]: "Punt Returns"}, inplace=True)

    for x in range(11, 16):
        df.rename(columns={df.columns[x]: "Kick Returns"}, inplace=True)

    df.to_csv(os.path.dirname(file) + "/5.csv")
    os.rename(os.path.dirname(file) + "/5.csv", os.path.dirname(file) + "/kick_punt_return.csv")


def kicking_punting(file):
    df = pd.read_csv(file, index_col=0)
    df.fillna(0, inplace=True)

    for x in range(4, 6):
        df.rename(columns={df.columns[x]: "Games"}, inplace=True)

    for x in range(6, 8):
        df.rename(columns={df.columns[x]: "0-19"}, inplace=True)

    for x in range(8, 10):
        df.rename(columns={df.columns[x]: "20-29"}, inplace=True)

    for x in range(10, 12):
        df.rename(columns={df.columns[x]: "30-39"}, inplace=True)

    for x in range(12, 14):
        df.rename(columns={df.columns[x]: "40-49"}, inplace=True)

    for x in range(14, 16):
        df.rename(columns={df.columns[x]: "50+"}, inplace=True)

    for x in range(16, 22):
        df.rename(columns={df.columns[x]: "Scoring"}, inplace=True)

    for x in range(22, 27):
        df.rename(columns={df.columns[x]: "Kickoffs"}, inplace=True)

    for x in range(27, 32):
        df.rename(columns={df.columns[x]: "Punting"}, inplace=True)

    df.to_csv(os.path.dirname(file) + "/6.csv")
    os.rename(os.path.dirname(file) + "/6.csv", os.path.dirname(file) + "/kicking_punting.csv")


def defense_and_fumbles(file):
    df = pd.read_csv(file, index_col=0)
    df.fillna(0, inplace=True)
    df.drop_duplicates(inplace=True)
    df.drop(0, axis=0, inplace=True)

    for x in range(4, 6):
        df.rename(columns={df.columns[x]: "Games"}, inplace=True)

    for x in range(6, 11):
        df.rename(columns={df.columns[x]: "Def Interceptions"}, inplace=True)

    for x in range(11, 15):
        df.rename(columns={df.columns[x]: "Fumbles"}, inplace=True)

    for x in range(17, 22):
        df.rename(columns={df.columns[x]: "Tackles"}, inplace=True)

    df.to_csv(os.path.dirname(file) + "/7.csv")
    os.rename(os.path.dirname(file) + "/7.csv", os.path.dirname(file) + "/defense_and_fumbles.csv")


def scoring_summary(file):
    df = pd.read_csv(file, index_col=0)
    df.fillna(0, inplace=True)
    df.columns = df.iloc[0]
    df.drop(0, axis=0, inplace=True)

    df.to_csv(os.path.dirname(file) + "/8.csv")
    os.rename(os.path.dirname(file) + "/8.csv", os.path.dirname(file) + "/scoring_summary.csv")


def touchdown_log(file):
    df = pd.read_csv(file, index_col=0)
    df.fillna(0, inplace=True)
    df.columns = df.iloc[0]
    df.drop_duplicates(inplace=True)
    df.drop(0,axis=0, inplace=True)

    df.to_csv(os.path.dirname(file) + "/9.csv")
    os.rename(os.path.dirname(file) + "/9.csv", os.path.dirname(file) + "/touchdown_log.csv")


def opponent_touchdown_log(file):
    df = pd.read_csv(file, index_col=0)
    df.fillna(0, inplace=True)
    df.columns = df.iloc[0]
    df.drop_duplicates(inplace=True)
    df.drop(0, axis=0, inplace=True)

    df.to_csv(os.path.dirname(file) + "/10.csv")
    os.rename(os.path.dirname(file) + "/10.csv", os.path.dirname(file) + "/opponent_touchdown_log.csv")
