from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    WebDriverException, TimeoutException, NoSuchElementException,
    StaleElementReferenceException, ElementClickInterceptedException
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from colorama import Fore, Style, init
from time import sleep, time
import os
import sys
import threading

# 🎨 Initialisation
init(autoreset=True)

# ═══════════════════════════════════════════════════════════════════
#                        SYSTÈME DE LOGGING
# ═══════════════════════════════════════════════════════════════════

def print_banner():
    banner = Fore.YELLOW + """
██████╗  █████╗ ██╗    ██╗ █████╗               ███████╗███╗   ██╗ █████╗ ██████╗ 
██╔══██╗██╔══██╗██║    ██║██╔══██╗              ██╔════╝████╗  ██║██╔══██╗██╔══██╗
██║  ██║███████║██║ █╗ ██║███████║    █████╗    ███████╗██╔██╗ ██║███████║██████╔╝
██║  ██║██╔══██║██║███╗██║██╔══██║    ╚════╝    ╚════██║██║╚██╗██║██╔══██║██╔═══╝   By 1s0e/DAWA
██████╔╝██║  ██║╚███╔███╔╝██║  ██║              ███████║██║ ╚████║██║  ██║██║     
╚═════╝ ╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝              ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝                                                                 
"""
    print(banner)

def log_step(step_num, total, message):
    """Log une étape de progression avec animation fluide"""
    bar_length = 40
    progress = step_num / total
    percentage = int(progress * 100)
    
    # Animation fluide de la barre
    for i in range(int(bar_length * progress) + 1):
        filled = i
        bar = '█' * filled + '░' * (bar_length - filled)
        current_percent = int((i / bar_length) * 100)
        print(f"\r{Fore.CYAN}[{step_num}/{total}] {Fore.WHITE}{bar} {Fore.YELLOW}{current_percent}%", end='', flush=True)
        sleep(0.02)
    
    print(f"\n{Fore.MAGENTA}      ➜ {Fore.WHITE}{message}{Style.RESET_ALL}")

def log_success(msg): 
    print(f"{Fore.GREEN}  ✓ {msg}{Style.RESET_ALL}")

def log_warning(msg): 
    print(f"{Fore.YELLOW}  ⚠ {msg}{Style.RESET_ALL}")

def log_error(msg): 
    print(f"{Fore.RED}  ✗ {msg}{Style.RESET_ALL}")

def log_info(msg): 
    print(f"{Fore.CYAN}  ℹ {msg}{Style.RESET_ALL}")

def section_header(title):
    """Affiche un en-tête de section"""
    print(f"\n{Fore.CYAN}{'─'*70}")
    print(f"{Fore.YELLOW}  {title}")
    print(f"{Fore.CYAN}{'─'*70}{Style.RESET_ALL}")

# ═══════════════════════════════════════════════════════════════════
#                      CONFIGURATION
# ═══════════════════════════════════════════════════════════════════

def load_config():
    """Charge la configuration depuis config.txt"""
    config_file = 'config.txt'
   
    if not os.path.exists(config_file):
        log_error(f"Fichier {config_file} introuvable!")
        print(f"\n{Fore.YELLOW}Créez un fichier config.txt avec:")
        print(f"{Fore.WHITE}username=votre_username")
        print(f"{Fore.WHITE}password=votre_password{Style.RESET_ALL}\n")
        sys.exit(1)
   
    config = {}
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and '=' in line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    config[key.strip()] = value.strip()
       
        if 'username' not in config or 'password' not in config:
            log_error("config.txt doit contenir 'username' et 'password'!")
            sys.exit(1)
       
        log_success("Configuration chargée")
        log_info(f"Username: {Fore.WHITE}{config['username']}")
        return config
   
    except Exception as e:
        log_error(f"Erreur de lecture: {e}")
        sys.exit(1)

# ═══════════════════════════════════════════════════════════════════
#                      CONFIGURATION CHROME
# ═══════════════════════════════════════════════════════════════════

