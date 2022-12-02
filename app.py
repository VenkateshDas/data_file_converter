import streamlit as st
from data_file_converter.file_converter import DataFileConverter

# create a streamlit application to convert any file format to any other file format
st.title("File Converter")
st.write("Convert any supported file format to any other supported file format for data analysis")
input_file = st.file_uploader("Upload a file", type=['csv', 'json', 'xlsx', 'parquet', 'feather', 'pickle', 'pkl', 'hdf', 'html', 'xml'])
output_file_type = st.selectbox("Select output file type", ['csv', 'json', 'xlsx', 'parquet', 'feather', 'pickle', 'pkl', 'hdf', 'html', 'xml'])
if input_file is not None:
    # The input file is passed to the __call__ method of the DataFileConverter class to convert the file to the selected file type.
    file_converter = DataFileConverter()
    output_file, output_file_name = file_converter.convert_file(input_file, str(output_file_type))
    # Create a download button to download the converted file.
    st.download_button(
        label="Download converted File",
        data=output_file,
        file_name=output_file_name,
    )
