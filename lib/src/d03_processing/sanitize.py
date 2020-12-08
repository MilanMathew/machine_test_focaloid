def stringify_keys(team_dict):
    sanitize_key = lambda x: x[0]
    team_keys = list(team_dict.keys())
    results = [(sanitize_key(team_key), team_dict[team_key]) for team_key in team_keys]
    # if len(results) == 0:
    #     return results[0]
    
    return results


def formatted_decimal(dividend, divisor, no_of_decimals=1):
    percent = round(dividend * 1.0 / divisor, no_of_decimals)
    if percent % 1 > 0:
        return percent
    else:
        return int(percent)