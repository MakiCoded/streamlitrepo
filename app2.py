import streamlit as st

st.title('Currency Converter App')
st.write('This App convert the currency of one country to another currency!')

sidebar = st.sidebar
sidebar.header("Our Current Exchange Rate💲") 
sidebar.write("""
            :blue['USD - NGN']: 1700\n
            :blue['USD - CAD']: 1.43\n
            :blue['NGN - USD']: 0.00064\n
            :blue['NGN - CAD']: 0.00092\n
            :blue['CAD - USD']: 0.70\n
            :blue['CAD - NGN']: 1085.00
""")
sidebar.divider()
sidebar.subheader('🎯About')
sidebar.write('This is a simple currency converter that converts the currency of one country to another currency. It is built with Streamlit and Python.')   
        
rate = {
    'USD - NGN': 1700,
    'USD - CAD': 1.43,
    'NGN - USD': 0.00064,
    'NGN - CAD': 0.00092,
    'CAD - USD': 0.70,
    'CAD - NGN': 1085.00
}

result = 0

col1, col2 = st.columns(2)

with col1:
    Currency_from = st.selectbox('Select Source Currency', ['USD', 'CAD', 'NGN'], key='currency_from')
    currency_destination = st.selectbox('Select destination Currency', ['USD', 'CAD','NGN'], key='currency_destination')
    if pair in rate:
        result = amount * rate[pair]
        return result
    else:
        
with col2:
    amount1 = st.number_input('Enter the amount to convert')
    amount2 = st.number_input('Enter the amount to convert')

   pair = f'{Currency_from} - {currency_destination}'
       
            st.metric(label ='Conversion Result', value=f'{result:,.2f}') 
            #is equal to :orange[{Result:,.2f}] {currency_destination}')
        else:
            st.metric('Conversion Result', 'Invalid currency pair')
    

