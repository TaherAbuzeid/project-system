import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from oauth2client.service_account import ServiceAccountCredentials
import datetime

# تحميل بيانات الاعتماد من Streamlit secrets
st.write(st.secrets)
service_account_info = st.secrets["gcp_service_account"]

# إنشاء الاتصال بجوجل شيتس
creds = Credentials.from_service_account_info(service_account_info)
client = gspread.authorize(creds)

# فتح الأوراق في Google Sheets
sheet1 = client.open("Streamlit").worksheet("Users")
sheet2 = client.open("Streamlit").worksheet("UserData")



Ad_Accounts = ["Didi","ADV","INT","DGM Active Fit","c+o","Mohamed H","khmis1","khmis2","khmis3","Broad","فهداوف1110","p1 knee 2","MARIOU","knee مستورد"]
Client = ["zoghby"]
Media_Buyer = ["ahmed","Taher","MH"]
Products = ["عسل","jacet","مشد حريمي كامل","مشد شورت","مشد الضهر","حزام بطن","زيت زيتون"]

st.image("nn.jpg", use_column_width=True)
st.title("Welcome System ✅")

# كلمات المرور لكل جزء
passwrd_Fund = "taher@010"
passwrd_dash = "elzoghby@010"

# تعريف حالة تسجيل الدخول في session_state
if "logged_in_fund" not in st.session_state:
    st.session_state.logged_in_fund = False
    st.session_state.username_fund = ""

if "logged_in_dash" not in st.session_state:
    st.session_state.logged_in_dash = False
    st.session_state.username_dash = ""

choice = st.radio("اختر العملية:", ["Fund Data", "Dashboard"])

if choice == "Fund Data":
    # الخطوة 1: نموذج تسجيل الدخول
    if not st.session_state.logged_in_fund:
        with st.form(key="user_input_form_fund"):
            name = st.selectbox("Enter name:",["Taher","Ahmed", "MH"])
            password = st.text_input("Enter password:", type="password")
            submit_button = st.form_submit_button("LogIn")

        if submit_button:
            if not name or not password:
                st.warning("⚠️ Please fill in all fields!")
            elif password == passwrd_Fund:
                new_row = [name, datetime.datetime.now().strftime("%Y-%m-%d"),"Fund"]
                sheet1.append_row(new_row)
                st.session_state.logged_in_fund = True
                st.session_state.username_fund = name
                st.success(f"Welcome {name} ✅")
                st.experimental_rerun()
            else:
                st.error("❌ Incorrect password!")

    # الخطوة 2: إذا كان المستخدم مسجل الدخول، يظهر النموذج الثاني
    if st.session_state.logged_in_fund:
        st.subheader("Enter Your Details 📄")

        with st.form(key="user_data_form"):
            client = st.selectbox("Enter Your Account: ", Client)
            media_buyer = st.selectbox("Enter Your Media Buyer: ", Media_Buyer)
            products = st.selectbox("Enter Your Product: ", Products)
            ad_Accounts = st.selectbox("Enter Your Ad Account: ", Ad_Accounts)
            Fund = st.number_input("Enter Fund: ")
            Code = st.number_input("Enter Code: ")
            submit_details = st.form_submit_button("Save Data")

        if submit_details:
            if not client or not media_buyer or not products or not ad_Accounts :
                st.warning("⚠️ Please fill in all fields!")
            else:
                new_data_row = [st.session_state.username_fund, client, media_buyer, products, ad_Accounts, datetime.datetime.now().strftime("%Y-%m-%d"), Fund, Code]
                sheet2.append_row(new_data_row)
                st.success("✅ Your data has been saved successfully!")

elif choice == "Dashboard":
    # الخطوة 1: نموذج تسجيل الدخول
    if not st.session_state.logged_in_dash:
        with st.form(key="user_input_form_dash"):
            name = st.selectbox("Enter name:",["Taher","Ahmed", "MH"])
            password = st.text_input("Enter password:", type="password")
            submit_button = st.form_submit_button("LogIn")

        if submit_button:
            if not name or not password:
                st.warning("⚠️ Please fill in all fields!")
            elif password == passwrd_dash:
                new_row = [name, datetime.datetime.now().strftime("%Y-%m-%d"),"Dashboard"]
                sheet1.append_row(new_row)
                st.session_state.logged_in_dash = True
                st.session_state.username_dash = name
                st.success(f"Welcome {name} ✅")
                st.experimental_rerun()
            else:
                st.error("❌ Incorrect password!")

    # الخطوة 2: إذا كان المستخدم مسجل الدخول، يظهر البيانات المرتبطة بالـ Dashboard
    if st.session_state.logged_in_dash:
        st.write("🔍 سيتم عرض الـ Dashboard هنا...")
        # هنا سيتم إضافة كود عرض وتحليل البيانات باستخدام Plotly وغيرها
