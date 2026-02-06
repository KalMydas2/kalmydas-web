import streamlit as st
import requests
from datetime import datetime

# ==============================================================================
# --- ⚙️ CONFIGURATION ---
# ==============================================================================
# ⚠️ Remplace par ton Token et tes ID (Je remets les tiens ici pour faciliter le copier-coller)
TOKEN = "8529579275:AAF7jJgdaty9Ewp4KnmtHyOS5DUQgvrx0Jc"
SUPPORT_CHAT_ID = "-5279762957"
CHANNEL_URL = "https://t.me/Kalmydas"
MY_CONTACT_LINK = "https://t.me/Kal_mydas"

# --- LIENS BROKERS ---
LINK_BROKER_FR_1 = "https://ma.valetax.com/p/3522435"
LINK_BROKER_FR_2 = "https://fusionmarkets.com/?refcode=108479"
LINK_BROKER_WORLD_1 = "https://one.justmarkets.link/a/aispz02jbv"
LINK_BROKER_WORLD_2 = "https://ma.valetax.com/p/3522435"
LINK_BROKER_WORLD_3 = "https://fusionmarkets.com/?refcode=108479"

# --- LIENS DRIVE ---
# Horizon
DRIVE_HORIZON_DOSSIER = "https://drive.google.com/drive/folders/1d3Gk5tkQB7sBAj_M_PfbFuXxM0TKsi0v?usp=sharing"
DRIVE_HORIZON_INSTALL = "https://drive.google.com/file/d/1NkRzpIRY643wzWkAuY0EIz_c8-WdgpWD/view?usp=sharing"
DRIVE_HORIZON_EXE     = "https://drive.google.com/file/d/1BSUZJ92MDdubnZeUntd6XK2aiK73oTxQ/view?usp=sharing"
# Valkyrie
DRIVE_VALKYRIE_DOSSIER = "https://drive.google.com/drive/folders/1d3Gk5tkQB7sBAj_M_PfbFuXxM0TKsi0v?usp=sharing"
DRIVE_VALKYRIE_INSTALL = "https://drive.google.com/file/d/1NkRzpIRY643wzWkAuY0EIz_c8-WdgpWD/view?usp=sharing"
DRIVE_VALKYRIE_EXE     = "https://drive.google.com/file/d/1BSUZJ92MDdubnZeUntd6XK2aiK73oTxQ/view?usp=sharing"

# ==============================================================================
# --- 🔧 FONCTIONS UTILES ---
# ==============================================================================
def send_telegram_notification(message):
    """Envoie le rapport directement sur ton groupe Telegram"""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": SUPPORT_CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, json=payload)
        return response.status_code == 200
    except:
        return False

# ==============================================================================
# --- 🖥️ INTERFACE WEB STREAMLIT ---
# ==============================================================================
st.set_page_config(page_title="Kal Mydas - Inscription", page_icon="🏛️")

# En-tête
st.title("🏛️ BIENVENUE CHEZ KAL MYDAS")
st.caption("*(Propulsé par l'IA Kairos)*")
st.markdown("---")

# --- 1. PROFIL & IDENTITÉ ---
st.header("1. Profil & Identité")

col1, col2 = st.columns(2)
with col1:
    profil = st.radio("Votre Niveau", ["Débutant (Guidez-moi)", "Expert (Direct)"])
with col2:
    pays = st.selectbox("Votre Pays", ["France", "Autre Pays"])

tiktok = st.text_input("Votre Nom sur TikTok", placeholder="@votre_pseudo")
# Ici on demande un contact général (Email ou Telegram) car le client n'a pas forcément Telegram
contact = st.text_input("Votre Contact (Telegram ou Email)", placeholder="@pseudo ou email@gmail.com")

# --- 2. MODE & OFFRES ---
st.header("2. Type de Compte")

mode_compte = st.radio("Quel est votre objectif ?", ["Compte RÉEL (Gains Réels)", "Compte DÉMO (Gratuit)"])

