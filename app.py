import streamlit as st
import json
import os
from datetime import datetime

# ==============================================================================
# --- ⚙️ CONFIGURATION ---
# ==============================================================================

# CHEMIN VERS L'INBOX DU BOT (Relatif ou Absolu)
# Ici, tout est dans le même dossier ANTIGRAVITY
INBOX_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inbox")

# --- DOCUMENTS LEGAUX ---
LEGAL_DOC_URL = "https://drive.google.com/file/d/1dShUwZXykqVJS7skSFw1CXKBlfc355FV/view"  # Conditions Générales
LICENSE_DOC_URL = "https://drive.google.com/file/d/1GbC-pWwiop-CGq6WohI5mxaYLoBJZ-x2/view"  # Licence / Attestation

# --- LIENS TELECHARGEMENT (Même structure que KAIROS4.py) ---
DRIVE_ROBOTS = {
    "HORIZON": {
        "Réel": {
            "MT4": {
                "folder": "https://drive.google.com/drive/folders/12wfcsgungGjdPoZevjSw8_3GFwQAmZmI?usp=sharing",
                "installer": "https://drive.google.com/file/d/1D-ih1c1kGqgQbKsbk9wdaCVWrrlRjrCr/view?usp=sharing",
                "exe": "https://drive.google.com/drive/folders/1CiOZGqz9E9pB5OMbN4kNWVlHMNdiX2Le?usp=sharing"
            },
            "MT5": {
                "folder": "https://drive.google.com/drive/folders/1p_gMdu4h8YwtEnuHxdaL6U3KuDVbVKDW?usp=sharing",
                "installer": "https://drive.google.com/file/d/1w5ATihZ8DKStj3S0NK5EeYR0vWnflUNq/view?usp=sharing",
                "exe": "https://drive.google.com/drive/folders/10KS2npIaOa8qapte5h69dCCF7dyYh1fl?usp=sharing"
            }
        },
        "Démo": {
             "MT4": {
                "folder": "https://drive.google.com/drive/folders/1tS6Xpln8IcbndTeJIKtngHStZgLE8ao2?usp=sharing",
                "installer": "https://drive.google.com/file/d/1mGnjhmwQjMKhw104ywLcbjG580Tbd9fz/view?usp=sharing",
                "exe": "https://drive.google.com/drive/folders/1ogeQ3mzK17WVAAkzMv0AipPHXC1VhVoy?usp=sharing"
            },
            "MT5": {
                "folder": "https://drive.google.com/drive/folders/18rUn5-YgywdO2c0UeiujqC_EY3ATVq4s?usp=sharing",
                "installer": "https://drive.google.com/file/d/19T0joFR9cZB4Dzlw5dr1bq1eT-Sa7WAd/view?usp=sharing",
                "exe": "https://drive.google.com/drive/folders/192UFSkLpi1GKcqkzRlc0z0lPstEqkbRb?usp=sharing"
            }
        }
    },
    "VALKYRIE": {
        "Réel": {
            "MT4": {
                "folder": "https://drive.google.com/drive/folders/1YQixOyIuWdKYx2r3RS9c4DYcALo5BHRc?usp=sharing",
                "installer": "https://drive.google.com/file/d/15gMTr9E8_7SmlFmuKuq1WJ_Q7apDaTSb/view?usp=sharing",
                "exe": "https://drive.google.com/drive/folders/1If5-STzXToGLM99u7HZ-xI3xiGm88JPK?usp=sharing"
            },
            "MT5": {
                "folder": "LINK_VALKYRIE_REAL_MT5_FOLDER",
                "installer": "LINK_VALKYRIE_REAL_MT5_INSTALLER",
                "exe": "LINK_VALKYRIE_REAL_MT5_EXE"
            }
        },
        "Démo": {
            "MT4": {
                "folder": "https://drive.google.com/drive/folders/1WDedP4HWqSA5aQH0SiG7szmH_ZTQAVZV?usp=sharing",
                "installer": "https://drive.google.com/file/d/1vGMzMroHUsDANdsG1Bi2Qs-9X4XjwJP6/view?usp=sharing",
                "exe": "https://drive.google.com/drive/folders/1emNLSozRH_XHXjcwDJD0DmAQpR6cCBG1?usp=sharing"
            },
            "MT5": {
                "folder": "LINK_VALKYRIE_DEMO_MT5_FOLDER",
                "installer": "LINK_VALKYRIE_DEMO_MT5_INSTALLER",
                "exe": "LINK_VALKYRIE_DEMO_MT5_EXE"
            }
        }
    }
}

