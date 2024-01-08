#modules
import streamlit as st


#functions from other files
import functions.gptapi as gptapi
import functions.gptapi as gptapi
#import functions.bigquery as bq

#main part of tnd tab
def tnd():
    st.title("Title Tag Generator")
    st.markdown("<h4>Instructions:</h4>", unsafe_allow_html=True)
    st.markdown("""<ul>
                <li>Select industry.</li>
                <li>Depending on the selected industry, further selection options are now available.</li>
                <li>"Hub" as Job Detail stands for: No specific job detail is generated in title / description / h1 tag.</li>
                <li>Select the desired language output.</li>
                <li>Click on the button "Generate Title and Description Tag" to generate the respective tags via GPT.</li>
               </ul>""", unsafe_allow_html=True)

    ### hier folgen die Input Felder
    st.divider()
    st.markdown("### Provide information")

    col1_generic_info, col2_generic_info = st.columns(2)
    with col1_generic_info:
        industry_choosen = st.selectbox("Choose industry", ["Cleaning", "Construction", "Electrician", "Hospitality", "Machinist", "Mechanical Engineering", "Solar", "Tourism", "Truck Driver", "Warehouse", "Welding"])
        if industry_choosen == "Cleaning":
            job_detail_choosen = st.selectbox("Choose Job Detail", ["Hub", "Housekeeping"])
        elif industry_choosen == "Construction":
            job_detail_choosen = st.selectbox("Choose Job Detail", ["Hub", "Bricklayer", "Machine Operator", "Excavator Operator", "Civil Engineer", "Carpenter", "Painting", "Plumbing"])
        elif industry_choosen == "Electrician":
            job_detail_choosen = st.selectbox("Choose Job Detail", ["Hub", "Engineer"])
        elif industry_choosen == "Hospitality":
            job_detail_choosen = st.selectbox("Choose Job Detail", ["Hub", "Chef", "Waiter", "Restaurant", "Bar", "Barista", "Food Delivery"])
        elif industry_choosen == "Machinist":
            job_detail_choosen = st.selectbox("Choose Job Detail", ["Hub"])
        elif industry_choosen == "Mechanical Engineering":
            job_detail_choosen = st.selectbox("Choose Job Detail", ["Hub", "Manufacturing Engineer", "Production Engineer", "Robots Engineer", "Materials Engineer", "Aerospace", "Automotive", "Mechatronics"])
        elif industry_choosen == "Solar":
            job_detail_choosen = st.selectbox("Choose Job Detail", ["Hub"])
        elif industry_choosen == "Tourism":
            job_detail_choosen = st.selectbox("Choose Job Detail", ["Hub", "Flight Attendant", "Tour Guide", "Travel Agent", "Spa Therapist", "Restaurant Manager"])
        elif industry_choosen == "Truck Driver":
            job_detail_choosen = st.selectbox("Choose Job Detail", ["Hub"])
        elif industry_choosen == "Warehouse":
            job_detail_choosen = st.selectbox("Choose Job Detail", ["Hub", "Forklift", "Logistics"])
        elif industry_choosen == "Welding":
            job_detail_choosen = st.selectbox("Choose Job Detail", ["Hub", "Inspector", "Engineer"])




    with col2_generic_info:
        location_wanted = st.text_input("Provide city of work")
        lang_wanted = st.selectbox("Choose language", ["English", "German", "Croatian"])
      
    if st.button("Generate now"):
        if job_detail_choosen == "Hub":
            job_detail_choosen = ""
        #gpt prompts
        act_as_prompt_title = "You are a SEO specialist, working as a recruiter. Its your job to attract english-speaking employees to work and live in germany. "
        content_prompt_title = f"Write a SEO title tag for the job as a {job_detail_choosen} in {industry_choosen}. Must include {job_detail_choosen}. Always start with: 'Job in Germany'. The Job is located in Germany {location_wanted}. Write in {lang_wanted}."
        #generate title tag
        title_tag_generated, title_tag_generated_cost = gptapi.openAI_content(act_as_prompt_title, content_prompt_title)
    
        st.divider()
        st.markdown(f"""<h4>Title Tag for {industry_choosen}-Job in {location_wanted} / Germany</h4>
                        <ul>
                        <li><b>Title Tag:</b> {title_tag_generated}</li>
                        <li><b>Industry choosen:</b> {industry_choosen}</li>
                        <li><b>Job Detail Choosen:</b> {job_detail_choosen}</li>
                        <li><b>Cost:</b> {title_tag_generated_cost} EUR</li>
                        </ul>
        
                        """, unsafe_allow_html=True)
        st.divider()

            #####################
        total_cost_tnd = (
                title_tag_generated_cost
        )
        total_cost_tnd = round(total_cost_tnd, 5)

    #bq.to_bigquery("TND Generator", total_cost_tnd, focus_keyword_input, additional_usage_information, lang_wanted)

    
