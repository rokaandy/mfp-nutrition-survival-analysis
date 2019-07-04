import json


def daily_totals(nest_dict):
    """Creates list of keys and values from the first dictionary, and zips them together"""
    total_cols = [
        list(nest_dict.keys())[0] + "_" + x["name"].lower() for x in nest_dict["total"]
    ]
    total_values = [y["value"] for y in nest_dict["total"]]
    total_dict = {}
    for col, val in zip(total_cols, total_values):
        total_dict[col] = val
    return total_dict


def daily_goals(nest_dict):
    """Creates list of keys and values from the second dictionary, and zips them together"""
    goal_cols = [
        list(nest_dict.keys())[1] + "_" + k["name"].lower() for k in nest_dict["goal"]
    ]
    goal_values = [i["value"] for i in nest_dict["goal"]]
    goal_dict = {}
    for col, val in zip(goal_cols, goal_values):
        goal_dict[col] = val
    return goal_dict


def merge(dict1, dict2):
    """Combines new keys and values for 'Total' and 'Goals' into single dictionary"""
    res = {**dict1, **dict2}
    return res


def parsed_dict(df, nest_dict):
    """Iterrates through entire parsed dataframe and appends merged rows"""
    results = []
    for row in df["daily_goal"].values:
        nest_dict = json.loads(row)
        results.append(merge(daily_goals(nest_dict), daily_totals(nest_dict)))
    return results


def end_date_col(df):
    """Creates a new column with the previous date of the diary_date column"""
    for index, row in df.iterrows():
        if (index != len(df) - 1):
            df.loc[index, 'end_date'] = df.loc[index + 1, 'diary_date']