# --- LIENS STRIPE (Abonnements) ---
STRIPE_LINKS = {
    "HORIZON": {
        "PARTENAIRE": {
            "NON": "https://buy.stripe.com/00wdR81XG76jgDrbKtffy05",
            "OUI": "https://buy.stripe.com/fZuaEW31KduHbj79Clffy0c"
        },
        "LIBERTÉ": {
            "NON": "https://buy.stripe.com/7sYeVc0TC62f0Et7udffy0d",
            "OUI": "https://buy.stripe.com/5kQ8wO7i08ancnbg0Jffy0e"
        }
    },
    "VALKYRIE": {
        "PARTENAIRE": {
            "NON": "https://buy.stripe.com/00wcN4cCk1LZ3QF29Tffy06",
            "OUI": "https://buy.stripe.com/28EdR8eKs8ancnbbKtffy0b"
        },
        "LIBERTÉ": {
            "NON": "https://buy.stripe.com/00weVcfOw9er4UJ7udffy04",
            "OUI": "https://buy.stripe.com/28EbJ06dWfCPcnb01Lffy09"
        }
    }
}

BTC_WALLET = "bc1q9penjcn8pzyg3w4l6655x8vz0gyzc6zvmpkdxy"
CONTACT_SUPPORT = "https://t.me/kal_mydas"

# --- BROKERS ---
BROKERS_FR = {"Valetax": "https://ma.valetax.com/p/3522435", "Fusion Markets": "https://fusionmarkets.com/?refcode=108479"}
BROKERS_BE = {"Valetax": "https://ma.valetax.com/p/3522435", "Fusion Markets": "https://fusionmarkets.com/?refcode=108479"}
BROKERS_WORLD = {
    "JustMarkets": "https://one.justmarkets.link/a/aispz02jbv", 
    "Valetax": "https://ma.valetax.com/p/3522435", 
    "Fusion Markets": "https://fusionmarkets.com/?refcode=108479"
}

# ==============================================================================
# --- 🔧 FONCTIONS UTILES ---
# ==============================================================================

def ensure_inbox():
    if not os.path.exists(INBOX_PATH):
        try:
            os.makedirs(INBOX_PATH)
        except Exception as e:
            st.error(f"Erreur création dossier inbox: {e}")

def save_lead_json(data):
    """Sauvegarde le lead en JSON compatible CRM dans le dossier inbox"""
    ensure_inbox()
    
    unique_id = int(datetime.now().timestamp() * 1000)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"lead_WEB_{unique_id}_{timestamp}.json"
    filepath = os.path.join(INBOX_PATH, filename)
    
    # Mapping Offre CRM
    offre_crm = "Standard"
    if "PARTENAIRE" in data.get('offre', '').upper():
        offre_crm = "PARTENAIRE"
    elif "LIBERTÉ" in data.get('offre', '').upper():
        offre_crm = "LIBERTÉ"

    # Construction JSON CRM (Clients + Accounts)
    export_data = {
        "clients": [{
            "id": unique_id,
            "name": data.get('nom', 'Anonyme'),
            "notes": f"Source: WEB Streamlit | Telegram: {data.get('telegram')} | TikTok: {data.get('tiktok')} | Pays: {data.get('pays')} | Profil: {data.get('profil')}",
            "telegram": data.get('telegram'),
            "tiktok": data.get('tiktok'),
            "country": data.get('pays'),
            "type": "Particulier"
        }],
        "accounts": [{
            "id": unique_id + 1,
            "clientId": unique_id,
            "login": data.get('login', '000000'),
            "password": data.get('mdp', ''),
            "server": data.get('serveur', 'Unknown'),
            "platform": data.get('plateforme', 'MT4'),
            "robotName": data.get('robot', 'HORIZON'),
            "offerId": offre_crm,
            "balance": data.get('capital', '0'),
            "startDate": datetime.now().strftime("%Y-%m-%d"),
            "isReal": data.get('mode') == 'Réel'
        }]
    }
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)
        return True, filename
    except Exception as e:
        return False, str(e)

# ==============================================================================
# --- 🖥️ INTERFACE STREAMLIT ---
# ==============================================================================

