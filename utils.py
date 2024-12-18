import numpy as np
import pandas as pd

def getFiles():
    """Return a dictionary of file paths."""
    return {
        'circuits': 'archive/circuits.csv',
        'constructor_results': 'archive/constructor_results.csv',
        'constructor_standings': 'archive/constructor_standings.csv',
        'constructors': 'archive/constructors.csv',
        'driver_standings': 'archive/driver_standings.csv',
        'drivers': 'archive/drivers.csv',
        'lap_times': 'archive/lap_times.csv',
        'pit_stops': 'archive/pit_stops.csv',
        'qualifying': 'archive/qualifying.csv',
        'races': 'archive/races.csv',
        'results': 'archive/results.csv',
        'seasons': 'archive/seasons.csv',
        'sprint_results': 'archive/sprint_results.csv',
        'status': 'archive/status.csv'
    }

def getConstructorColours():
    """Return a dictionary of constructor colors."""
    return {
        'Ferrari': '#E8002D',
        'Sauber': '#52E252',
        'Red Bull': '#3671C6',
        'McLaren': '#FF8000',
        'Mercedes': '#27F4D2',
        'Williams': '#64C4FF',
        'Alpine F1 Team': '#FF87BC',
        'Aston Martin': '#229971',
        'RB F1 Team': '#6692FF',
        'Haas F1 Team': '#B6BABD',
    }

def convert_to_time_format(ms):
    """Convert milliseconds to "minutes:seconds.milliseconds" format."""
    if pd.isna(ms):
        return 'N/A'
    minutes, seconds = divmod(ms // 1000, 60)
    milliseconds = ms % 1000
    return f"{int(minutes)}:{int(seconds):02}.{int(milliseconds):03}"

def convert_lap_time_to_ms(lap_time):
    """Convert lap time from "minutes:seconds" format to milliseconds."""
    if pd.isna(lap_time) or lap_time == r'\N':
        return np.nan  # Return NaN for missing or invalid values
    mins, secs = lap_time.split(':')
    return int(mins) * 60 * 1000 + float(secs) * 1000

def format_minutes(x, pos):
    """Format y-axis ticks for minutes and seconds."""
    minutes, remainder = divmod(x, 1)
    seconds = remainder * 60
    return f'{int(minutes):02}:{seconds:05.3f}'