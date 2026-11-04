
import streamlit as st
from bed_calculations import calculate_bed

# Page configuration
st.set_page_config(
    page_title="Radiotherapy BED Calculator",
    page_icon="🧬",
    layout="centered"
)


# Custom design and typography

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', 'Segoe UI', sans-serif;
}

.stApp {
    background-color: var(--background-color);
}

.block-container {
    max-width: 1050px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

.hero {
    background: linear-gradient(135deg, #101E35, #24445D);
    padding: 2.5rem;
    border-radius: 18px;
    margin-bottom: 2rem;
    color: white;
}

.hero-label {
    color: #A8C7D8;
    font-size: 0.9rem;
    letter-spacing: 2px;
    margin-bottom: 1rem;
}

.hero h1 {
    color: white;
    font-family: 'Inter', sans-serif;
    font-size: 2.8rem;
    line-height: 1.15;
    margin-bottom: 0.5rem;
}

.hero h3 {
    color: #C3D9E5;
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    margin-top: 0;
}

.hero-description {
    color: #E2EAF0;
    font-size: 1.1rem;
    line-height: 1.6;
    margin-top: 1.5rem;
}

h1, h2, h3, p, label {
    font-family: 'Inter', 'Segoe UI', sans-serif;
}

div[data-testid="stSelectbox"] label {
    font-size: 1.15rem;
    font-weight: 600;
    color: var(--text-color);
}

.stButton > button {
    background-color: #142943;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 0.7rem 1.2rem;
    font-size: 1.1rem;
}

.stButton > button:hover {
    background-color: #24445D;
    color: white;
}

/* Comparison option cards */

.st-key-mode_card_1,
.st-key-mode_card_2,
.st-key-mode_card_3 {
    border-radius: 14px;
    padding: 16px;
    min-height: 300px;
    box-sizing: border-box;
    transition: border 0.2s ease;
}

</style>
""", unsafe_allow_html=True)


# Main heading
st.html("""
<div style="
    background: linear-gradient(135deg, #101E35, #24445D);
    padding: 40px;
    border-radius: 18px;
    margin-bottom: 30px;
    color: white;
">

    <p style="
        color: #A8C7D8;
        font-size: 14px;
        letter-spacing: 2px;
        font-weight: 600;
    ">
        RADIOTHERAPY • DOSIMETRY TOOL
    </p>

    <h1 style="
        color: white;
        font-family: 'Inter', sans-serif;
        font-size: 42px;
        font-weight: 700;
        line-height: 1.2;
        margin-bottom: 10px;
    ">
        Radiotherapy BED Calculator
    </h1>

    <h3 style="
        color: #C3D9E5;
        font-family: 'Inter', sans-serif;
        font-weight: 400;
        margin-top: 0;
    ">
        Treatment Comparison Tool
    </h3>



    <p style="
        color: #E2EAF0;
        font-size: 17px;
        line-height: 1.6;
        margin-top: 25px;
    ">
        An educational tool for calculating and comparing
        the Biologically Effective Dose (BED) across different
        radiotherapy treatment schedules and tissues.
    </p>

</div>
""")


# What is BED?
st.subheader("What is BED?")

st.write(
    "The Biologically Effective Dose (BED) is a radiobiological "
    "parameter used in radiotherapy to estimate and compare the "
    "biological effects of different radiation dose-fractionation "
    "schedules. It takes into account the dose per fraction "
    "and the α/β ratio of the tissue."
)

st.markdown("### The BED Formula")

st.latex(
    r"BED = nd\left(1+\frac{d}{\alpha/\beta}\right)"
)

st.caption(
    "n = Number of fractions | "
    "d = Dose per fraction (Gy) | "
    "α/β = Tissue-specific alpha/beta ratio (Gy)"
)


st.divider()



# Comparison mode selection

st.subheader("What do you want to compare?")

if "comparison_mode" not in st.session_state:
    st.session_state["comparison_mode"] = (
        "Compare different treatment schedules for the same tissue"
    )



col1, col2, col3 = st.columns(3)

# Determine which option is selected
selected_mode = st.session_state["comparison_mode"]

mode_1 = "Compare different treatment schedules for the same tissue"
mode_2 = "Compare the same treatment schedule across different tissues"
mode_3 = "Full comparison (different schedules and tissues)"

# Style the comparison cards

st.markdown(f"""
<style>

/* Comparison card styling */

.st-key-mode_card_1,
.st-key-mode_card_2,
.st-key-mode_card_3 {{
    border: 2px solid rgba(128,128,128,0.35);
    border-radius: 14px;
    padding: 18px;
    height: 360px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
}}

.st-key-mode_card_1 {{
    border-color: {'#2A9D8F' if selected_mode == mode_1 else 'rgba(128,128,128,0.35)'};
}}

.st-key-mode_card_2 {{
    border-color: {'#2A9D8F' if selected_mode == mode_2 else 'rgba(128,128,128,0.35)'};
}}

.st-key-mode_card_3 {{
    border-color: {'#2A9D8F' if selected_mode == mode_3 else 'rgba(128,128,128,0.35)'};
}}

.st-key-mode_card_1 h3,
.st-key-mode_card_2 h3,
.st-key-mode_card_3 h3 {{
    color: #2A9D8F;
    font-size: 1.5rem;
    margin-bottom: 18px;
}}

.st-key-mode_card_1 p strong,
.st-key-mode_card_2 p strong,
.st-key-mode_card_3 p strong {{
    font-size: 1.05rem;
    line-height: 1.5;
}}

.st-key-mode_card_1 [data-testid="stCaption"],
.st-key-mode_card_2 [data-testid="stCaption"],
.st-key-mode_card_3 [data-testid="stCaption"] {{
    opacity: 0.8;
}}

</style>
""", unsafe_allow_html=True)



# Option 1
with col1:
    with st.container(key="mode_card_1"):
        st.markdown("### 01")
        st.markdown("**Same Tissue, Different Treatment Schedules**")
        st.caption(
            "Compare different dose-fractionation schedules "
            "for the same tissue."
        )

        if selected_mode == mode_1:
            st.caption("✓ Currently selected")

        if st.button(
            "Select",
            key="select_mode_1",
            type="primary" if selected_mode == mode_1 else "secondary",
            use_container_width=True
        ):
            st.session_state["comparison_mode"] = mode_1
            st.rerun()


# Option 2
with col2:
    with st.container(key="mode_card_2"):
        st.markdown("### 02")
        st.markdown("**Same Treatment Schedule, Different Tissues**")
        st.caption(
            "Compare the biological effect of the same treatment "
            "schedule across different tissues."
        )

        if selected_mode == mode_2:
            st.caption("✓ Currently selected")

        if st.button(
            "Select",
            key="select_mode_2",
            type="primary" if selected_mode == mode_2 else "secondary",
            use_container_width=True
        ):
            st.session_state["comparison_mode"] = mode_2
            st.rerun()


# Option 3
with col3:
    with st.container(key="mode_card_3"):
        st.markdown("### 03")
        st.markdown("**Full Comparison**")
        st.caption(
            "Compare multiple treatment schedules "
            "across multiple tissues."
        )

        if selected_mode == mode_3:
            st.caption("✓ Currently selected")

        if st.button(
            "Select",
            key="select_mode_3",
            type="primary" if selected_mode == mode_3 else "secondary",
            use_container_width=True
        ):
            st.session_state["comparison_mode"] = mode_3
            st.rerun()

mode = st.session_state["comparison_mode"]





if mode == "Compare different treatment schedules for the same tissue":

    st.subheader("Same tissue – different treatment schedules")

    tissue = st.text_input("Enter tissue name:")

    alpha_beta = st.number_input(
        "Alpha/beta ratio (Gy):",
        min_value=0.1,
        value=2.0,
        step=0.1
    )

    number_of_treatments = st.number_input(
        "Number of treatment schedules:",
        min_value=1,
        value=2,
        step=1
    )

    treatment_data = []

    for i in range(int(number_of_treatments)):

        st.write(f"Treatment schedule {i + 1}")

        dose = st.number_input(
            f"Dose per fraction (Gy) – Schedule {i + 1}:",
            min_value=0.1,
            value=2.0,
            step=0.1,
            key=f"dose_{i}"
        )

        fractions = st.number_input(
            f"Number of fractions – Schedule {i + 1}:",
            min_value=1,
            value=25,
            step=1,
            key=f"fractions_{i}"
        )
        treatment_data.append({
            "dose": dose,
            "fractions": fractions
        })
    if st.button("Calculate BED"):

        results = []

        for treatment in treatment_data:

            bed = calculate_bed(
                treatment["dose"],
                treatment["fractions"],
                alpha_beta
            )

            results.append(bed)

        st.subheader("BED Results")

        result_data = []

        for i, bed in enumerate(results):

            result_data.append({
                "Treatment Schedule": f"Schedule {i + 1}",
                "BED (Gy)": round(bed, 2)
            })

        result_data = sorted(
            result_data,
            key=lambda x: x["BED (Gy)"],
            reverse=True
        )

        st.dataframe(
            result_data,
            use_container_width=True,
            hide_index=True
        )

        highest_bed = result_data[0]

        st.success(
            f"Highest BED: {highest_bed['Treatment Schedule']} "
            f"({highest_bed['BED (Gy)']} Gy)"
        )

        chart_data = {
            item["Treatment Schedule"]: item["BED (Gy)"]
            for item in result_data
        }

        st.bar_chart(chart_data)
        
        

elif mode == "Compare the same treatment schedule across different tissues":

    st.subheader("Same treatment schedule – different tissues")

    dose = st.number_input(
        "Dose per fraction (Gy):",
        min_value=0.1,
        value=2.0,
        step=0.1
    )

    fractions = st.number_input(
        "Number of fractions:",
        min_value=1,
        value=25,
        step=1
    )

    number_of_tissues = st.number_input(
        "Number of tissues to compare:",
        min_value=1,
        value=2,
        step=1
    )

    tissue_data = []

    for i in range(int(number_of_tissues)):

        st.write(f"Tissue {i + 1}")

        tissue = st.text_input(
            f"Tissue name – {i + 1}:",
            key=f"tissue_{i}"
        )

        alpha_beta = st.number_input(
            f"Alpha/beta ratio (Gy) – Tissue {i + 1}:",
            min_value=0.1,
            value=10.0,
            step=0.1,
            key=f"ab_{i}"
        )

        tissue_data.append({
            "tissue": tissue,
            "alpha_beta": alpha_beta
        })

    if st.button("Calculate BED", key="calculate_tissues"):

        results = []

        for i, tissue in enumerate(tissue_data):

            bed = calculate_bed(
                dose,
                fractions,
                tissue["alpha_beta"]
            )

            tissue_name = tissue["tissue"].strip()

            if not tissue_name:
                tissue_name = f"Tissue {i + 1}"

            results.append({
                "Tissue": tissue_name,
                "Alpha/beta (Gy)": tissue["alpha_beta"],
                "BED (Gy)": round(bed, 2)
            })

        results = sorted(
            results,
            key=lambda x: x["BED (Gy)"],
            reverse=True
        )

        st.subheader("BED Results")

        st.dataframe(
            results,
            use_container_width=True,
            hide_index=True
        )

        highest_bed = results[0]

        st.success(
            f"Highest BED: {highest_bed['Tissue']} "
            f"({highest_bed['BED (Gy)']} Gy)"
        )

        st.subheader("BED Comparison")

        chart_data = {
            f"{item['Tissue']} (α/β={item['Alpha/beta (Gy)']} Gy)": item["BED (Gy)"]
            for item in results
        }

        st.bar_chart(chart_data)
        

elif mode == "Full comparison (different schedules and tissues)":

    st.subheader("Full comparison – Different schedules and tissues")

    st.write(
        "Compare multiple treatment schedules across different tissues."
    )

    # Number of treatment schedules
    number_of_treatments = st.number_input(
        "Number of treatment schedules:",
        min_value=1,
        value=2,
        step=1,
        key="full_number_treatments"
    )

    treatment_data = []

    for i in range(int(number_of_treatments)):

        st.write(f"Treatment schedule {i + 1}")

        treatment_name = st.text_input(
            f"Treatment schedule name – {i + 1}:",
            value=f"Schedule {i + 1}",
            key=f"full_treatment_name_{i}"
        )

        dose = st.number_input(
            f"Dose per fraction (Gy) – Schedule {i + 1}:",
            min_value=0.1,
            value=2.0,
            step=0.1,
            key=f"full_dose_{i}"
        )

        fractions = st.number_input(
            f"Number of fractions – Schedule {i + 1}:",
            min_value=1,
            value=25,
            step=1,
            key=f"full_fractions_{i}"
        )

        treatment_data.append({
            "name": treatment_name,
            "dose": dose,
            "fractions": fractions
        })

    st.divider()

    # Number of tissues
    number_of_tissues = st.number_input(
        "Number of tissues to compare:",
        min_value=1,
        value=2,
        step=1,
        key="full_number_tissues"
    )

    tissue_data = []

    for i in range(int(number_of_tissues)):

        st.write(f"Tissue {i + 1}")

        tissue_name = st.text_input(
            f"Tissue name – {i + 1}:",
            key=f"full_tissue_name_{i}"
        )

        alpha_beta = st.number_input(
            f"Alpha/beta ratio (Gy) – Tissue {i + 1}:",
            min_value=0.1,
            value=10.0,
            step=0.1,
            key=f"full_alpha_beta_{i}"
        )

        tissue_data.append({
            "name": tissue_name,
            "alpha_beta": alpha_beta
        })

    st.divider()

    # Calculate BED
    if st.button("Calculate BED", key="calculate_full"):

        results = []

        for treatment in treatment_data:

            for tissue in tissue_data:

                bed = calculate_bed(
                    treatment["dose"],
                    treatment["fractions"],
                    tissue["alpha_beta"]
                )

                treatment_name = treatment["name"].strip()
                tissue_name = tissue["name"].strip()

                if not treatment_name:
                    treatment_name = "Unnamed schedule"

                if not tissue_name:
                    tissue_name = "Unnamed tissue"

                results.append({
                    "Treatment schedule": treatment_name,
                    "Tissue": tissue_name,
                    "Dose per fraction (Gy)": treatment["dose"],
                    "Fractions": treatment["fractions"],
                    "Alpha/beta (Gy)": tissue["alpha_beta"],
                    "BED (Gy)": round(bed, 2)
                })

        results = sorted(
            results,
            key=lambda x: x["BED (Gy)"],
            reverse=True
        )

        st.subheader("BED Results")

        st.dataframe(
            results,
            use_container_width=True,
            hide_index=True
        )

        highest_bed = results[0]

        st.success(
            f"Highest BED: {highest_bed['Treatment schedule']} "
            f"– {highest_bed['Tissue']} "
            f"({highest_bed['BED (Gy)']} Gy)"
        )

        st.subheader("BED Comparison")

        chart_data = {
            f"{item['Treatment schedule']} – {item['Tissue']}": item["BED (Gy)"]
            for item in results
        }

        st.bar_chart(chart_data)


# Scientific information and limitations

st.divider()

st.subheader("Scientific Information & Limitations")

st.markdown("""
### About Biologically Effective Dose (BED)

The Biologically Effective Dose (BED) is a radiobiological
quantity based on the Linear-Quadratic (LQ) model. It is used
to estimate and compare the biological effects of different
radiotherapy fractionation schedules, taking into account
the dose per fraction, number of fractions 
and tissue-specific α/β ratio.

The BED concept was introduced in 1989 and has since become
an important tool in radiotherapy research and biological
dose comparison.
""")

st.markdown("""
### Model Assumptions & Limitations

This calculator uses the simplified Linear-Quadratic BED
equation. Its calculations are based on the following
assumptions and limitations:

- Complete repair of sublethal damage between fractions is assumed.
- The calculation does not account for overall treatment time,
  tumour repopulation or dose-rate effects.
- The α/β ratio is tissue-dependent, and its value may be
  uncertain for some tissues and clinical situations.
- BED does not account for spatial dose distribution,
  irradiated volume, dose heterogeneity or individual
  patient and tumour characteristics.
- The validity of the standard LQ model at very high
  doses per fraction (approximately above 8–10 Gy) remains
  debated. Additional biological effects, such as vascular
  damage and immune responses, may not be fully represented
  by the simplified model.
""")

st.markdown("""
### Educational Use Disclaimer

This application is intended for educational and research
purposes only. It is not intended for clinical decision-making,
treatment prescription or patient management.

The calculated BED values are theoretical estimates based
on a simplified radiobiological model. They should not be
interpreted as clinical recommendations or used as a substitute
for professional judgment.

Users are responsible for verifying all input values and
results. Clinical decisions must always be made by qualified
healthcare professionals using appropriate clinical and
dosimetric information.
""")

with st.expander("Scientific References"):

    st.markdown("""
    1. **International Atomic Energy Agency (IAEA).**
       Radiation Oncology Physics: A Handbook for Teachers
       and Students. Vienna: IAEA; 2005.
       [Access the book](https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1196_web.pdf)

    2. **Hall EJ, Giaccia AJ.**
       Radiobiology for the Radiologist. 7th ed.
       Philadelphia: Lippincott Williams & Wilkins; 2012.
       [Access the book](https://eprints.poltekkesadisutjipto.ac.id/id/eprint/2055/1/Radiobiology-for-the-Radiologist.pdf)

    3. **Fowler JF.**
       21 years of Biologically Effective Dose.
       Br J Radiol. 2010;83(991):554–568.
       [Read the article](https://pmc.ncbi.nlm.nih.gov/articles/PMC3473681/)

    4. **Biologically Effective Dose and Dose Rate in Gamma Knife Radiosurgery for Trigeminal Neuralgia: A Systematic Review and Meta-Analysis.**
       [Read the article](https://www.sciencedirect.com/science/article/pii/S2452109425002192)

    5. **MIM Software.**
       BED and Tumor Control Probability Modeling.
       [Access the white paper](https://www.mimsoftware.com.cn/manager/templates/mimsoftware/resources/whitepapers/BED_and_Tumor_Control_Probability_Modeling.pdf)

    6. **Kirkpatrick JP, Meyer JJ, Marks LB.**
       The linear-quadratic model is inappropriate to model
       high dose per fraction effects in radiosurgery.
       Semin Radiat Oncol. 2008;18(4):240–243.
       [Read the article](https://doi.org/10.1016/j.semradonc.2008.04.005)

    7. **Zheng D, et al.**
       Mathematical modeling in radiotherapy for cancer:
       a comprehensive narrative review.
       Radiat Oncol. 2025;20:49.
       [Read the article](https://doi.org/10.1186/s13014-025-02626-7)
    """)
