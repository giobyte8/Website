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
    watchlist.stack = 'Python / Django Rest Framework / React / Redux'
    watchlist.desc = """
        Track all the movies that you're wishing to watch, you'd watched or you're
        waiting for, incoming releases and suggestions based on your
        preferences. Create multiple lists and share it with friends
    """
    watchlist.link = 'https://github.com/DiganmeGiovanni/WatchlistWeb'

    pos = Project()
    pos.title = 'POS For the people'
    pos.stack = 'Electron / React / Sequelize ORM'
    pos.desc = """
            The small businesses in latam do not need an over engineered Point of Sales,
            they need a portable, local and simple to use UI to manage its small
            inventory and daily sales. 
        """
    pos.link = "https://github.com/DiganmeGiovanni/PoS2"

    py_docker = Project()
    py_docker.title = 'PyDocker'
    py_docker.stack = 'Python / Django / Docker API'
    py_docker.desc = 'Monitor, start and stop docker containers from a human friendly WebUI'
    py_docker.link = 'https://github.com/DiganmeGiovanni/PyDocker'

    chat_ss = Project()
    chat_ss.title = "Chat Team SS"
    chat_ss.stack = "Node JS / Socket IO / Express JS"
    chat_ss.desc = "A real time and responsive web chat system built with web sockets and NoSQL"
    chat_ss.link = "https://github.com/DiganmeGiovanni/Chat-TeamSS"

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

    codelizer = Project()
    codelizer.title = "Codelizer Service"
    codelizer.stack = "Java / Spring"
    codelizer.desc = """
        Subtract Java classes and methods from Java projects and put them into
        a database for analytics
    """
    codelizer.link = "https://github.com/DiganmeGiovanni/CodelizerService"

    secret_strings = Project()
    secret_strings.title = "JSecret strings"
    secret_strings.stack = "Java / Java Cryptography Architecture"
    secret_strings.desc = """
        A tool for encryption and decryption of Strings through native Java
        JCA (Java Cryptography Architecture) classes.
    """
    secret_strings.link = "https://github.com/DiganmeGiovanni/JSecretStrings"

    qr_scanner = Project()
    qr_scanner.title = "QR Scanner"
    qr_scanner.stack = "Java / ZXing"
    qr_scanner.desc = """
        Scan QR codes through your web cam and launch your browser if it are
        links or file browser if it are local filesystem urls
    """
    qr_scanner.link = "https://github.com/DiganmeGiovanni/QRScanner"

    docker_scripts = Project()
    docker_scripts.title = "Docker Scripts"
    docker_scripts.stack = "Docker / Docker Compose / Bash"
    docker_scripts.desc = """
        Helper and utility scripts and docker files to create containers
        for my daily development workflow
    """
    docker_scripts.link = "https://github.com/DiganmeGiovanni/DockerScripts"

    projects = [
        watchlist,
        pos,
        py_docker,
        chat_ss,
        rtsp_viewer,
        sigma,
        fx_form,
        codelizer,
        secret_strings,
        qr_scanner,
        docker_scripts
    ]

    return render(req, 'portfolio/side_projects.html', {
        'nav_active': 'portfolio',
        'projects': projects
    })


def learning(req):
    py_side = Project()
    py_side.title = "LearningPySide2"
    py_side.stack = "Qt / PySide 2 / QML"
    py_side.link = "https://github.com/DiganmeGiovanni/LearningPySide2"

    python = Project()
    python.title = "LearningPython"
    python.stack = "Python 3"
    python.link = "https://github.com/DiganmeGiovanni/LearningPython"

    node = Project()
    node.title = "LearningNodeJS"
    node.stack = "Node JS / Socket IO"
    node.link = "https://github.com/DiganmeGiovanni/LearningNodeJS"

    bash = Project()
    bash.title = "LearningBash"
    bash.stack = "Bash scripting"
    bash.link = "https://github.com/DiganmeGiovanni/LearningBash"

    j_monkey = Project()
    j_monkey.title = "LearningJMonkey"
    j_monkey.stack = "JMonkey Engine / 3D Programming / Java"
    j_monkey.link = "https://github.com/DiganmeGiovanni/LearningJMonkey"

    cpp = Project()
    cpp.title = "LearningCpp"
    cpp.stack = "C++"
    cpp.link = "https://github.com/DiganmeGiovanni/LearningCpp"

    django = Project()
    django.title = "LearningDjango"
    django.stack = "Django / Python"
    django.link = "https://github.com/DiganmeGiovanni/LearningDjango"

    android = Project()
    android.title = "LearningAndroid"
    android.stack = "Android / Java"
    android.link = "https://github.com/DiganmeGiovanni/LearningAndroid"

    flux = Project()
    flux.title = "LearningFlux"
    flux.stack = "React / Flux / Prop Types"
    flux.link = "https://github.com/DiganmeGiovanni/LearningFlux"

    networking = Project()
    networking.title = "LearningNetworking"
    networking.stack = "Cisco networking / Basic networking theory"
    networking.link = "https://github.com/DiganmeGiovanni/LearningNetworking"

    databases = Project()
    databases.title = "LearningDatabases"
    databases.stack = "Oracle Management / MongoDB management / MySQL management"
    databases.link = "https://github.com/DiganmeGiovanni/LearningDatabases"

    java_fx = Project()
    java_fx.title = "LearningJavaFX"
    java_fx.stack = "Java FX / Java 8"
    java_fx.link = "https://github.com/DiganmeGiovanni/LearningJavaFX"

    foundation = Project()
    foundation.title = "LearningFoundation"
    foundation.stack = "Foundation framework / CSS3"
    foundation.link = "https://github.com/DiganmeGiovanni/LearningFoundation"

    oop = Project()
    oop.title = "LearningOOP"
    oop.stack = "Object Oriented Programming / Java"
    oop.link = "https://github.com/DiganmeGiovanni/LearningOOP"

    projects = [
        py_side,
        python,
        node,
        bash,
        j_monkey,
        cpp,
        django,
        android,
        flux,
        networking,
        databases,
        java_fx,
        foundation,
        oop
    ]

    return render(req, 'portfolio/continuous_learning.html', {
        'nav_active': 'learning',
        'projects': projects
    })


def blog(req):
    return render(req, 'blog/index.html', {
        'nav_active': 'blog'
    })
