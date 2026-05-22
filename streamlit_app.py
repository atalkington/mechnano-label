import streamlit as st

def render_label(name, sku, net_weight, lot_number, mfg_date, coo):

    design_width = 1488
    design_height = 1024

    container_width = 200  # <-- change this to whatever fits Streamlit
    scale = container_width / design_width

    html = f"""
    <style>
        .scale-wrapper {{
            width: {design_width}px;
            height: {design_height}px;
            transform: scale({scale});
            transform-origin: top left;
        }}
        .label-container {{
            position:relative;
            width:{design_width}px;
            height:{design_height}px;
            background:#dcdcdc;
            overflow:hidden;
            margin:auto;
            font-family:Arial, Helvetica, sans-serif;
        }}

        .top-bar {{
            position:absolute;
            top:0;
            left:0;
            width:100%;
            height:210px;
            background:linear-gradient(to right,#000,#1c1c1c);
        }}

        .diag1 {{
            position:absolute;
            top:-180px;
            right:-120px;
            width:1200px;
            height:700px;
            background:#9f9f9f;
            transform:rotate(-32deg);
        }}

        .diag2 {{
            position:absolute;
            bottom:-260px;
            left:-260px;
            width:1200px;
            height:500px;
            background:#b8b8b8;
            transform:rotate(-32deg);
            opacity:0.65;
        }}

        .logo {{
            position:absolute;
            top:20px;
            left:30px;
            color:white;
        }}

        .logo-top, .logo-bottom {{
            font-size:100px;
            font-weight:700;
            line-height:0.9;
        }}

        .logo-bottom {{
            margin-left:40px;
        }}

        .content {{
            position:absolute;
            top:220px;
            left:45px;
            color:black;
        }}

        .content-row {{
            font-size:64px;
            margin-bottom:25px;
            line-height:1;
        }}

        .footer-left {{
            position:absolute;
            left:30px;
            bottom:40px;
            font-size:34px;
            line-height:1.25;
            color:black;
        }}

        .footer-note {{
            position:absolute;
            bottom:60px;
            left:700px;
            font-size:22px;
            font-weight:700;
            color:white;
            text-align:center;
        }}
    </style>

    <div class="label-container">

        <div class="top-bar"></div>
        <div class="diag1"></div>
        <div class="diag2"></div>

        <div class="logo">
            <div class="logo-top">Mechnano</div>
        </div>

        <div class="content">
            <div class="content-row"><b>NAME:</b> {name}</div>
            <div class="content-row"><b>SKU:</b> {sku}</div>
            <div class="content-row"><b>NET WEIGHT:</b> {net_weight}</div>
            <div class="content-row"><b>LOT #:</b> {lot_number}</div>
            <div class="content-row"><b>MFG. DATE:</b> {mfg_date}</div>
            <div class="content-row"><b>COO:</b> {coo}</div>
        </div>

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
    """

    st.components.v1.html(html, width=600, height=400, scrolling=True)

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
        render_label(
                name,
                sku,
                net_weight,
                lot_number, 
                mfg_date,
                coo
        )