def setup_driver():
    """Configure et initialise le driver Chrome"""
    section_header("⚙️  CONFIGURATION DU NAVIGATEUR")
    
    chrome_options = Options()
    prefs = {
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 1
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--use-fake-ui-for-media-stream")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.page_load_strategy = 'eager'
    
    log_success("Options Chrome configurées")
    log_success("Mode furtif activé")
    log_success("Optimisations performances activées")
    
    return webdriver.Chrome(service=Service(), options=chrome_options)

# ═══════════════════════════════════════════════════════════════════
#                      STATISTIQUES
# ═══════════════════════════════════════════════════════════════════

snap_count = 0
fail_count = 0
bug_count = 0
refresh_count = 0
start_time = time()

def show_stats():
    """Affiche les statistiques avec un design moderne type card"""
    elapsed = time() - start_time
    hours = int(elapsed // 3600)
    minutes = int((elapsed % 3600) // 60)
    seconds = int(elapsed % 60)
    
    success_rate = ((snap_count / (snap_count + fail_count)) * 100) if (snap_count + fail_count) > 0 else 100
    
    # Barre de progression stylée
    bar_length = 40
    filled = int((success_rate / 100) * bar_length)
    bar = '█' * filled + '░' * (bar_length - filled)
    
    # Couleur selon le taux
    if success_rate >= 90:
        rate_color = Fore.GREEN
        rate_emoji = "🔥"
    elif success_rate >= 70:
        rate_color = Fore.YELLOW
        rate_emoji = "⚡"
    else:
        rate_color = Fore.RED
        rate_emoji = "⚠️"
    
    # Design moderne avec cards
    print(f"\n{Fore.CYAN}{'━' * 70}")
    print(f"{Fore.YELLOW}  📊  STATISTIQUES EN TEMPS RÉEL")
    print(f"{Fore.CYAN}{'━' * 70}{Style.RESET_ALL}\n")
    
    # Card Snaps envoyés
    print(f"{Fore.GREEN}  ┌─ ✓ SNAPS ENVOYÉS")
    print(f"{Fore.GREEN}  │  {Fore.WHITE}{snap_count} snap(s){Style.RESET_ALL}")
    print()
    
    # Card Échecs
    print(f"{Fore.RED}  ┌─ ✗ ÉCHECS D'ENVOI")
    print(f"{Fore.RED}  │  {Fore.WHITE}{fail_count} échec(s){Style.RESET_ALL}")
    print()
    
    # Card Bugs
    print(f"{Fore.YELLOW}  ┌─ ⚠ BUGS CONSÉCUTIFS")
    print(f"{Fore.YELLOW}  │  {Fore.WHITE}{bug_count}/3{Style.RESET_ALL}")
    print()
    
    # Card Refresh
    print(f"{Fore.MAGENTA}  ┌─ ↻ PAGES RECHARGÉES")
    print(f"{Fore.MAGENTA}  │  {Fore.WHITE}{refresh_count} fois{Style.RESET_ALL}")
    print()
    
    # Card Temps
    print(f"{Fore.BLUE}  ┌─ ⏱ TEMPS ÉCOULÉ")
    print(f"{Fore.BLUE}  │  {Fore.WHITE}{hours}h {minutes:02d}m {seconds:02d}s{Style.RESET_ALL}")
    print()
    
    # Card Taux de réussite (le plus important)
    print(f"{Fore.CYAN}{'─' * 70}{Style.RESET_ALL}")
    print(f"{rate_color}  {rate_emoji}  TAUX DE RÉUSSITE : {success_rate:.1f}%{Style.RESET_ALL}")
    print(f"  {Fore.WHITE}{bar}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'─' * 70}{Style.RESET_ALL}\n")

# ═══════════════════════════════════════════════════════════════════
#                      UTILITAIRES
# ═══════════════════════════════════════════════════════════════════

skip_countdown = False

def wait_with_skip(seconds, message=""):
    """Attente avec animation fluide et possibilité de skip"""
    global skip_countdown
    skip_countdown = False
    
    print(f"\n{Fore.YELLOW}⏸  {message}")
    print(f"{Fore.CYAN}   Appuyez sur ENTRÉE pour passer...{Style.RESET_ALL}\n")
    
    def listen_for_skip():
        global skip_countdown
        input()
        skip_countdown = True
    
    listener = threading.Thread(target=listen_for_skip, daemon=True)
    listener.start()
    
    for i in range(seconds, 0, -1):
        if skip_countdown:
            print(f"\r{Fore.GREEN}   ⏭  Pause sautée!{' '*50}{Style.RESET_ALL}")
            return
        
        # Animation fluide du spinner
        spinner = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        for frame in spinner:
            if skip_countdown:
                print(f"\r{Fore.GREEN}   ⏭  Pause sautée!{' '*50}{Style.RESET_ALL}")
                return
            print(f"\r{Fore.MAGENTA}   {frame} {Fore.WHITE}{i}s restantes...{' '*20}", end='', flush=True)
            sleep(0.1)
    
    print(f"\r{' '*70}\r", end='')

def is_valid_group(text):
    """Vérifie si c'est un vrai groupe (pas un élément de menu)"""
    if not text or not text.strip():
        return False
    
    text_lower = text.strip().lower()
    
    # Liste EXHAUSTIVE de tous les termes à ignorer
    ignored_terms = [
        # Sélection (FR)
        'sélectionner', 'tout sélectionner', 'sélectionner tout',
        'désélectionner', 'tout désélectionner', 'désélectionner tout',
        'effacer', 'effacer tout', 'tout effacer',
        
        # Sélection (EN)
        'select', 'select all', 'all select',
        'deselect', 'deselect all', 'all deselect',
        'clear', 'clear all', 'all clear',
        
        # Raccourcis
        'raccourcis', 'raccourci', 'shortcuts', 'shortcut',
        
        # Interface
        'send to', 'envoyer à', 'envoyer', 'to:', 'à:',
        'recent', 'récent', 'récents', 'recents',
        'best friends', 'meilleurs amis',
        'groups', 'groupes', 'groupe', 'group',
        'stories', 'story', 'histoire', 'histoires',
        
        # Émojis seuls
        '🔥', '⭐', '💬', '👥', '📸', '❤️', '💛', '💚', '💙', '💜'
    ]
    
    # Vérifications strictes
    for term in ignored_terms:
        if text_lower == term or term in text_lower or text_lower in term:
            return False
    
    # Ignorer textes trop courts
    if len(text.strip()) < 2:
        return False
    
    # Ignorer uniquement émojis/symboles
    if all(ord(c) > 127 for c in text.strip()):
        return False
    
    return True

# ═══════════════════════════════════════════════════════════════════
#                      PROGRAMME PRINCIPAL
# ═══════════════════════════════════════════════════════════════════

print_banner()

credentials = load_config()
driver = setup_driver()

selected_group_xpaths = []

try:
    # ═══════════════════════════════════════════════════════════════
    #                      CONNEXION
    # ═══════════════════════════════════════════════════════════════
    
    section_header("🔐  CONNEXION À SNAPCHAT")
    
    log_step(1, 6, "Chargement de Snapchat...")
    driver.get('https://www.snapchat.com/')
    log_success("Page chargée")

    log_step(2, 6, "Saisie du nom d'utilisateur...")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'ai_input'))).send_keys(credentials['username'])
    sleep(0.3)
    log_success("Username renseigné")

    log_step(3, 6, "Clic sur 'Next'...")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/main/div[2]/div[1]/aside/div/form/div/span/button'))).click()
    log_success("Bouton Next cliqué")

    wait_with_skip(30, "Vérification humaine possible (CAPTCHA)")

    try:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="password-root"]/div/div[4]/div/section/div/div/div[3]/button[1]'))).click()
        log_success("Cookies acceptés")
    except:
        pass

    log_step(4, 6, "Saisie du mot de passe...")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'password'))).send_keys(credentials['password'])
    sleep(0.3)
    log_success("Mot de passe renseigné")

    log_step(5, 6, "Connexion en cours...")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/div[1]/main/div[1]/div/div[1]/div/form/div[3]/button'))).click()
    sleep(0.3)
    log_success("Connexion réussie")

    log_step(6, 6, "Gestion des popups...")
    try:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div[4]/div[2]/button[1]'))).click()
        log_success("Notifications gérées")
    except:
        pass

    try:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'div._jsfs svg[aria-label="close"]'))).click()
        log_success("Popup Ads fermée")
    except:
        pass

    # ═══════════════════════════════════════════════════════════════
    #                   SÉLECTION DES GROUPES
    # ═══════════════════════════════════════════════════════════════

    def scrape_groups():
        """Récupère UNIQUEMENT les vrais groupes (pas les éléments de menu)"""
        section_header("🔍  DÉTECTION DES GROUPES")
        
        try:
            log_info("Activation de la caméra...")
            try:
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg.aC3Y8'))
                ).click()
                sleep(1.2)
                log_success("Caméra activée")
            except:
                log_info("Caméra déjà active")

            log_info("Prise d'un snap de test...")
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div[1]/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[1]/div/button[1]/div'))
            ).click()
            sleep(0.6)
            log_success("Snap pris")

            log_info("Ouverture du menu...")
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="snap-preview-container"]/div[2]/button[2]'))
            ).click()
            sleep(1.2)
            log_success("Menu ouvert")

            log_info("Accès au shortcut flamme...")
            flame_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@class="c47Sk" and text()="🔥"]'))
            )
            flame_button.click()
            sleep(1.2)
            log_success("Shortcut flamme activé")

            log_info("Analyse des groupes...")
            sleep(0.6)
           
            group_elements = driver.find_elements(By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/form/div/ul/li')
            
            groups = []
            ignored_count = 0
            
            print(f"\n{Fore.CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print(f"{Fore.YELLOW}  🎯  GROUPES DISPONIBLES")
            print(f"{Fore.CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Style.RESET_ALL}\n")
            
            for i, elem in enumerate(group_elements):
                try:
                    text = elem.text.strip()
                    
                    # Filtrage strict : n'affiche QUE les vrais groupes
                    if is_valid_group(text):
                        groups.append({
                            'index': len(groups),
                            'name': text,
                            'xpath': f'//*[@id="root"]/div[1]/div[3]/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/form/div/ul/li[{i+1}]'
                        })
                        # Affichage moderne sans boîte
                        display_name = text[:40] if len(text) > 40 else text
                        print(f"  {Fore.GREEN}[{len(groups)-1}]{Fore.WHITE}  {display_name}{Style.RESET_ALL}")
                    else:
                        ignored_count += 1
                        
                except Exception as e:
                    pass
            
            print(f"\n{Fore.CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Style.RESET_ALL}\n")
           
            if not groups:
                log_error("Aucun groupe trouvé!")
                log_warning("Vérifiez que vous avez des groupes avec flamme")
                return None
           
            log_success(f"{len(groups)} groupe(s) détecté(s)")
            log_info(f"{ignored_count} élément(s) de menu ignoré(s)")
            return groups
           
        except Exception as e:
            log_error(f"Erreur: {str(e)}")
            return None

    available_groups = scrape_groups()
   
    if available_groups:
        section_header("⚙️  CONFIGURATION DE L'ENVOI")
        
        print(f"{Fore.YELLOW}Sélectionnez les groupes à cibler:")
        print(f"{Fore.WHITE}  • Numéros séparés par virgules (ex: 0,1,3)")
        print(f"{Fore.WHITE}  • Tapez 'all' pour tous les groupes{Style.RESET_ALL}\n")
        
        user_input = input(f"{Fore.MAGENTA}➜ Votre choix: {Fore.WHITE}").strip()
       
        if user_input.lower() == 'all':
            selected_group_xpaths = [g['xpath'] for g in available_groups]
            log_success(f"Tous les groupes sélectionnés ({len(selected_group_xpaths)})")
        else:
            try:
                indices = [int(x.strip()) for x in user_input.split(',')]
                selected_group_xpaths = []
                
                for idx in indices:
                    if 0 <= idx < len(available_groups):
                        selected_group_xpaths.append(available_groups[idx]['xpath'])
                        log_success(f"✓ {available_groups[idx]['name']}")
                    else:
                        log_warning(f"Index {idx} invalide (max: {len(available_groups)-1})")
                        
                if not selected_group_xpaths:
                    log_error("Aucun groupe valide! Sélection de tous...")
                    selected_group_xpaths = [g['xpath'] for g in available_groups]
                else:
                    log_success(f"{len(selected_group_xpaths)} groupe(s) configuré(s)")
                    
            except:
                log_error("Entrée invalide! Tous les groupes sélectionnés")
                selected_group_xpaths = [g['xpath'] for g in available_groups]
       
        try:
            driver.find_element(By.XPATH, '//*[@id="snap-preview-container"]/div[2]/button[1]').click()
            sleep(0.6)
        except:
            pass
        
        log_info("Actualisation...")
        driver.refresh()
        sleep(4)
        log_success("Prêt!")

    # ═══════════════════════════════════════════════════════════════
    #                   FONCTIONS D'ENVOI
    # ═══════════════════════════════════════════════════════════════

    def click_group_original(xpath):
        """Sélectionne un groupe"""
        try:
            elem = driver.find_element(By.XPATH, xpath)
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elem)
            sleep(0.25)
            actions = ActionChains(driver)
            actions.move_to_element(elem).click().perform()
            sleep(0.5)
            return True
        except:
            return False

    def send_snap():
        """Envoie un snap aux groupes sélectionnés"""
        global snap_count, fail_count, bug_count, refresh_count

        try:
            # Bouton "Clique ici"
            try:
                bouton = driver.find_element(By.XPATH, '//*[@id="snap-preview-container"]/div[1]/button')
                driver.execute_script("arguments[0].click();", bouton)
                sleep(0.3)
            except:
                pass

            # Snap
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div[1]/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[1]/div/button[1]/div'))
            ).click()
            log_success("Snap capturé")
            sleep(0.6)

            # Menu
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="snap-preview-container"]/div[2]/button[2]'))
            ).click()
            log_success("Menu ouvert")
            sleep(1.0)

            # Flamme
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@class="c47Sk" and text()="🔥"]'))
            ).click()
            log_success("Flamme activée")
            sleep(1.2)

            # Sélection
            log_info("Sélection des groupes...")
            success_count = 0
            for xpath in selected_group_xpaths:
                if click_group_original(xpath):
                    success_count += 1
            
            if success_count == 0:
                raise Exception("Aucun groupe sélectionné")
            
            log_success(f"{success_count}/{len(selected_group_xpaths)} sélectionnés")
            sleep(0.3)

            # Envoi
            send_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/form/div[2]/button'))
            )
            driver.execute_script("arguments[0].click();", send_button)
            
            print(f"\n{Fore.GREEN}{'─'*70}")
            print(f"{Fore.GREEN}{'🚀  SNAP ENVOYÉ AVEC SUCCÈS!'.center(70)}")
            print(f"{Fore.GREEN}{'─'*70}{Style.RESET_ALL}\n")

            snap_count += 1
            bug_count = 0
            sleep(2.5)

        except Exception as e:
            bug_count += 1
            fail_count += 1
            log_warning(f"Échec ({bug_count}/3)")
            log_error(str(e)[:80])

            if bug_count >= 3:
                log_error("Actualisation nécessaire...")
                driver.refresh()
                refresh_count += 1
                bug_count = 0
                sleep(6)

    # ═══════════════════════════════════════════════════════════════
    #                   BOUCLE D'ENVOI
    # ═══════════════════════════════════════════════════════════════

    if selected_group_xpaths:
        section_header("🚀  ENVOI AUTOMATIQUE DÉMARRÉ")
        
        for i in range(1000):
            print(f"\n{Fore.CYAN}╔{'═'*68}╗")
            print(f"{Fore.CYAN}║{Fore.YELLOW}{f'📤  ENVOI #{i+1}/1000'.center(68)}{Fore.CYAN}║")
            print(f"{Fore.CYAN}╚{'═'*68}╝{Style.RESET_ALL}\n")
            
            send_snap()
            show_stats()
    else:
        log_error("Aucun groupe sélectionné!")

