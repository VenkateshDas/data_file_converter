import pandas as pd
from io import BytesIO
from typing import Tuple
import os

class DataFileConverter:

    def __init__(self):
        self.supported_file_types = ['csv', 'json', 'xlsx', 'parquet', 'feather', 'pickle', 'pkl', 'hdf', 'html', 'xml']

    def _detect_file_type(self, file_path: str) -> str:
        file_type = file_path.split('.')[-1]
        return file_type

    def _extract_file_name(self, file_path: str) -> str:
        file_name = file_path.split('.')[0]
        return file_name

    # A function to convert any file format to dataframe in pandas. It accepts file path and file types as arguments and returns a dataframe.
    def convert_to_dataframe(self, input_file_path: BytesIO, file_type: str) -> pd.DataFrame:
        if file_type == 'xlsx':
            df = pd.read_excel(input_file_path)
        elif file_type == 'pkl':
            df = pd.read_pickle(input_file_path)
        elif file_type in self.supported_file_types:
            df = getattr(pd, f'read_{file_type}')(input_file_path)
        else:
            raise ValueError('File type not supported')
        return df

    # A function to convert any dataframe to any file format. It accepts dataframe, file path and file types as arguments and returns a dataframe.
    def convert_to_file(self, df: pd.DataFrame, output_file_name: str, file_type: str):
        if file_type in self.supported_file_types:
            return getattr(df, f'to_{file_type}')()
        else:
            raise ValueError('File type not supported')

    def convert_file(self, input_file_path: BytesIO, output_file_type: str) -> Tuple:
        # streamlit specific code for reading file name from the file uploader widget
        input_file_address = input_file_path.name
        input_file_name = self._extract_file_name(input_file_address)
        input_file_type = self._detect_file_type(input_file_address)
        df = self.convert_to_dataframe(input_file_path, input_file_type)
        output_file = self.convert_to_file(df, input_file_name, output_file_type)
        output_file_name = f"{input_file_name}.{output_file_type}"

        return output_file, output_file_name