st.set_page_config(page_title="KAIROS 4 - Assistant", page_icon="🏛️", layout="centered")

# CSS Custom
# CSS Custom - Branding KAL MYDAS (Light & Premium)
st.markdown("""
<style>
    /* Global Text & Background */
    .stApp { background-color: #f8fafc; color: #0f172a; } /* Slate 50 Background */
    
    /* Headers - GOLD */
    h1, h2, h3 { color: #b45309 !important; text-align: center; font-family: 'Segoe UI', sans-serif; }
    
    /* Buttons - GOLD Gradient */
    .stButton>button { 
        background: linear-gradient(45deg, #f59e0b, #fbbf24); 
        color: black !important; 
        border-radius: 8px; 
        font-weight: bold; 
        border: none;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0px 4px 12px rgba(251, 191, 36, 0.4);
    }

    /* Alerts - Light & Clean */
    /* Success: Green Growth */
    div[data-baseweb="notification"] { border-radius: 8px; }
    .stSuccess { 
        background-color: #ecfdf5 !important; /* Light Green */
        color: #065f46 !important; /* Dark Green Text */
        border: 1px solid #34d399;
    }
    /* Info: Guide / Context - Light Blue & Gold */
    .stInfo { 
        background-color: #f0f9ff !important; /* Light Blue */
        color: #0c4a6e !important; /* Dark Blue Text */
        border-left: 5px solid #fbbf24; /* Gold Accent */
    }
    /* Warning: Attention - Light Orange */
    .stWarning { 
        background-color: #fffbeb !important; /* Light Yellow */
        color: #92400e !important; /* Dark Orange Text */
        border: 1px solid #f59e0b;
    }
    
    /* Inputs */
    .stTextInput>div>div>input { color: #0f172a; background-color: white; border: 1px solid #cbd5e1; }
    .stSelectbox>div>div>div { color: #0f172a; background-color: white; border: 1px solid #cbd5e1; }
</style>
""", unsafe_allow_html=True)

st.title("🏛️ KAIROS 4.0")
st.caption("Assistant d'Architecture Financière")

# Sidebar Info
st.sidebar.header("📚 Documentation Légale")
st.sidebar.link_button("📜 Conditions Générales (CGU)", LEGAL_DOC_URL)
st.sidebar.link_button("📝 Licence / Attestation", LICENSE_DOC_URL)
st.sidebar.markdown("---")
st.sidebar.link_button("🆘 Contacter le Support", CONTACT_SUPPORT)
st.sidebar.markdown("---")
st.sidebar.info("Application Client KAIROS 4.0 - v4.1 (Stable)")

# --- ETAPE 1: PROFIL ---
st.header("1. Profil & Identité")
col1, col2 = st.columns(2)
with col1:
    profil = st.radio("Votre Profil", ["Débutant (Observateur)", "Expert (Bâtisseur)"])
with col2:
    pays = st.selectbox("Résidence Fiscale", ["France", "Belgique", "Monde"])

tiktok = st.text_input("Pseudo TikTok (Requis)", placeholder="@...")
telegram = st.text_input("Pseudo Telegram (Optionnel)", placeholder="@...")
nom = telegram.replace('@', '') if telegram else "UserWeb"

# --- ETAPE 2: MODE ---
st.header("2. Type de Compte")

# --- LAYOUT SLOTS (Pour éviter le conflit DOM) ---
slot_mode_header = st.container()
slot_mode_radio = st.container()
slot_mode_content = st.container() # Le contenu conditionnel ira la-dedans

with slot_mode_header:
    # INFO GUIDE (Permanent pour éviter bug DOM)
    st.info("""
    🎓 **INFO GUIDE : Quel mode choisir ?**
    
    • **Investissement (Réel)** : Vous connectez votre vrai capital pour générer des gains.
    • **Démo (Test)** : Vous utilisez de l'argent virtuel pour tester sans risque.
    
    *Conseil : Si vous n'avez jamais utilisé de robot, commencez par une semaine en Démo.*
    """)

with slot_mode_radio:
    mode = st.radio("Objectif", ["Investissement (Réel)", "Démo (Test)"], horizontal=True, key="mode_choice")
    mode_clean = "Réel" if "Investissement" in mode else "Démo"