except WebDriverException as e:
    log_error(f"Erreur WebDriver: {str(e)[:100]}")
except KeyboardInterrupt:
    print(f"\n\n{Fore.YELLOW}╔{'═'*68}╗")
    print(f"{Fore.YELLOW}║{'⏸  INTERRUPTION UTILISATEUR'.center(68)}║")
    print(f"{Fore.YELLOW}╚{'═'*68}╝{Style.RESET_ALL}\n")
except Exception as e:
    log_error(f"Erreur: {str(e)}")
    import traceback
    traceback.print_exc()

# ═══════════════════════════════════════════════════════════════════
#                   FERMETURE
# ═══════════════════════════════════════════════════════════════════

section_header("🏁  FERMETURE")

try:
    if driver:
        driver.quit()
        log_success("Navigateur fermé")
except:
    pass

show_stats()

print(f"\n{Fore.CYAN}╔{'═'*68}╗")
success_msg = '✓  Programme terminé avec succès'.center(68)
thanks_msg = "Merci d'avoir utilisé SnapchBot".center(68)
print(f"{Fore.CYAN}║{Fore.GREEN}{success_msg}{Fore.CYAN}║")
print(f"{Fore.CYAN}║{Fore.WHITE}{thanks_msg}{Fore.CYAN}║")
print(f"{Fore.CYAN}╚{'═'*68}╝{Style.RESET_ALL}\n")