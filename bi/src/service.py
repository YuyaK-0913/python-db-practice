from datetime import date
import numpy as np
import pandas as pd
from db_client import AbstractDBClient, MySQLClient
from logger import configure_logger
from model import PitchTypeRepository, MergedRepository
from schema import PitchType, Merged

logger = configure_logger(__name__)


class BaseService(object):
    def __init__(
        self,
        db_client: AbstractDBClient,
    ):
        self.db_client = db_client

class PitchTypeService(BaseService):
    def __init__(
        self,
        db_client: AbstractDBClient,
    ):
        super().__init__(db_client=db_client)
        self.pitch_type_repository = PitchTypeRepository(db_client=db_client)

    def list_pitch_type(self) -> list[str]:
        pitch_types = self.pitch_type_repository.select()
        pitch_types_lst = [pitch_type.pitch_type for pitch_type in pitch_types]
        return pitch_types_lst

class MergedService(BaseService):
    def __init__(
        self,
        db_client: AbstractDBClient,
    ):
        super().__init__(db_client=db_client)
        self.merged_repository = MergedRepository(db_client=db_client)

    def retrieve_merged_data(
            self,
            pitch_type: str = None
            ):
        merged_lst = self.merged_repository.select(pitch_type=pitch_type)
        df = pd.DataFrame([merged.dict() for merged in merged_lst])
        return df


# debug
if __name__ == "__main__":
    db_client = MySQLClient()

    pt = PitchTypeService(db_client=db_client)
    pitch_types_lst = pt.list_pitch_type()
    print(pitch_types_lst)

    ms = MergedService(db_client=db_client)
    ms_df = ms.retrieve_merged_data(pitch_type='FS')
    print(ms_df.tail())