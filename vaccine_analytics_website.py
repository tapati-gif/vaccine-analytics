import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------- PAGE SETUP ----------------
st.set_page_config(
    page_title="Vaccine Analytics Mini Project",
    layout="wide"
)

st.title("💉 Vaccine Analytics Mini Project")
st.subheader("Biotechnology + Data Analytics using Python")

st.markdown("""
This project demonstrates how **data analytics and Python** can be applied  
to **vaccine development, safety monitoring, and epidemiological analysis**.
""")

st.divider()

# ---------------- DATA & CONTROLS ----------------
vaccines = ["Vaccine A", "Vaccine B", "Vaccine C"]
efficacy = [92, 85, 78]

events = ["Fever", "Headache", "Fatigue", "Pain"]
counts = [320, 210, 120, 80]

variant_data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Delta": [40, 60, 55, 30, 15, 5],
    "Omicron": [0, 10, 30, 55, 70, 85]
})
variant_data = variant_data.set_index("Month")

# Sidebar controls
st.sidebar.header("Controls")
vaccine_options = ["All"] + vaccines
selected_vaccine = st.sidebar.selectbox("Select vaccine", vaccine_options, index=0)
selected_events = st.sidebar.multiselect("Adverse events to show", events, default=events)
max_days = st.sidebar.slider("Days for immune response plot", min_value=10, max_value=180, value=60)
rate = st.sidebar.slider("Immune response rate (k)", min_value=0.01, max_value=0.2, value=0.07, step=0.01)
selected_variants = st.sidebar.multiselect("Variants to display", list(variant_data.columns), default=list(variant_data.columns))
selected_months = st.sidebar.multiselect("Months to display", list(variant_data.index), default=list(variant_data.index))

st.divider()

# ---------------- SECTION 1 ----------------
st.header("1️⃣ Vaccine Efficacy Analysis")

if selected_vaccine == "All":
    plot_vaccines = vaccines
    plot_efficacy = efficacy
else:
    idx = vaccines.index(selected_vaccine)
    plot_vaccines = [selected_vaccine]
    plot_efficacy = [efficacy[idx]]

fig1, ax1 = plt.subplots()
ax1.bar(plot_vaccines, plot_efficacy, color="tab:blue")
ax1.set_ylabel("Efficacy (%)")
ax1.set_ylim(0, 100)

st.pyplot(fig1)

st.markdown("""
**Interpretation:**  
Selected vaccine efficacy shown above.
""")

st.divider()

# ---------------- SECTION 2 ----------------
st.header("2️⃣ Adverse Event Monitoring")

filtered_events = [e for e in events if e in selected_events]
filtered_counts = [counts[events.index(e)] for e in filtered_events]

fig2, ax2 = plt.subplots()
ax2.bar(filtered_events, filtered_counts, color="tab:orange")
ax2.set_ylabel("Number of Cases")

st.pyplot(fig2)

st.markdown("""
**Interpretation:**  
Filtered adverse events are shown above.
""")

st.divider()

# ---------------- SECTION 3 ----------------
st.header("3️⃣ Immune Response Modeling")

days = np.arange(0, max_days)
antibody = 1 - np.exp(-rate * days)

fig3, ax3 = plt.subplots()
ax3.plot(days, antibody)
ax3.set_xlabel("Days After Vaccination")
ax3.set_ylabel("Antibody Level")

st.pyplot(fig3)

st.markdown("""
**Interpretation:**  
Antibody levels rise rapidly after vaccination and stabilize over time,
indicating effective immune memory.
""")

st.divider()

# ---------------- SECTION 4 ----------------
st.header("4️⃣ Variant Tracking Analytics")

if len(selected_variants) == 0:
    st.info("Select one or more variants in the sidebar to view the chart.")
else:
    months_to_show = selected_months if len(selected_months) > 0 else list(variant_data.index)
    data_to_plot = variant_data.loc[months_to_show, selected_variants]
    st.line_chart(data_to_plot)

st.markdown("""
**Interpretation:**  
Variant frequencies over selected months.
""")

st.divider()

# ---------------- SECTION 5 ----------------
st.header("5️⃣ Key Insights & Conclusion")

st.markdown("""
✅ Python enables real-time vaccine data analysis  
✅ Analytics helps monitor safety and efficacy  
✅ Immune response modeling supports vaccine design  
✅ Variant tracking is critical for public health decisions  

**This project integrates biotechnology with data analytics,
making it highly relevant for modern biotech and AI roles.**
""")

st.success("Project Ready for Portfolio, Resume, and Internship Submission 🚀")
