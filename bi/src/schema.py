from datetime import date

from pydantic import BaseModel, Extra

class PitchType(BaseModel):
    pitch_type: str

    class Config:
        extra = Extra.forbid


class Merged(BaseModel):
    game_date: date
    pitch_type: str
    release_speed: float
    batter_name: str
    events: str
    balls: int
    strikes: int
    inning: int
    stand: str
    p_throws: str
    day_of_week: int
    day_name: str
    
    class Config:
        extra = Extra.forbid