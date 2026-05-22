import streamlit as st

st.title("🏷️ Label Generator")

with st.form("label_form"):

    name = st.text_input("Name")
    product = st.text_input("Product")
    batch = st.text_input("Batch Number")
    notes = st.text_area("Notes")

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
                border: 3px solid black;
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

            <p><b>Name:</b> {name}</p>
            <p><b>Product:</b> {product}</p>
            <p><b>Batch:</b> {batch}</p>
            <p><b>Notes:</b> {notes}</p>
        </div>

        <button onclick="window.print()">
            Download / Save as PDF
        </button>

    </body>
    </html>
    """

    st.components.v1.html(html, height=600, scrolling=True)
