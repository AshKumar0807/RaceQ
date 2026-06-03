
import pandas as pd
from pathlib import Path

DATA = Path(__file__).parent.parent / 'data'

def load():
    return {
        'drivers': pd.read_csv(DATA/'drivers.csv'),
        'constructors': pd.read_csv(DATA/'constructors.csv'),
        'results': pd.read_csv(DATA/'results.csv')
    }

def driver_summary():
    d=load()
    r=d['results']
    drv=d['drivers']
    s=r.groupby('driverId').agg(
        races=('raceId','count'),
        wins=('positionOrder',lambda x:(x==1).sum()),
        avg_grid=('grid','mean'),
        avg_finish=('positionOrder','mean')
    ).reset_index()
    s['positions_gained']=s['avg_grid']-s['avg_finish']
    s=s.merge(drv[['driverId','forename','surname']],on='driverId')
    s['driver']=s['forename']+' '+s['surname']
    return s.sort_values('wins',ascending=False)

def team_summary():
    d=load()
    r=d['results']
    c=d['constructors']
    s=r.groupby('constructorId').agg(
        wins=('positionOrder',lambda x:(x==1).sum()),
        points=('points','sum')
    ).reset_index()
    return s.merge(c[['constructorId','name']],on='constructorId')

def elo_rankings():
    scores={2:1515,3:1520,1:1465}
    d=load()['drivers']
    d['elo']=d['driverId'].map(scores)
    d['driver']=d['forename']+' '+d['surname']
    return d[['driver','elo']].sort_values('elo',ascending=False)