offre_choisie = "GRATUIT"
broker_name_manual = "" # Variable pour stocker le nom du broker

if mode_compte == "Compte RÉEL (Gains Réels)":
    st.info("💎 **CHOISISSEZ VOTRE LICENCE**")
    type_offre = st.radio("Offre", ["🤝 PARTENAIRE (10€/mois)", "🦅 LIBERTÉ (15€/mois)"])
    
    if type_offre == "🦅 LIBERTÉ (15€/mois)":
        offre_choisie = "LIBERTÉ (15€)"
        # Si Liberté, on ne propose pas de liens, mais on demandera le nom à la fin si pas Sérénité
    else:
        offre_choisie = "PARTENAIRE (10€)"
        st.write("🔽 **Ouvrez votre compte via nos partenaires :**")
        if pays == "France":
            st.markdown(f"👉 [Ouvrir Compte Broker 1]({LINK_BROKER_FR_1})")
            st.markdown(f"👉 [Ouvrir Compte Broker 2]({LINK_BROKER_FR_2})")
        else:
            st.markdown(f"👉 [Ouvrir Compte Broker 1]({LINK_BROKER_WORLD_1})")
            st.markdown(f"👉 [Ouvrir Compte Broker 2]({LINK_BROKER_WORLD_2})")
            st.markdown(f"👉 [Ouvrir Compte Broker 3]({LINK_BROKER_WORLD_3})")
        st.success("✅ Cochez la case ci-dessous une fois votre compte créé.")
        st.checkbox("J'ai créé mon compte broker")
else:
    offre_choisie = "GRATUIT (Démo)"
    broker_name_manual = "COMPTE DÉMO"

# --- 3. CAPITAL & ROBOT ---
st.header("3. Capital & Robot")

capital = st.select_slider("Quel capital allez-vous utiliser ?", options=["0 - 5.000€", "+ 5.000€"])
if profil == "Débutant (Guidez-moi)":
    st.caption("ℹ️ En dessous de 5000€, nous activons la sécurité micro-lots.")

robot_choix = st.selectbox("Choisissez votre Robot", ["KalMydas HORIZON (Stable)", "KalMydas VALKYRIE (Performance)"])

# --- 4. OPTION SÉRÉNITÉ ---
st.header("4. Option Sérénité (Hébergement)")

serenite_active = "NON"
login_mt = ""
mdp_mt = ""
serveur_mt = ""
broker_final = "" # Ce sera le broker envoyé au support
plateforme = "MT4"

is_demo = (mode_compte == "Compte DÉMO (Gratuit)")
prix_serenite = "OFFERT (Démo)" if is_demo else "10€/mois"

choix_serenite = st.radio(f"Voulez-vous que Kal Mydas héberge votre compte ? (Coût: {prix_serenite})", ["OUI (Hébergement)", "NON (Je gère seul)"])

if choix_serenite == "OUI (Hébergement)":
    serenite_active = "OUI"
    st.warning("🔒 **ZONE SÉCURISÉE (Hébergement)**")
    plateforme = st.selectbox("Plateforme", ["MT4", "MT5"])
    login_mt = st.text_input("1️⃣ Numéro de Compte (Login)")
    mdp_mt = st.text_input("2️⃣ Mot de Passe de Trading", type="password", help="Données cryptées")
    serveur_mt = st.text_input("3️⃣ Nom EXACT du Serveur", placeholder="ex: PUPrime-Live2")
    # Si Sérénité, le serveur suffit à identifier le broker
    broker_final = "Voir Serveur"

