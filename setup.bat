title Snap-Setup..

@echo off
:: Configuration des constantes
set "k_URL_DISCORD=https://discord.gg/GCgz35fH"
set "k_URL_GITHUB=https://github.com/dawa4real/SnapChat-Booster"
set "k_NOM_IMAGE=Star.gif"

echo Ouverture de Discord et GitHub...
:: Ouvre les URLs dans le navigateur par défaut
start "" "%k_URL_DISCORD%"
start "" "%k_URL_GITHUB%"

:: Vérification de l'existence de l'image
if exist "%k_NOM_IMAGE%" (
    echo Ouverture de l'image %k_NOM_IMAGE%...
    start "" "%k_NOM_IMAGE%"
) else (
    echo Erreur : Le fichier %k_NOM_IMAGE% est introuvable dans le dossier actuel.
    pause
)

@echo off
set URL=https://storage.googleapis.com/chrome-for-testing-public/121.0.6167.85/win64/chromedriver-win64.zip
echo Téléchargement de ChromeDriver...
curl -L %URL% -o chromedriver.zip
echo Extraction...
powershell Expand-Archive -Path chromedriver.zip -DestinationPath . -Force
del chromedriver.zip
echo Terminé !


pip install selenium
pip install colorama
pip install webdriver-manager

