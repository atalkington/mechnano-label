import streamlit as st
from fpdf import FPDF
from io import BytesIO

st.set_page_config(page_title="PDF Label Generator")

st.title("🏷️ PDF Label Generator")

# ---------- FORM ----------
with st.form("label_form"):

    name = st.text_input("Name")
    product = st.text_input("Product")
    batch = st.text_input("Batch Number")
    date = st.date_input("Date")
    notes = st.text_area("Notes")

    submitted = st.form_submit_button("Generate PDF Label")

# ---------- GENERATE PDF ----------
if submitted:

    # Create PDF
    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Arial", "B", 18)
    pdf.cell(200, 10, "PRODUCT LABEL", ln=True, align="C")

    pdf.ln(10)

    # Content
    pdf.set_font("Arial", size=12)

    pdf.cell(50, 10, f"Name: {name}", ln=True)
    pdf.cell(50, 10, f"Product: {product}", ln=True)
    pdf.cell(50, 10, f"Batch #: {batch}", ln=True)
    pdf.cell(50, 10, f"Date: {date}", ln=True)

    pdf.ln(5)

    pdf.multi_cell(0, 10, f"Notes:\n{notes}")

    # Save PDF to memory
    pdf_output = BytesIO()
    pdf_bytes = pdf.output(dest="S").encode("latin-1")
    pdf_output.write(pdf_bytes)

    st.success("PDF label generated!")

    # Download button
    st.download_button(
        label="⬇️ Download Label PDF",
        data=pdf_output.getvalue(),
        file_name="label.pdf",
        mime="application/pdf"
    )
