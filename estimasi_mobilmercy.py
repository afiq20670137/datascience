import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobilmercy.sav', 'rb'))


st.title('Estimasi Harga Mobil Bekas Mercedes Benz')
st.image('mercedes.webp')


year = st.number_input('Tahun mobil')
mileage = st.number_input('Kilometer mobil')
tax = st.number_input('Pajak mobil')
mpg = st.number_input('konsumsi BBM')
engineSize = st.number_input('ukuran mesin')

predict = ''
if st.button('estimasi harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    st.write('estimasi harga mobil bekas dalam pounds : ', predict)
    st.write('estimasi harga mobil bekas dalam IDR : ', predict*19000)
    
    
    st.text('Created By Afiq & Niken')
