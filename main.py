# from app.menu import Menu
# from app.config_manager import load_config

# def main():
#     config = load_config()

#     menu = Menu(config)
#     menu.run()

# if __name__ == "__main__":
#     main()






from ui.app import EasyTubeApp

def main():
    app = EasyTubeApp()
    app.run()

if __name__ == "__main__":
    main()