from datetime import date
from constants import TABLES
from db_client import AbstractDBClient, MySQLClient
from logger import configure_logger
from typing import Any
from schema import PitchType, Merged
import pandas as pd
import numpy as np

logger = configure_logger(__name__)


class BaseRepository():
    def __init__(
        self,
        db_client: AbstractDBClient,
    ):
        self.db_client = db_client
        self.table_name: str = ""
        
    def execute_select_query(
        self,
        query: str,
        parameters: tuple | None = None,
    ) -> list[dict[str, Any]]:

        logger.info(f"select query: {query}, parameters: {parameters}")

        with self.db_client.get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(query, parameters)
                rows = cursor.fetchall()
                
        return rows


class PitchTypeRepository(BaseRepository):
    def __init__(
        self,
        db_client: AbstractDBClient,
    ):
        super().__init__(db_client=db_client)
        self.table_name: str = TABLES.BATTING.value
        
    def select(self) -> list[PitchType]:
        query = f"""
        select distinct pitch_type from {self.table_name};
        """
        # list[dict]
        records = self.execute_select_query(query=query)
        
        # list[Batting]
        # pythonオブジェクトへの変換
        pitch_types = [PitchType(**r) for r in records]
        
        return pitch_types


class MergedRepository(BaseRepository):
    def __init__(
        self,
        db_client: AbstractDBClient,
    ):
        super().__init__(db_client=db_client)
        self.table_name: str = 'batting'
        
    def select(
            self,
            pitch_type: str = None,
            ) -> list[Merged]:
        query = f"""
        select 
            {self.table_name}.*,
            gd.day_of_week,
            gd.day_name
        from 
            {self.table_name}
        join
            {TABLES.GAME_DATES.value} gd on {self.table_name}.game_date = gd.date
        """
        
        where=""
        parameters=[]
        
        prefix = "where"
        if pitch_type is not None:
            where += f"{prefix} {self.table_name}.pitch_type = %s "
            parameters.append(pitch_type)
            prefix = "and"
        
        query += where

        # list[dict]
        records = self.execute_select_query(
            query=query,
            parameters=tuple(parameters),
        )
                
        # list[Batting]
        # pythonオブジェクトへの変換
        data = [Merged(**r) for r in records]
        
        return data

# debug
if __name__ == "__main__":
    db_client = MySQLClient()

    # pt = PitchTypeRepository(db_client=db_client)
    # pitch_types = pt.select()
    # lst = [pitch_type.pitch_type for pitch_type in pitch_types]
    # print(lst)

    merged = MergedRepository(db_client=db_client)
    data = merged.select(
        pitch_type='FS'
    )
    # print(data)
    df = pd.DataFrame([d.dict() for d in data])
    print(df.head())