# CONTENU CONDITIONNEL (Dans un conteneur dédié)
with slot_mode_content:
    offre = "Standard" # Default
    
    if mode_clean == "Réel":
        st.info("💎 **CHOIX DE L'OFFRE (Licence)**")
        
        # ---------------------------------------------------------
        # AFFICHAGE STATIQUE (Côte à côte) POUR ÉVITER LES BUGS DOM
        # ---------------------------------------------------------
        col_partenaires, col_liberte = st.columns(2)
        
        with col_partenaires:
            st.info("""
            🤝 **OFFRE PARTENAIRE (Recommandé)**
            
            • **Prix** : 10€ / mois
            • **Avantages** : 
                - Frais réduits (Spreads Négociés)
                - Support Prioritaire Kal (@kal_mydas)
                - Accès VIP au Canal Privé
                - ⚠️ **Validation KYC Obligatoire (Identité)**
            """)
            st.write("🔽 **Brokers Partenaires (Ouvrir un compte) :**")
            brokers = BROKERS_FR if pays == "France" else (BROKERS_BE if pays == "Belgique" else BROKERS_WORLD)
            for name, link in brokers.items():
                st.markdown(f"👉 **[{name}]({link})** (Cliquez pour ouvrir)")
                if "JustMarkets" in name:
                     st.warning("⚠️ **Code Affiliation OBLIGATOIRE** : `aispz02jbv`")
        
        with col_liberte:
            st.warning("""
            🦅 **OFFRE LIBERTÉ**
            
            • **Prix** : 15€ / mois
            • **Désavantages** : 
                - Vous payez plus cher votre licence
                - **AUCUN SUPPORT** en cas de litige avec votre broker
                - Vous gérez seul vos spreads et commissions
            """)
        
        # Le choix se fait en dessous, sans modifier l'affichage du dessus
        choix_offre = st.radio("Je choisis mon offre :", ["🤝 PARTENAIRE (10€/mois)", "🦅 LIBERTÉ (15€/mois)"], key="offre_choice")
        if "PARTENAIRE" in choix_offre:
             offre = "PARTENAIRE"
        else:
             offre = "LIBERTÉ"
            
    else:
        # MODE DEMO
        offre = "DÉMO GRATUIT"
        st.warning("""
        ⚠️ **RAPPEL IMPORTANT : MetaQuotes ≠ Broker**
        
        Pour avoir des identifiants (Login/Mdp) valides, vous devez ouvrir un **compte de démonstration** chez un vrai courtier (comme JustMarkets, Vantage, etc.).
        Ne confondez pas avec l'application "MetaTrader" seule.
        """)
        st.write("🔽 **Ouvrir un compte DÉMO gratuit (1 minute) :**")
        brokers = BROKERS_FR if pays == "France" else (BROKERS_BE if pays == "Belgique" else BROKERS_WORLD)
        for name, link in brokers.items():
            st.markdown(f"👉 **[{name}]({link})** (Cliquez pour ouvrir)")
            if "JustMarkets" in name:
                 st.warning("⚠️ **Code Affiliation OBLIGATOIRE** : `aispz02jbv`")

# --- ETAPE 3: CAPITAL & ROBOT ---
st.header("3. Capital & Robot")

# Placeholders pour stabilité
c_capital = st.container()
c_robot_widget = st.container()

with c_capital:
    # INFO GUIDE CAPITAL
    st.info("""
    🎓 **Pourquoi le Capital est important ?**
    
    • **Compte CENTIMES (Standard Cent)** : Transforme 10€ en 1 000 unités. Idéal pour démarrer avec un petit capital (< 1 000€).
    • **Compte STANDARD** : 1€ = 1 unité. Recommandé pour les capitaux plus importants (> 1 000€).
    """)
        
    st.markdown("💰 **Quel est votre capital de départ ?**")
    capital = st.radio("Montant", ["Moins de 1000€ (Centimes recommandé)", "Plus de 1000€ (Standard possible)"], label_visibility="collapsed", key="capital_choice")

