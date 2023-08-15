import streamlit as st
import pandas as pd
def main():
    st.title("Online Excel Data Import App")
    
    # Upload Excel file
    uploaded_file = st.file_uploader("https://drrabangladesh-my.sharepoint.com/:x:/g/personal/mamun_arktechbd_org/EeUPMTenrYNFh4YechyHKAUBaUadsZ7MtOboEDv5zVdAIQ?e=U5SUry", type=["xlsx", "xls"])
    
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.dataframe(df)
        
if __name__ == "__main__":
    main()

