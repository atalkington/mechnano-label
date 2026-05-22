import streamlit as st

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

    html = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial;
                padding: 40px;
            }}

            .label {{
                width: 400px;
                border: 3px solid white;
                padding: 20px;
                border-radius: 12px;
            }}

            h2 {{
                text-align: center;
            }}

            p {{
                font-size: 18px;
            }}

            button {{
                margin-top: 20px;
                padding: 10px 20px;
                font-size: 16px;
            }}
        </style>
    </head>

    <body>

        <div class="label">
            <h2>PRODUCT LABEL</h2>

            <p><b>NAME:</b> {name}</p>
            <p><b>SKU:</b> {sku}</p>
            <p><b>NET WEIGHT:</b> {net_weight}</p>
            <p><b>LOT #:</b> {lot_number}</p>
            <p><b>MFG. DATE:</b> {mfg_date}</p>
            <p><b>COO:</b> {coo}</p>
        </div>

        <button onclick="window.print()">
            Download / Save as PDF
        </button>

    </body>
    </html>
    """

    st.components.v1.html(html, height=600, scrolling=True)
