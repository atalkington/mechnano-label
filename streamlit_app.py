import streamlit as st
from PIL import Image
#import qrcode

st.title("🏷️ Label Generator")

with st.form("label_form"):

    name = st.text_input("Name")
    sku = st.text_input("SKU")
    net_weight = st.text_input("Net Weight")
    lot_number = st.text_input("Lot #")
    mfg_date = st.text_input("Mfg. Date")
    coo = st.text_input("COO")

    submitted = st.form_submit_button("Generate Label")

if submitted:
# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

    st.set_page_config(
        page_title="Elect Nano Label",
        layout="wide"
    )
    
# ---------------------------------------------------
# QR CODE GENERATION
# ---------------------------------------------------

   # large_qr_data = "https://www.electnano.com"
   # small_qr_data = "https://www.electnano.com/ip"
    
  #  large_qr = qrcode.make(large_qr_data)
   # small_qr = qrcode.make(small_qr_data)
# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

    st.markdown(
        """
        <style>
                .label-container{
                position:relative;
                width:1488px;
                height:1024px;
                background:#dcdcdc;
                overflow:hidden;
                margin:auto;
                font-family:Arial, Helvetica, sans-serif;
            }
        
            .top-bar{
                position:absolute;
                top:0;
                left:0;
                width:100%;
                height:210px;
                background:linear-gradient(to right,#000,#1c1c1c);
                z-index:1;
            }
        
            .diag1{
                position:absolute;
                top:-180px;
                right:-120px;
                width:1200px;
                height:700px;
                background:#9f9f9f;
                transform:rotate(-32deg);
                z-index:2;
            }
        
            .diag2{
                position:absolute;
                bottom:-260px;
                left:-260px;
                width:1200px;
                height:500px;
                background:#b8b8b8;
                transform:rotate(-32deg);
                opacity:0.65;
                z-index:1;
            }
        
            .logo{
                position:absolute;
                top:20px;
                left:30px;
                color:white;
                z-index:10;
            }
        
            .logo-top{
                font-size:100px;
                font-weight:700;
                line-height:0.9;
            }
        
            .logo-bottom{
                font-size:100px;
                font-weight:700;
                line-height:0.9;
                margin-left:40px;
            }
        
            .content{
                position:absolute;
                top:220px;
                left:45px;
                z-index:5;
                color:black;
            }
        
            .content-row{
                font-size:64px;
                margin-bottom:25px;
                line-height:1;
            }
        
            .footer-left{
                position:absolute;
                left:30px;
                bottom:40px;
                font-size:34px;
                line-height:1.25;
                color:black;
                z-index:5;
            }
        
            .footer-note{
                position:absolute;
                bottom:60px;
                left:700px;
                font-size:22px;
                font-weight:700;
                color:white;
                text-align:center;
                z-index:5;
            }
        
            .small-qr{
                position:absolute;
                bottom:110px;
                left:880px;
                width:105px;
                height:105px;
                z-index:5;
            }
        
            .large-qr{
                position:absolute;
                bottom:65px;
                right:60px;
                width:260px;
                height:260px;
                background:white;
                padding:12px;
                border-radius:6px;
                z-index:5;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    # ---------------------------------------------------
    # LAYOUT
    # ---------------------------------------------------
    
    st.markdown(
        f"""
        <div class="label-container">
    
            <div class="top-bar"></div>
            <div class="diag1"></div>
            <div class="diag2"></div>
    
            <!-- LOGO -->
            <div class="logo">
                <div class="logo-top">Mech</div>
                <div class="logo-bottom">Nano</div>
            </div>
    
            <!-- CONTENT -->
            <div class="content">
    
                <div class="content-row">
                    <strong>NAME:</strong> {name}
                </div>
    
                <div class="content-row">
                    <strong>SKU:</strong> {sku}
                </div>
    
                <div class="content-row">
                    <strong>NET WEIGHT:</strong> {net_weight}
                </div>
    
                <div class="content-row">
                    <strong>LOT #:</strong> {lot_number}
                </div>
    
                <div class="content-row">
                    <strong>MFG. DATE:</strong> {mfg_date}
                </div>
    
                <div class="content-row">
                    <strong>COO:</strong> {coo}
                </div>
    
            </div>
    
            <!-- FOOTER -->
            <div class="footer-left">
                Mechnano LLC.<br>
                3850 E. Baseline Rd., Suite 126<br>
                Mesa, AZ 85206<br>
                (480) 717-7103<br>
                www.mechnano.com
            </div>
    
            <div class="footer-note">
                This product may be covered by one or more patents.<br>
                Scan QR code or visit www.electnano.com/ip
            </div>
    
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------------------------------------------
# QR CODE OVERLAYS
# ---------------------------------------------------

# Create columns to help place QR codes
#col1, col2, col3 = st.columns([6, 2, 2])

#with col2:
    #st.image(small_qr, width=105)

#with col3:
   # st.image(large_qr, width=260)
