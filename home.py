import streamlit as st 
import streamlit.components.v1 as components
# import calendar
# from version import VERSION

# from util import img_to_bytes

with st.container():
    
    tritri_form = st.form('tritri')
    total = tritri_form.text_input("Total Tricount (€)")
    difference5050 = tritri_form.text_input("Avance Fanny en répartition 50/50 (€)")

    submitted = tritri_form.form_submit_button("Calcul")
    if submitted:

        if total=="":
            st.stop()
        if "," in total:
            total = total.replace(",", ".")
            
        try:
            total = float(total)
        except:
            st.stop()

        if difference5050=="":
            st.stop()
        if "," in difference5050:
            difference5050 = difference5050.replace(",", ".")
        try:
            difference5050 = float(difference5050)
        except:
            st.stop()

        mc_60pc = 60/100*total
        fg_60pc = 40/100*total
        mc = total/2 - difference5050
        fg = total/2 + difference5050
        mc2fg_60pc = round(mc_60pc - mc,2)
        
        tritri_form.markdown("---")
        if mc2fg_60pc >= 0:
            tritri_form.info('Michel doit ' + str(mc2fg_60pc) + '€ à Fanny (Répartition 60/40)')
        else:
            tritri_form.info('Fanny doit ' + str(abs(mc2fg_60pc)) + '€ à Michel (Répartition 60/40)')
        
        tritri_form.text("Détails pour une répartition 60/40 d'un total de " + str(total) + "€ :")
        tritri_form.text(('- Fanny a payé ' + str(round(fg, 2)) + '€ sur ' + str(round(fg_60pc, 2)) + '€ dus'))
        tritri_form.text(('- Michel a payé ' + str(round(mc, 2)) + '€ sur ' + str(round(mc_60pc, 2)) + '€ dus'))
