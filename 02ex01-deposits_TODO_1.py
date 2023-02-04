# TODO: add lines to calculate yields for some common periods
#       of time (e.g. 1 month, 1 year, 5 years, 10 years)
# TODO: change the script to output the 1-year percent yield
#       as well
# TODO: (extra) Output only percents if the initial SUM is
#       not known at the moment the script is run

def deposit(initial_sum, percent, fixed_period, set_period):
    """Calculate deposit yield."""
    per = percent / 100
    growth = (1 + per) ** (set_period / fixed_period)
    
    growth_mounth = (1 + per) ** (set_period / (1/12))
    
    growth_1_year = (1 + per) ** (set_period / 1)
    
    growth_5_years = (1 + per) ** (set_period / 5)

    growth_10_yaears = (1 + per) ** (set_period / 10)

    return (f"Yields for {set_period} will be: {initial_sum} * {growth}")
    return (f"Yields for 1 mounth will be: {initial_sum} * {growth_mounth}")
    return (f"Yields for 1 yesr will be: {initial_sum} * {growth_1_year}")
    return (f"Yields for 5 years will be: {initial_sum} * {growth_5_years}")
    return (f"Yields for 10 yesr will be: {initial_sum} * {growth_10_yaears}")