with c_robot_widget:
    # INFO GUIDE ROBOT
    st.info("""
    🎓 **Quel Robot pour démarrer ?**
    
    • **HORIZON** est conçu pour la sécurité. Il ne trade que dans le sens de la tendance. C'est le choix idéal pour dormir tranquille.
    • **VALKYRIE** est une formule 1. Ça va très vite, ça gagne beaucoup, mais ça peut sortir de la route. À éviter si vous débutez.
    """)
        
    st.markdown("🤖 **Choix de votre Stratégie (Robot)**")
    
    # ---------------------------------------------------------
    # AFFICHAGE STATIQUE (Côte à côte) POUR ÉVITER LES BUGS DOM
    # ---------------------------------------------------------
    col_h, col_v = st.columns(2)
    
    with col_h:
        st.info("""
        🌊 **HORIZON** (Recommandé)
        
        • **Force Tranquille**
        • **Obj**: Croissance stable
        • **Perf**: +60% / 10 ans
        • **Capital Min**: 100€ (Cent) ou 10k (Std)
        • **Drawdown Max**: ~40% (10 ans)
        • **Plateforme**: MT4 & MT5
        """)
        
    with col_v:
        st.warning("""
        🔥 **VALKYRIE** (Expert)
        
        • **Attaque Pure**
        • **Obj**: Suiveur de Tendance Agressif
        • **Perf**: +600% / 15 ans
        • **Capital Min**: 10€ (Cent) ou 1000€ (Std)
        • **Drawdown Max**: ~13% (15 ans)
        • **Plateforme**: MT4 Uniquement
        """)

    # Le choix du robot se fait en dessous, en toute connaissance de cause
    robot_choice = st.radio("Sélectionnez votre Robot :", ["HORIZON", "VALKYRIE"], key="robot_choice")
    robot = "HORIZON" if "HORIZON" in robot_choice else "VALKYRIE"

# Conseil Capital (Reste simple et statique si possible, ou juste un st.write)
# Conseil Capital
advice_slot = st.empty()

if "Moins" in capital:
    if robot == "VALKYRIE":
         advice_slot.warning("⚠️ **Valkyrie & Petit Capital** : Assurez-vous d'utiliser un compte **CENTIMES** pour diviser le risque par 100.")
    else:
         advice_slot.success("✅ **Excellent choix !** Horizon en compte Centimes est parfait pour démarrer en douceur.")
else:
    if robot == "HORIZON":
        advice_slot.success("✅ **Stabilité Maximale.** Horizon avec un capital standard est très sécurisant sur le long terme.")
    else:
        advice_slot.warning("⚠️ **Mode Expert.** Valkyrie demande une surveillance accrue (Trading Haute Fréquence).")

# --- ETAPE 4: SÉRÉNITÉ & TECH ---
# --- ETAPE 4: SÉRÉNITÉ & TECH ---
st.header("4. Configuration Technique")

# Choix Hébergement (Selectbox pour éviter les bugs de layout)
serenite_choice = st.selectbox("Option Hébergement", ["❌ NON (Je gère mon PC)", "🛡️ OUI - Option Sérénité (10€/mois)"], help="Nous hébergeons le robot pour vous.")
serenite = "OUI" in serenite_choice

col_p, col_l = st.columns(2)
with col_p:
    plateforme = st.selectbox("Plateforme Trading", ["MT4", "MT5"])
with col_l:
    login = st.text_input("Numéro de Compte (Login)")

if serenite:
    st.info("ℹ️ **Mode Sérénité Activé :** Vos identifiants sont requis pour l'installation sur nos serveurs.")
    mdp = st.text_input("Mot de Passe (Trading)", type="password")
    serveur = st.text_input("Nom du Serveur Broker")
else:
    mdp = ""
    serveur = st.text_input("Nom du Serveur (Optionnel si non hébergé)")

# --- VALIDATION ---
st.markdown("---")

# Session State pour gérer les étapes (Validation -> Paiement -> Final)
if 'step' not in st.session_state:
    st.session_state.step = 0

# ETAPE 0: VALIDATION TECHNIQUE
if st.session_state.step == 0:
    if st.button("🚀 VALIDER LA CONFIGURATION"):
        if not tiktok or not login:
            st.error("⚠️ TikTok et Login sont requis.")
        else:
            if mode_clean == "Réel":
                st.session_state.step = 1 # Go to Payment
                st.rerun()
            else:
                st.session_state.step = 2 # Go to Finish (Demo)
                st.rerun()

