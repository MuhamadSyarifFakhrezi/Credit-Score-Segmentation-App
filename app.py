import streamlit as st
import pandas as pd
import joblib
import time
from data_preprocessing import data_preprocessing, encoder_Credit_Mix, encoder_Payment_Behaviour, encoder_Payment_of_Min_Amount
from prediction import prediction

st.image('image.png')

st.warning('''
         ###### ⚠️ Please input some information to predict customer segmentation based on credit score
         ''')

data = pd.DataFrame()

col1, col2 = st.columns(2, gap='large')

with col1:
    Credit_Mix = st.selectbox(label='Credit Mix', options=list(encoder_Credit_Mix.categories_[0]), index=2)
    data["Credit_Mix"] = [Credit_Mix]

with col2:
    Payment_of_Min_Amount = st.selectbox(label='Payment of Min Amount', options=list(encoder_Payment_of_Min_Amount.categories_[0]), index=2)
    data["Payment_of_Min_Amount"] = [Payment_of_Min_Amount]

Payment_Behaviour = st.selectbox(label='Payment Behaviour', options=list(encoder_Payment_Behaviour.categories_[0]), index=5)
data["Payment_Behaviour"] = Payment_Behaviour

col1, col2, col3, col4 = st.columns(4)

with col1:
    Age = int(st.number_input('Age', 0, 56, value=33))
    data["Age"] = Age

with col2:
    Num_Bank_Accounts = int(st.number_input('Num Bank Accounts', 0, 10, value=5))
    data["Num_Bank_Accounts"] = Num_Bank_Accounts

with col3:
    Num_Credit_Card = int(st.number_input('Num Credit Card', 0, 11, value=5))
    data["Num_Credit_Card"] = Num_Credit_Card

with col4:
    Interest_Rate = float(st.number_input('Interest Rate', 1, 34, value=14))
    data["Interest_Rate"] = Interest_Rate


col1, col2, col3, col4 = st.columns(4)

with col1:
    Num_of_Loan = int(st.number_input('Num of Loan', 0, 9, value=4))
    data["Num_of_Loan"] = Num_of_Loan

with col2:
    Delay_from_due_date = int(st.number_input('Delay from due date', 0, 67, value=21))
    data["Delay_from_due_date"] = Delay_from_due_date

with col3:
    Num_of_Delayed_Payment = int(st.number_input('Num of Delayed Payment', 0, 28, value=13))
    data["Num_of_Delayed_Payment"] = Num_of_Delayed_Payment

with col4:
    Changed_Credit_Limit = float(st.number_input('Changed Credit Limit', 0.00, 36.97, value=10.00))
    data["Changed_Credit_Limit"] = Changed_Credit_Limit

col1, col2, col3, col4 = st.columns(4)

with col1:
    Num_Credit_Inquiries = float(st.number_input('Num Credit Inquiries', 0, 17, value=6))
    data["Num_Credit_Inquiries"] = Num_Credit_Inquiries

with col2:
    Outstanding_Debt = float(st.number_input('Outstanding Debt', 0.23, 4998.07, value=1426.00))
    data["Outstanding_Debt"] = Outstanding_Debt

with col3:
    Monthly_Inhand_Salary = float(st.number_input('Monthly Inhand Salary', 303.645417, 15204.633333, value=4198.00))
    data["Monthly_Inhand_Salary"] = Monthly_Inhand_Salary

with col4:
    Monthly_Balance = float(st.number_input('Monthly Balance', 0.00776, 1602.040519, value=403.00))
    data["Monthly_Balance"] = Monthly_Balance

col1, col2, col3 = st.columns(3)

with col1:
    Amount_invested_monthly = float(st.number_input('Amount invested monthly', 0.00, 1977.326102, value=193.00))
    data["Amount_invested_monthly"] = Amount_invested_monthly

with col2:
    Total_EMI_per_month = float(st.number_input('Total EMI per month', 0.00, 1779.103254, value=107.00))
    data["Total_EMI_per_month"] = Total_EMI_per_month

with col3:
    Credit_History_Age = float(st.number_input('Credit History Age', 1, 404, value=221))
    data["Credit_History_Age"] = Credit_History_Age

with st.expander("View the Raw Data"):
    st.dataframe(data=data, width=800, height=10)

if st.button('Predict'):
    try:
        new_data = data_preprocessing(data=data)
        with st.expander("View the Preprocessed Data"):
            st.dataframe(data=new_data, width=800, height=10)        
        result = prediction(new_data)

        if result == 'Good':
            result_text = """
            #### This Customer has a :green-background[:green[{} Credit Score]]
            """.format(result)
        elif result == 'Poor':
            result_text = """
            #### This Customer has a :red-background[:red[{} Credit Score]]
            """.format(result)
        else:
            result_text = """
            #### This Customer has a :grey-background[:grey[{} Credit Score]]
            """.format(result)

        def stream_data():
            for word in result_text.split(" "):
                yield word + " "
                time.sleep(0.1)

        st.write_stream(stream_data)
    except ValueError:
        st.error('Please Complete The Information Above:smiley:')