else:
    # SI SÉRÉNITÉ NON
    serenite_active = "NON"
    st.info("💻 Vous gérez l'installation vous-même.")
    
    # On demande quand même Login/Plateforme pour la licence
    plateforme = st.selectbox("Plateforme pour la licence", ["MT4", "MT5"])
    login_mt = st.text_input("1️⃣ Numéro de Compte (Login) - Requis pour la licence")
    
    mdp_mt = "NON REQUIS (Client gère)"
    serveur_mt = "NON REQUIS (Client gère)"
    
    # LOGIQUE AIGUILLAGE V15 :
    # Si Réel + Sérénité NON -> On demande le nom du broker
    if not is_demo:
        broker_final = st.text_input("🏦 Nom de votre Broker", placeholder="ex: Vantage, PUPrime...")
    else:
        broker_final = "COMPTE DÉMO"

# --- 5. VALIDATION ---
st.markdown("---")
submit = st.button("🚀 VALIDER MON INSCRIPTION")

if submit:
    # Vérification des champs obligatoires
    if not tiktok or not contact:
        st.error("⚠️ Merci de remplir votre Nom TikTok et votre Contact.")
    elif not login_mt:
        st.error("⚠️ Le Numéro de Compte (Login) est obligatoire pour la licence.")
    elif serenite_active == "OUI" and (not mdp_mt or not serveur_mt):
        st.error("⚠️ Pour l'hébergement, le Mot de Passe et le Serveur sont obligatoires.")
    else:
        # TOUT EST OK -> ON ENVOIE
        
        # Choix des liens
        if "HORIZON" in robot_choix:
            lnk_dossier = DRIVE_HORIZON_DOSSIER
            lnk_install = DRIVE_HORIZON_INSTALL
            lnk_exe = DRIVE_HORIZON_EXE
            short_robot = "HORIZON"
        else:
            lnk_dossier = DRIVE_VALKYRIE_DOSSIER
            lnk_install = DRIVE_VALKYRIE_INSTALL
            lnk_exe = DRIVE_VALKYRIE_EXE
            short_robot = "VALKYRIE"

        # Construction du message Telegram pour TOI
        titre_lead = "🟢 NOUVEAU LEAD WEB (DÉMO)" if is_demo else "🔴 NOUVEAU CLIENT WEB (RÉEL)"
        
        msg_support = f"""
🔥 <b>{titre_lead}</b> 🔥
➖➖➖➖➖➖➖➖➖➖
📅 {datetime.now().strftime("%d/%m/%Y %H:%M")}
👤 <b>TikTok:</b> {tiktok}
📧 <b>Contact:</b> {contact}
🌍 <b>Pays:</b> {pays}
➖➖➖➖➖➖➖➖➖➖
💎 <b>Offre:</b> {offre_choisie}
🏦 <b>Broker:</b> {broker_final}
🤖 <b>Robot:</b> {short_robot}
💰 <b>Capital:</b> {capital}
🛡️ <b>Sérénité:</b> {serenite_active}
➖➖➖➖➖➖➖➖➖➖
🔐 <b>INFOS TECHNIQUES :</b>
Plateforme: {plateforme}
1️⃣ Login: <code>{login_mt}</code>
2️⃣ Mdp: <code>{mdp_mt}</code>
3️⃣ Serveur: <code>{serveur_mt}</code>
➖➖➖➖➖➖➖➖➖➖
        """
        
        # Envoi
        success = send_telegram_notification(msg_support)
        
        if success:
            st.success("✅ INSCRIPTION VALIDÉE !")
            st.balloons()
            
            st.markdown(f"""
            ### 🎉 Félicitations !
            L'algorithme **{short_robot}** vous est attribué.
            
            **📂 VOS TÉLÉCHARGEMENTS :**
            * [📥 Télécharger le Dossier Complet]({lnk_dossier})
            * [🛠️ Guide d'Installation]({lnk_install})
            * [🤖 Fichier du Robot (.ex4/.ex5)]({lnk_exe})
            
            ---
            **🔔 IMPORTANT :**
            Si vous n'avez pas Telegram, surveillez vos Emails/SMS (selon le contact fourni).
            Si vous avez Telegram, rejoignez le canal : {CHANNEL_URL}
            """)
        else:
            st.error("Oups, une erreur de connexion est survenue. Veuillez réessayer.")