import streamlit as st

def sidebar():
    st.image("https://static.wixstatic.com/media/864b24_5bcde7e8595a49aba5e790e514053534~mv2.png/v1/fill/w_335,h_87,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Hello-Jobs-Logo-noClaim-schwarz-weiss-ws.png")
    st.title("Google for Jobs Process Optimization")

    st.markdown("<p>Welcome to the Hello Jobs 'Goole for Jobs Process Optimization'-Tool.</p>", unsafe_allow_html=True)
    st.markdown("<h3>General information:</h3>", unsafe_allow_html=True)
    st.markdown("""<ul>
                <li>In order to improve "Google for Jobs" performance we want to make sure Google actually crawls every job published on a regular basis.</li>
                <li>We also need to make sure that all title tags for the jobs are following the best practise pattern for Google for Jobs. For this case we are using a custom trained GPT3.5-Model.</li>
                <li>Copy&Pasting the Job URL and Pressing "Index now"-Button pings Google & Bing for a Crawl. This adds the Job URL to the Crawling Queue.</li>
                </ul>""", unsafe_allow_html=True)
    
    st.divider()
    st.markdown("<h3>Contact</h3><p>If you have any questions, requests or comments, please contact Paul:</p><ul><li><a href='mailto:seo@paulherzog.at'>E-Mail</a></li>", unsafe_allow_html=True)
    st.divider()
