#========================================================================
# Import packages

import streamlit as st

from PIL import Image
#%matplotlib inline

from joblib import dump, load
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import make_pipeline

#import matplotlib.pyplot as plt
#import tkinter as tk
#==> Use tex font
# plt.rc('text', usetex=True)
# plt.rc('font', family='serif')

st.set_page_config(page_title= "Développement d'aplication mobile/web", page_icon= ":tada:", layout= "wide" )

# header setting


st.title("Développement d'aplication mobile/web")
# st.subheader("Projet de fin de formation en MLOPs")

#================================================================================
#import base64

#st.markdown("![Alt Text](https://media3.giphy.com/media/WlUlR0GdKlr5F3JKBd/giphy.gif?cid=ecf05e4738lqascq7f2w76pp8fquwjtc3ms6p4uybmf43ojr&rid=giphy.gif&ct=g)")

#================================================================================

#import streamlit as st

def main():

    content_options = ["Contexte et objectifs du projet", "Outils numériques envisageables", "Déploiement",
                       "Copyrights"]
    choice = st.sidebar.radio("Sommaire", content_options)

    #================================================================================
    if choice == "Contexte et objectifs du projet":
        
        st.write("## Contexte du projet:")
        st.write("- Nombreuses sont les personnes s'intéressant aux activités sportives")
        st.write("- Les activités sportives sont diverses et variées")
        st.write("- Trouver un cadre pouvant rapprocher les amateurs sportifs relativement aux disciplines qu'ils pratiquent peut s'avérer intéressant ")
        
        st.write()
        st.write("## Objectifs du projet:")
        st.write("1 - Développer une application pouvant servir de plateforme pouvant unir des amateurs du sport pratiquant la même discipline;")
        st.write("2 - L'application doit être opérationnel sur Smartphone mais aussi sur des machines comme un ordinateur")
        st.write("3 - ...")
 
    #================================================================================
    elif choice == "Outils numériques envisageables":
        st.write("## Outils numériques envisageables")
        
        
        # Création d'une session state pour suivre quelles images doivent être affichées
        if 'show_backend' not in st.session_state:
            st.session_state['show_backend'] = False

        def toggle_backend():
            st.session_state['show_backend'] = not st.session_state['show_backend']

        # Création des boutons et association avec les fonctions
        st.button("Backend", on_click=toggle_backend, type = "primary")

        # Affichage des images en fonction de l'état des boutons
        if st.session_state['show_backend']:
            st.write("- Machine Linux (de péférence) ou mac")
            st.write("- Langage de programmation: pytho/Dart")
            st.write("- Principales librairies/ à utiliser: Flet/Flutter (mobile), Django (web): une préférence de flutter est plus probable")
            st.write("- Base de données SQL.")
            st.write("- Android Studio / Xcode pour effectuer des tests de fonction sur des émulateurs.")

        # --------------------------------

        if 'show_frontend' not in st.session_state:
            st.session_state['show_frontend'] = False
            
        def toggle_frontend():
            st.session_state['show_frontend'] = not st.session_state['show_frontend']
            
        st.button("Frontend", on_click=toggle_frontend, type = "primary")

        if st.session_state['show_frontend']:
            st.write("JavaScript, React, CSS, HTML.")
    
        
    #================================================================================

    elif choice == "Déploiement":
        st.write("## Déploiement")
        
        if 'show_mobile' not in st.session_state:
            st.session_state['show_mobile'] = False
            
        def toggle_mobile():
            st.session_state['show_mobile'] = not st.session_state['show_mobile']
            
        st.button("Service mobile", on_click=toggle_mobile, type = "primary")

        if st.session_state['show_mobile']:
            # st.write("- Docker")
            st.write("- Un compte Google play Store")
        
        # ------------------------------------------
        
        if 'show_containers' not in st.session_state:
            st.session_state['show_containers'] = False
            
        def toggle_container():
            st.session_state['show_containers'] = not st.session_state['show_containers']
            
        st.button("Conteneurisation / orchestration (fonctionnement sur web)", on_click=toggle_container, type = "primary")

        if st.session_state['show_containers']:
            st.write("- Docker")
            st.write("- Un compte DockerHub")
            st.write("- Kubernetes")
        
        # ------------------------------------------

        
        if 'show_serveur' not in st.session_state:
            st.session_state['show_serveur'] = False
            
        def toggle_serveur():
            st.session_state['show_serveur'] = not st.session_state['show_serveur']
            
        st.button("Serveurs/Cloud (fonctionnement sur web)", on_click=toggle_serveur, type = "primary")

        if st.session_state['show_serveur']:
            st.write("- Serveur Linux")
            st.write("- Github")
            st.write("- AWS")
        
    
    
    #================================================================================
    elif choice == "Copyrights":
        #image = Image.open('customerstatisfaction.jpg')
        #st.image(image, caption='')
        st.write("## Directeurs du projets")
        st.write("- Arjeka [learn more >] (https://www.arjeka.com/)")
        st.write("- Arthur Hamer [learn more >] (...)")
        
        st.write()
        st.write("## Développeur informatique")
        st.write("- Esso-passi PALI [learn more >] (https://github.com/eppali)")
        



if __name__ == "__main__":
    main()

#================================================================================
#================================================================================
