import streamlit as st
from data_file_converter.file_converter import DataFileConverter
import mimetypes
import os

# create a streamlit application to convert any file format to any other file format
st.title("Data File Converter")
st.write("Convert any supported file format to any other supported file format for data analysis")
file_converter = DataFileConverter()
input_file = st.file_uploader("Upload a file", type=file_converter.supported_file_types)

if input_file is not None:
    output_file_type = st.selectbox("Select output file type", ['csv', 'json', 'parquet', 'html', 'xml'])
    output_file, output_file_name, df = file_converter.convert_file(input_file, str(output_file_type))
    st.write(df)
    convert = st.button("Convert")
    if convert:
        # Create a download button to download the converted file.
        mimetype = mimetypes.guess_type(output_file_name)[0]
        download_button = st.download_button(
            label="Download converted File",
            data=output_file,
            file_name=output_file_name,
            mime=mimetype,
        )
