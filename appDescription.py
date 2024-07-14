#========================================================================
# Import packages

import streamlit as st

from PIL import Image
#%matplotlib inline


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
                       "Principales étapes  et chronologie","Copyrights"]
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
            st.write("- Machine Linux (de péférence) ou Mac")
            st.write("- Langage de programmation: python/Dart")
            st.write("- Principales librairies/ à utiliser: Flet/Flutter (préférence pour flutter)")
            st.write("- Base de données SQL.")
            st.write("- Android Studio / Xcode pour effectuer des tests de fonctionnement sur des émulateurs.")

        # --------------------------------

        if 'show_frontend' not in st.session_state:
            st.session_state['show_frontend'] = False
            
        def toggle_frontend():
            st.session_state['show_frontend'] = not st.session_state['show_frontend']
            
        st.button("Frontend", on_click=toggle_frontend, type = "primary")

        if st.session_state['show_frontend']:
            st.write("JavaScript, Bootstrap, CSS, HTML.")
    
        
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
            st.write("- Un compte Google play Store (utilisation sur android)")
            st.write("- Un compte app Store (utilisation sur iPhone)")
        
        # ------------------------------------------
        
        if 'show_containers' not in st.session_state:
            st.session_state['show_containers'] = False
            
        def toggle_container():
            st.session_state['show_containers'] = not st.session_state['show_containers']
            
        st.button("Conteneurisation / orchestration (fonctionnement sur web)", on_click=toggle_container, type = "primary")

        if st.session_state['show_containers']:
            st.write("- Docker")
            st.write("- Un compte DockerHub")
            st.write("- Kubernetes (optionnel)")
        
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
            
        # ------------------------------------------

        
        if 'show_besoin' not in st.session_state:
            st.session_state['show_besoin'] = False
            
        def toggle_serveur():
            st.session_state['show_besoin'] = not st.session_state['show_besoin']
            
        st.button("Besoin d'informations", on_click=toggle_serveur, type = "primary")

        if st.session_state['show_besoin']:
            st.write("- Nom de l'application")
            st.write("- Logo")
            st.write("- Conditions d'utilisation de l'application")
            st.write("- Cahier des charges, ...")
        
    
    elif choice == "Principales étapes  et chronologie":
        st.write("## Principales étapes  et chronologie")
        
        # ------------------------------------------------------
        
        if 'show_authentication' not in st.session_state:
            st.session_state['show_authentication'] = False
            
        def toggle_authentication():
            st.session_state['show_authentication'] = not st.session_state['show_authentication']
            
        st.button("Authentification (2 semaines)", on_click=toggle_authentication, type = "primary")

        if st.session_state['show_authentication']:
            # st.write("- Docker")
            st.write("- Page d'accueil ")
            st.write("- Création d'un nouveau compte")
            st.write("- Connexion")
            st.write("- Création d'un nouveau compte")
            
    
        # ------------------------------------------------------
        
        if 'show_authorization' not in st.session_state:
            st.session_state['show_authorization'] = False
            
        def toggle_authentication():
            st.session_state['show_authorization'] = not st.session_state['show_authorization']
            
        st.button("Base de données, autorisation et gestion de compte (4 semaines)", on_click=toggle_authentication, type = "primary")

        if st.session_state['show_authorization']:
            st.write("- Bases de données")
            st.write("- Vérirication / Existence / création d'un nouveau compte")
            st.write("- Vérirication / Existence/ autorisation de connexion ")
            st.write("- Cryptage des informations de connexion")
            st.write("- Récupération de compte (réinitialisation)")  
            st.write("- Suppression un compte, ...")
            st.write("- Informations de confidentialité et CGU")
            
        # # ------------------------------------------------------
        
        # if 'show_database' not in st.session_state:
        #     st.session_state['show_database'] = False
            
        # def toggle_authentication():
        #     st.session_state['show_database'] = not st.session_state['show_database']
            
        # st.button("Base de données et mise en page de profils (4 semaines)", on_click=toggle_authentication, type = "primary")

        # if st.session_state['show_database']:
            
        #     st.write("- Mise en page de profils (format profil, informations et actions à faire, ...)")
            
  
            
        # ------------------------------------------------------

        if 'show_discipline_animations' not in st.session_state:
            st.session_state['show_discipline_animations'] = False
            
        def toggle_discipline_animations():
            st.session_state['show_discipline_animations'] = not st.session_state['show_discipline_animations']
            
        st.button("Intégration de différentes disciplines sportives et design (3 semaines)", on_click=toggle_discipline_animations, type = "primary")

        if st.session_state['show_discipline_animations']:
            st.write("- Intégrations des disciplines sportives (avec une désignation image)")
            st.write("- Animations de pages ")
            st.write("- Mise en page de profils (format profil, informations et actions à faire, ...)")
            
            
        # ------------------------------------------------------

        if 'show_localisation' not in st.session_state:
            st.session_state['show_localisation'] = False
            
        def toggle_localisation():
            st.session_state['show_localisation'] = not st.session_state['show_localisation']
            
        st.button("Intégration des localisations (3 semaines)", on_click=toggle_localisation, type = "primary")

        if st.session_state['show_localisation']:
            st.write("- Pays")
            st.write("- Départements")
            st.write("- Ville")
            
            
        # ------------------------------------------------------

        if 'show_partenaires' not in st.session_state:
            st.session_state['show_partenaires'] = False
            
        def toggle_localisation():
            st.session_state['show_partenaires'] = not st.session_state['show_partenaires']
            
        st.button("Utilisateurs et correspondance (3 semaines)", on_click=toggle_localisation, type = "primary")

        if st.session_state['show_partenaires']:
            st.write("- Par rapport à la localisation")
            st.write("- Par rapport au genre")
            st.write("- Par rapport aux disciplines sportives")
            
        # ------------------------------------------------------

        if 'show_deployment' not in st.session_state:
            st.session_state['show_deployment'] = False
            
        def toggle_deployment():
            st.session_state['show_deployment'] = not st.session_state['show_deployment']
            
        st.button("Déployement (4 semaines)", on_click=toggle_deployment, type = "primary")

        if st.session_state['show_deployment']:
            st.write("- Sur Google play store")
            st.write("- Sur app store")
            st.write("- Github")

        # ------------------------------------------------------

        if 'show_synthese' not in st.session_state:
            st.session_state['show_synthese'] = False
            
        def toggle_synthese():
            st.session_state['show_synthese'] = not st.session_state['show_synthese']
            
        st.button("Synthèse chronologique prévisionnelle:", on_click=toggle_synthese, type = "primary")

        if st.session_state['show_synthese']:
            st.write("- Durée totale estimative: 19 semaines soit environs 5 mois")
            st.write("- NB: un jour d'effort de travail par semaine !")
    
    #================================================================================
    elif choice == "Copyrights":
        #image = Image.open('customerstatisfaction.jpg')
        #st.image(image, caption='')
        st.write("## Directeurs du projets")
        st.write("- Arjeka [learn more >] (https://www.arjeka.com/)")
        st.write("- Arthur HAMER [learn more >] (...)")
        st.write("- Anthony GASIOREK [learn more >] (...)")
        
        st.write()
        st.write("## Développeur informatique")
        st.write("- Esso-passi PALI [learn more >] (https://github.com/eppali)")
        



if __name__ == "__main__":
    main()

#================================================================================
#================================================================================
