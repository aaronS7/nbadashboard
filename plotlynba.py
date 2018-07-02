import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import glob
import pandas as pd
import plotly.graph_objs as go
import os

app = dash.Dash(__name__)
server = app.server
# Handles Season dropdown that the other dropdowns depend on
def multiDrop():

    files = glob.glob("regularSeason/csv/*.csv")
    files.sort()
    print(os.listdir())
    print()
    print(files[50:])
    playerStats = files[50:]
    return html.Div([
        html.H3("NBA Seasons"),
        dcc.Dropdown(
        id="nbaDropdown",
        options =[
            # filename[22:] leaves the season year and fileName[18:] leaves full file name (not path)
            {"label": fileName[22:].replace(".csv",""), "value": fileName[18:]} for fileName in playerStats
        ],
        value = [playerStats[0][18:], playerStats[1][18:]],
        multi=True
    ),
    html.H3("NBA Player Stats"),
    dcc.Dropdown(
        id="nbaPlayerStats"
    ),
    html.H3("NBA Team Stats"),
    dcc.Dropdown(
        id="nbaTeamStats"
    ),
    html.H3("NBA MVP Stats"),
    dcc.Dropdown(
        id = "mvpStats"
    )])

app.layout = html.Div([
    multiDrop(),
    html.Br(),
    dcc.Graph(id="playerOut"),
    dcc.Graph(id="teamOut"),
    html.Br(),
    dcc.Graph(id="mvpOut")
])

# Callback for Team dropdown (second)
@app.callback(Output("nbaTeamStats", "options"),
              [Input("nbaDropdown", "value")])
def dropdownTeam_callback_options(season):
    df = pd.read_csv("team_regularSeason/csv/" + season[0])
    df = df.drop(["TeamName"], axis=1)
    return [{
        "label": val,
        "value": val
    } for val in df.columns.values]

# Callback to place value in team dropdown
@app.callback(Output("nbaTeamStats", "value"),
              [Input("nbaTeamStats", "options")])
def dropdownTeamStat_callback_value(season):
    return season[4]['value']

@app.callback(Output("teamOut", "figure"),
              [Input("nbaDropdown", "value"),
               Input("nbaTeamStats", "value")])
def teamStats_callback(season, option):
    dfList = {}
    for fileName in season:
        df = pd.read_csv("team_regularSeason/csv/" + fileName)
        dfList[fileName.replace(".csv", "")] = df.sort_values(option, ascending=False)
    return {
        "data": [go.Bar(x=df["TeamName"][:10], y=df[option][:10], name="Player's " + option + " " + year[4:]) for year, df in dfList.items()],
        "layout": go.Layout(title="NBA Seasons compared to" + " " + option)
    }

# Callback for player dropdown (first)
@app.callback(Output("nbaPlayerStats", "options"),
              [Input("nbaDropdown", "value")])
def dropdownStat_callback_options(season):
    df = pd.read_csv("regularSeason/csv/" + season[0])
    df = df.drop(["Name"], axis=1)
    return [{
        "label": val,
        "value": val
    } for val in df.columns.values]

@app.callback(Output("nbaPlayerStats", "value"),
              [Input("nbaPlayerStats", "options")])
def dropdownStat_callback_value(season):
    return season[4]['value']

@app.callback(Output("playerOut", "figure"),
              [Input("nbaDropdown", "value"),
               Input("nbaPlayerStats", "value")])
def playerStats_callback(season, option):
    dfList = {}
    for fileName in season:
        df = pd.read_csv("regularSeason/csv/" + fileName)
        dfList[fileName.replace(".csv", "")] = df.sort_values(option, ascending=False)
    return {
        "data": [go.Bar(x=df["Name"][:10], y=df[option][:10], name="Player's " + option + " " + year[4:]) for year, df in dfList.items()],
        "layout": go.Layout(title="NBA Seasons compared to" + " " + option)
    }


# Callback for mvp dropdown (third)
@app.callback(Output("mvpStats", "options"),
              [Input("nbaDropdown", "value")])
def mvpdropdown_callback_options(season):
    df = pd.read_csv("mvp.csv")
    df = df.set_index("Season")
    optionsdf = df.drop(["Player"], axis = 1)
    return [{
        "label": val,
        "value": val
    } for val in optionsdf.columns.values]


@app.callback(Output("mvpStats", "value"),
              [Input("mvpStats", "options")])
def mvpdropdown_callback_value(season):
    return season[2]['value']


@app.callback(Output("mvpOut", "figure"),
              [Input("nbaDropdown", "value"),
               Input("mvpStats", "value")])
def mvp_callback(seasons, option):
    df = pd.read_csv("mvp.csv")
    df = df.set_index("Season")
    dfList = []
    for season in seasons:
        if season[4:].replace(".csv","") == "2017-18":
            continue
        dfList.append(df.loc[season[4:].replace(".csv","")])
    df_concat = pd.concat(dfList, axis=0)

    return {
        "data": [go.Scatter(x=[season[4:].replace(".csv","")[:4] for season in seasons], y=df_concat[option], name="Player's " + option, text = df_concat["Player"], hoverinfo = "text+y")],
        "layout": go.Layout(title="NBA MVPs for each Season", xaxis={"title":"Season"}, yaxis={"title":option})
    }


if __name__ =="__main__":
    app.run_server(host ="0.0.0.0")