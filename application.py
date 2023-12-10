import pandas as pd
import datetime
import xgboost as xgb
import streamlit as st
import datetime

def main():
    html_temp = """
    <div style="background-color:lightblue; padding:16px">
    <h2 style="color:black; text-align:center;">Car Price Prediction using Machine Learning</h2>
    </div>
    """
    model = xgb.XGBRegressor()
    model.load_model('xgb_model.json')
    
    st.markdown(html_temp,unsafe_allow_html=True)
    st.write('')
    st.write('')
    
    st.markdown("#### Are You Planning to Sell Your Car ? \n #### So Let's Try Evaluating Price")
    st.write('')

    p1 = st.number_input("Current Show Room Price Of Car",1.5,50.0,step=1.0)
    st.write('')
    
    p2 = st.number_input('Enter Number of KiloMetres Driven',10,5000000000,step=50)
    st.write('')
    
    s1 = st.selectbox("Enter Fuel Type",('Petrol','Diesel','CNG'))
    if s1 == 'Petrol':
        p3 = 0
    elif s1 == 'Diesel':
        p3 = 1
    elif s1 == 'CNG':
        p3 = 2
    st.write('')
    
    s2 = st.selectbox("ARE YOU DEALER OR INDIVIDUAL",('Dealer','Individual'))
    if s2 == 'Dealer':
        p4 = 0
    elif s2 == 'Individual':
        p4 = 1
    st.write('')
    
    s3 = st.selectbox('Transmission Type',('Manual','Automatinc'))
    if s3 == 'Automatinc':
        p5 = 1
    if s3 == 'Manual':
        p5 = 0
    st.write('')
    
    p6 = st.slider("Number of Owner the Car Previously Had ",0,4)
    st.write('')
     
    date_time = datetime.datetime.now()
    years = st.number_input("In which year car was purchased ",2000,date_time.year)
    p7 = date_time.year - years 
    st.write('')
    
    data_new = pd.DataFrame({
        'Present_Price':p1,
        'Kms_Driven':p2,
        'Fuel_Type':p3,
        'Seller_Type':p4,
        'Transmission':p5,
        'Owner':p6,
        'Age':p7  
    },index=[0])
    
    try:
        if st.button('Predict'):
         pred = model.predict(data_new)
        if pred > 0:
           st.success("You can sell your car for {:.2f} Lakhs".format(pred[0]))
        else:
            st.warning("Nothing")
    except:
        st.warning(" we are here to give best price of your car !! ")
    
    
    
    
    
    
    
    
        



if __name__ == "__main__":
    main()
