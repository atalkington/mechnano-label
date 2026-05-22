import streamlit as st

design_width = 1488
design_height = 1024


def build_html(name, sku, net_weight, lot_number, mfg_date, coo):
    return f"""
    <html>
    <head>
    <style>
        @page {{
            size: {design_width}px {design_height}px;
            margin: 0;
        }}

        body {{
            margin: 0;
            padding: 0;
        }}

        .label-container {{
            width: 100%;
            max-width: 900px;
            aspect-ratio: 1488 / 1024;
            position: relative;
            background: #dcdcdc;
            font-family: Arial;
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
            font-size:100px;
            font-weight:700;
        }}

        .content {{
            position:absolute;
            top:220px;
            left:45px;
            font-size:64px;
        }}

        .content-row {{
            margin-bottom:25px;
        }}

        .footer-left {{
            position:absolute;
            left:30px;
            bottom:40px;
            font-size:34px;
        }}

        .footer-note {{
            position:absolute;
            bottom:60px;
            left:700px;
            font-size:22px;
            font-weight:700;
        }}
    </style>
    </head>

    <body>
    <div class="label-container">
        <div class="top-bar"></div>
        <div class="diag1"></div>
        <div class="diag2"></div>

        <div class="logo">Mechnano</div>

        <div class="content">
            <div class="content-row"><b>Name:</b> {name}</div>
            <div class="content-row"><b>SKU:</b> {sku}</div>
            <div class="content-row"><b>Net Weight:</b> {net_weight}</div>
            <div class="content-row"><b>Lot #:</b> {lot_number}</div>
            <div class="content-row"><b>Mfg Date:</b> {mfg_date}</div>
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
    </body>
    </html>
    """


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
    html = build_html(name, sku, net_weight, lot_number, mfg_date, coo)

    st.components.v1.html(html, height=400, scrolling=True)

    st.download_button(
        "⬇️ Download Label (HTML)",
        data=html,
        file_name="label.html",
        mime="text/html"
    )
