from django.shortcuts import render

# Create your views here.
from .models import Project


def index(req):
    return render(req, 'index/index.html', {
        'nav_active': 'index'
    })


def portfolio(req):
    watchlist = Project()
    watchlist.title = 'Watchlist'
    watchlist.stack = 'Python / Django Rest / React / Redux'
    watchlist.desc = """
        Track all the movies that you're wishing to watch, you'd watched or you're
        waiting for, incoming releases and suggestions based on your
        preferences.
    """
    watchlist.link = 'https://github.com/DiganmeGiovanni/WatchlistWeb'

    py_docker = Project()
    py_docker.title = 'PyDocker'
    py_docker.stack = 'Python / Django / Docker API'
    py_docker.desc = 'Manage docker containers from a human friendly WebUI'
    py_docker.link = 'https://github.com/DiganmeGiovanni/PyDocker'

    rtsp_viewer = Project()
    rtsp_viewer.title = 'RTSPViewer'
    rtsp_viewer.stack = 'Android / Java / Realm DB'
    rtsp_viewer.desc = """
        A Dynamic player for RSTP Streams. Very useful to
        test streaming servers
    """
    rtsp_viewer.link = 'https://github.com/DiganmeGiovanni/RTSPViewer'

    sigma = Project()
    sigma.title = 'Sigma'
    sigma.stack = "Android / Java / Realm DB"
    sigma.desc = """
        A financial assistant for common humans, track your accounts,
        incomes, spends and balances
    """
    sigma.link = 'https://github.com/DiganmeGiovanni/Sigma'

    fx_form = Project()
    fx_form.title = 'FX Form Generator'
    fx_form.stack = 'Java / Java FX'
    fx_form.desc = """
        "Automagically" generate a Java FX Form UI with support for validation from your java entities
    """
    fx_form.link = 'https://github.com/DiganmeGiovanni/FXFormGenerator'

    pos = Project()
    pos.title = 'POS For the people'
    pos.stack = 'Electron / React / Sequelize ORM'
    pos.desc = """
        The small businesses in latam do not need an over engineered Point of Sales,
        they need a portable, local and simple to use UI to manages its small
        inventory and daily sales. 
    """
    pos.link = "https://github.com/DiganmeGiovanni/PoS2"

    chat_ss = Project()
    chat_ss.title = "Chat Team SS"
    chat_ss.stack = "Node JS / Socket IO / Express JS"
    chat_ss.desc = "A real time web chat system"
    chat_ss.link = "https://github.com/DiganmeGiovanni/Chat-TeamSS"

    iot_noob = Project()
    iot_noob.title = "IoT Noob"
    iot_noob.stack = "Node JS / Arduino / Android"
    iot_noob.desc = "Control your home's lights remotely from an android app"
    iot_noob.link = "https://github.com/DiganmeGiovanni/IoTNoobAndroidClient"

    codelizer = Project()
    codelizer.title = "Codelizer Service"
    codelizer.stack = "Java"
    codelizer.desc = """
        Subtract Java classes and methods from Java projects and put them into
        a database for analytics about documentation, methods and params
    """
    codelizer.link = "https://github.com/DiganmeGiovanni/CodelizerService"

    secret_strings = Project()
    secret_strings.title = "JSecret strings"
    secret_strings.stack = "Java / Java Cryptography Architecture"
    secret_strings.desc = """
        A single tool to encryption and decryption of Strings through native Java
        JCA (Java Cryptography Architecture) classes and optionally using custom
        security layers (Basic funny tricks) on top of Standard Cryptography
        Architecture.
    """
    secret_strings.link = "https://github.com/DiganmeGiovanni/JSecretStrings"

    qr_scanner = Project()
    qr_scanner.title = "QR Scanner"
    qr_scanner.stack = "Java / ZXing"
    qr_scanner.desc = """
        Scan QR codes through your web cam and launch your browser if they are
        links or file browser if local filesystem urls
    """
    qr_scanner.link = "https://github.com/DiganmeGiovanni/QRScanner"

    projects = [
        watchlist,
        pos,
        py_docker,
        rtsp_viewer,
        sigma,
        chat_ss,
        fx_form,
        iot_noob,
        codelizer,
        secret_strings,
        qr_scanner
    ]

    return render(req, 'portfolio/side_projects.html', {
        'nav_active': 'portfolio',
        'projects': projects
    })


def learning(req):
    return render(req, 'portfolio/continuous_learning.html', {
        'nav_active': 'learning'
    })


def blog(req):
    return render(req, 'blog/index.html', {
        'nav_active': 'blog'
    })