# ETAPE 1: PAIEMENT (REEL UNIQUEMENT)
if st.session_state.step == 1:
    st.info("💎 **DERNIÈRE LIGNE DROITE !**")
    
    # Calcul Prix Exact (Nouvelle Logique V3)
    prix = 0
    if robot == "HORIZON":
        if offre == "PARTENAIRE": prix = 10
        elif offre == "LIBERTÉ": prix = 15
    elif robot == "VALKYRIE":
        if offre == "PARTENAIRE": prix = 15
        elif offre == "LIBERTÉ": prix = 20
    
    if serenite:
        if robot == "VALKYRIE" and offre == "LIBERTÉ":
            prix = 35 # Spécifique User
        else:
            prix += 10 # Standard
    
    st.markdown(
        f"""
        ### 📋 Récapitulatif
        - **Robot**: {robot}
        - **Offre**: {offre}
        - **Option Sérénité**: {"OUI" if serenite else "NON"}
        
        ### 💰 TOTAL À RÉGLER : {prix}€ / mois
        *"L'investissement sur soi est le seul qui rapporte des intérêts à vie."*
        """
    )
    
    st.markdown("### 💳 Mode de Règlement")
    method = st.radio("Choisissez votre méthode :", ["💳 Carte Bancaire (Stripe)", "₿ Crypto (Bitcoin)"])
    
    if "Carte" in method:
        # Lien Stripe
        try:
            f_robot = "HORIZON" if "HORIZON" in robot else "VALKYRIE"
            f_offre = "PARTENAIRE" if "PARTENAIRE" in offre else "LIBERTÉ"
            f_serenite = "OUI" if serenite else "NON"
            lien_stripe = STRIPE_LINKS.get(f_robot, {}).get(f_offre, {}).get(f_serenite, "https://stripe.com")
        except:
            lien_stripe = "https://stripe.com"

        st.link_button(f"💳 RÉGLER {prix}€", lien_stripe)
        validate_text = "✅ PAIEMENT EFFECTUÉ"
        
    else: # BTC
        st.markdown(f"**Veuillez envoyer exactement __{prix}€__ en BTC à l'adresse suivante :**")
        st.code(BTC_WALLET, language="text")
        st.caption("*(Cliquez sur l'icône à droite pour copier)*")
        
        st.warning("⚠️ **Important :** Réseau BTC (Bitcoin) uniquement. Envoyez une preuve de transaction au Support.")
        
        st.link_button("📤 Envoyer Preuve au Support", CONTACT_SUPPORT)
        validate_text = "✅ J'AI ENVOYÉ LES FONDS"
    
    if st.button(validate_text):
        st.session_state.step = 2
        st.rerun()

# ETAPE 2: FINALISATION & SAUVEGARDE
if st.session_state.step == 2:
    # Save Data
    user_data = {
        "nom": nom,
        "tiktok": tiktok,
        "telegram": telegram,
        "pays": pays,
        "profil": profil,
        "mode": mode_clean,
        "offre": offre,
        "capital": capital,
        "robot": robot,
        "plateforme": plateforme,
        "login": login,
        "mdp": mdp,
        "serveur": serveur
    }
    
    success, msg = save_lead_json(user_data)
    
    if success:
        st.success(f"✅ **INSCRIPTION VALIDÉE !**\n\nDossier généré et transmis : `{msg}`")
        st.balloons()
        
        # Affichage Liens
        f_robot = "HORIZON" if "HORIZON" in robot else "VALKYRIE"
        links = DRIVE_ROBOTS.get(f_robot, {}).get(mode_clean, {}).get(plateforme, {})
        
        st.markdown(f"### 📥 Téléchargements ({f_robot} - {mode_clean} - {plateforme})")
        
        if links.get("folder") and not links["folder"].startswith("LINK_"):
            col_d1, col_d2, col_d3 = st.columns(3)
            with col_d1:
                st.link_button("📂 Dossier Complet", links["folder"])
            with col_d2:
                st.link_button("⚙️ Installer", links["installer"])
            with col_d3:
                st.link_button("▶️ Exécutable", links["exe"])
        else:
            st.warning(f"⚠️ Les liens de téléchargement pour {f_robot}/{plateforme} ne sont pas encore configurés dans le script.")
        
        st.info("👉 Votre dossier est prêt dans le système KAIROS. Bienvenue dans l'équipe !")
        
        if st.button("🔄 NOUVELLE CONFIGURATION"):
            st.session_state.step = 0
            st.rerun()
        
    else:
        st.error(f"❌ Erreur lors de la sauvegarde : {msg}")
        if st.button("⬅️ Retour"):
            st.session_state.step = 0
            st.rerun()
