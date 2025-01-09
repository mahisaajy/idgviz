import streamlit as st
import pandas as pd
import plotly.express as px

def make_heatmap(input_df, input_y, input_x, input_color, cmap):
    # Pivot the data to create a matrix for the heatmap
    heatmap_data = input_df.pivot(index=input_y, columns=input_x, values=input_color)

    # Create the heatmap using Plotly
    fig = px.imshow(
        heatmap_data,
        color_continuous_scale=cmap,
        labels={"color": "Nilai"},
    )
    fig.update_layout(
        title="Heatmap Interaktif",
        xaxis_title=input_x,
        yaxis_title=input_y,
        coloraxis_colorbar=dict(title="Nilai"),
    )

    # Use Streamlit to display the heatmap
    st.plotly_chart(fig)

def main():
    # Set page configuration
    st.set_page_config(page_title="Geofisika Dashboard", layout="wide")

    # Sidebar
    st.sidebar.title("Pilih Data Geofisika")

    # Dropdown menu
    data_options = [
        "Petir LD2000",
        "Petir Nexstorm",
        "Magnet",
        "Percepatan Tanah",
        "Intensitas Gempa",
        "Gempa"
    ]

    selected_data = st.sidebar.selectbox("Pilih jenis data:", data_options)

    # Display the selected data
    st.title("Geofisika Dashboard")
    st.write(f"Anda memilih data: **{selected_data}**")


    if selected_data == "Petir LD2000":
        st.subheader("Data Petir LD2000")
        st.write("Informasi mengenai data petir ld2000.")

        # Load CSV file (replace 'magnet-lemi-year.csv' with the actual file path)
        try:
            df_year = pd.read_csv('data/petir-ld2000-ldc-year.csv')

            # Melt the dataframe to make it suitable for heatmap
            df_year_melted = df_year.melt(id_vars=['Station'], var_name='Year', value_name='Value')

            # Create heatmap
            make_heatmap(
                input_df=df_year_melted,
                input_y='Station',
                input_x='Year',
                input_color='Value',
                cmap='RdYlGn'
            )
        except FileNotFoundError:
            st.error("File 'petir-ld2000-ldc-year.csv' tidak ditemukan. Pastikan file tersedia di direktori yang sama dengan aplikasi ini.")

        st.subheader("Data Petir LD2000 per Bulan")
        st.write("Informasi mengenai data magnet per bulan.")

        # Load CSV file (replace 'magnet-lemi-month.csv' with the actual file path)
        try:
            df_month = pd.read_csv('data/petir-ld2000-ldc-month.csv')

            # Melt the dataframe to make it suitable for heatmap
            df_month_melted = df_month.melt(id_vars=['Station'], var_name='Month', value_name='Value')

            # Create heatmap
            make_heatmap(
                input_df=df_month_melted,
                input_y='Station',
                input_x='Month',
                input_color='Value',
                cmap='RdYlGn'  # Adjust the color theme if needed
            )
        except FileNotFoundError:
            st.error("File 'magnet-lemi-month.csv' tidak ditemukan. Pastikan file tersedia di direktori yang sama dengan aplikasi ini.")

    elif selected_data == "Petir Nexstorm":
        st.subheader("Data Petir Nexstorm")
        st.write("Informasi mengenai data petir nexstorm.")

        # Load CSV file (replace 'magnet-lemi-year.csv' with the actual file path)
        try:
            df_year = pd.read_csv('data/petir-nexstorm-nex-year.csv')

            # Melt the dataframe to make it suitable for heatmap
            df_year_melted = df_year.melt(id_vars=['Station'], var_name='Year', value_name='Value')

            # Create heatmap
            make_heatmap(
                input_df=df_year_melted,
                input_y='Station',
                input_x='Year',
                input_color='Value',
                cmap='RdYlGn'
            )
        except FileNotFoundError:
            st.error("File 'petir-nexstorm-nex-year.csv' tidak ditemukan. Pastikan file tersedia di direktori yang sama dengan aplikasi ini.")

        st.subheader("Data Petir Nexstorm per Bulan")
        st.write("Informasi mengenai data nexstorm per bulan.")

        # Load CSV file (replace 'magnet-lemi-month.csv' with the actual file path)
        try:
            df_month = pd.read_csv('data/petir-nexstorm-nex-month.csv')

            # Melt the dataframe to make it suitable for heatmap
            df_month_melted = df_month.melt(id_vars=['Station'], var_name='Month', value_name='Value')

            # Create heatmap
            make_heatmap(
                input_df=df_month_melted,
                input_y='Station',
                input_x='Month',
                input_color='Value',
                cmap='RdYlGn'  # Adjust the color theme if needed
            )
        except FileNotFoundError:
            st.error("File 'petir-nexstorm-nex-month.csv' tidak ditemukan. Pastikan file tersedia di direktori yang sama dengan aplikasi ini.")

    elif selected_data == "Magnet":
        st.subheader("Data Magnet")
        st.write("Informasi mengenai data magnet.")

        # Load CSV file (replace 'magnet-lemi-year.csv' with the actual file path)
        try:
            df_year = pd.read_csv('data/magnet-lemi-year.csv')

            # Melt the dataframe to make it suitable for heatmap
            df_year_melted = df_year.melt(id_vars=['Station'], var_name='Year', value_name='Value')

            # Create heatmap
            make_heatmap(
                input_df=df_year_melted,
                input_y='Station',
                input_x='Year',
                input_color='Value',
                cmap='RdYlGn'
            )
        except FileNotFoundError:
            st.error("File 'magnet-lemi-year.csv' tidak ditemukan. Pastikan file tersedia di direktori yang sama dengan aplikasi ini.")

        st.subheader("Data Magnet per Bulan")
        st.write("Informasi mengenai data magnet per bulan.")

        # Load CSV file (replace 'magnet-lemi-month.csv' with the actual file path)
        try:
            df_month = pd.read_csv('data/magnet-lemi-month.csv')

            # Melt the dataframe to make it suitable for heatmap
            df_month_melted = df_month.melt(id_vars=['Station'], var_name='Month', value_name='Value')

            # Create heatmap
            make_heatmap(
                input_df=df_month_melted,
                input_y='Station',
                input_x='Month',
                input_color='Value',
                cmap='RdYlGn'  # Adjust the color theme if needed
            )
        except FileNotFoundError:
            st.error("File 'magnet-lemi-month.csv' tidak ditemukan. Pastikan file tersedia di direktori yang sama dengan aplikasi ini.")

    elif selected_data == "Percepatan Tanah":
        st.subheader("Data Percepatan Tanah")
        st.write("Informasi mengenai data percepatan tanah.")

        # Load CSV file (replace 'magnet-lemi-year.csv' with the actual file path)
        try:
            df_year = pd.read_csv('data/percepatantanah-ew-year.csv')

            # Melt the dataframe to make it suitable for heatmap
            df_year_melted = df_year.melt(id_vars=['Station'], var_name='Year', value_name='Value')

            # Create heatmap
            make_heatmap(
                input_df=df_year_melted,
                input_y='Station',
                input_x='Year',
                input_color='Value',
                cmap='RdYlGn'
            )
        except FileNotFoundError:
            st.error("File 'percepatantanah-ew-year.csv' tidak ditemukan. Pastikan file tersedia di direktori yang sama dengan aplikasi ini.")

        st.subheader("Data Percepatan Tanah per Bulan")
        st.write("Informasi mengenai data percepatan tanah per bulan.")

        # Load CSV file (replace 'magnet-lemi-month.csv' with the actual file path)
        try:
            df_month = pd.read_csv('data/percepatantanah-ew-month.csv')

            # Melt the dataframe to make it suitable for heatmap
            df_month_melted = df_month.melt(id_vars=['Station'], var_name='Month', value_name='Value')

            # Create heatmap
            make_heatmap(
                input_df=df_month_melted,
                input_y='Station',
                input_x='Month',
                input_color='Value',
                cmap='RdYlGn'  # Adjust the color theme if needed
            )
        except FileNotFoundError:
            st.error("File 'percepatantanah-ew-month.csv' tidak ditemukan. Pastikan file tersedia di direktori yang sama dengan aplikasi ini.")

    elif selected_data == "Intensitas Gempa":
        st.subheader("Data Intensitas Gempa")
        st.write("Informasi mengenai data intensitas gempa.")

        # Load CSV file (replace 'magnet-lemi-year.csv' with the actual file path)
        try:
            df_year = pd.read_csv('data/intensitasgempa-ew-year.csv')

            # Melt the dataframe to make it suitable for heatmap
            df_year_melted = df_year.melt(id_vars=['Station'], var_name='Year', value_name='Value')

            # Create heatmap
            make_heatmap(
                input_df=df_year_melted,
                input_y='Station',
                input_x='Year',
                input_color='Value',
                cmap='RdYlGn'
            )
        except FileNotFoundError:
            st.error("File 'intensitasgempa-ew-year.csv' tidak ditemukan. Pastikan file tersedia di direktori yang sama dengan aplikasi ini.")

        st.subheader("Data Intensitas Gempa per Bulan")
        st.write("Informasi mengenai data intensitas gempa per bulan.")

        # Load CSV file (replace 'magnet-lemi-month.csv' with the actual file path)
        try:
            df_month = pd.read_csv('data/intensitasgempa-ew-month.csv')

            # Melt the dataframe to make it suitable for heatmap
            df_month_melted = df_month.melt(id_vars=['Station'], var_name='Month', value_name='Value')

            # Create heatmap
            make_heatmap(
                input_df=df_month_melted,
                input_y='Station',
                input_x='Month',
                input_color='Value',
                cmap='RdYlGn'  # Adjust the color theme if needed
            )
        except FileNotFoundError:
            st.error("File 'intensitasgempa-ew-month.csv' tidak ditemukan. Pastikan file tersedia di direktori yang sama dengan aplikasi ini.")

    elif selected_data == "Gempa":
        st.subheader("Data Gempa")
        st.write("Informasi mengenai data gempa.")

        # Load CSV file (replace 'magnet-lemi-year.csv' with the actual file path)
        try:
            df_year = pd.read_csv('data/gempabumi-ew-year.csv')

            # Melt the dataframe to make it suitable for heatmap
            df_year_melted = df_year.melt(id_vars=['Station'], var_name='Year', value_name='Value')

            # Create heatmap
            make_heatmap(
                input_df=df_year_melted,
                input_y='Station',
                input_x='Year',
                input_color='Value',
                cmap='RdYlGn'
            )
        except FileNotFoundError:
            st.error("File 'gempabumi-ew-year.csv' tidak ditemukan. Pastikan file tersedia di direktori yang sama dengan aplikasi ini.")

        st.subheader("Data Gempa per Bulan")
        st.write("Informasi mengenai data gempa per bulan.")

        # Load CSV file (replace 'magnet-lemi-month.csv' with the actual file path)
        try:
            df_month = pd.read_csv('data/gempabumi-ew-month.csv')

            # Melt the dataframe to make it suitable for heatmap
            df_month_melted = df_month.melt(id_vars=['Station'], var_name='Month', value_name='Value')

            # Create heatmap
            make_heatmap(
                input_df=df_month_melted,
                input_y='Station',
                input_x='Month',
                input_color='Value',
                cmap='RdYlGn'  # Adjust the color theme if needed
            )
        except FileNotFoundError:
            st.error("File 'gempabumi-ew-month.csv' tidak ditemukan. Pastikan file tersedia di direktori yang sama dengan aplikasi ini.")


    else:
        st.write("Pilih data Magnet untuk melihat heatmap.")

if __name__ == "__main__":
    main()
