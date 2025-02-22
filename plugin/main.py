from flowlauncher import FlowLauncher
import webbrowser

class Main(FlowLauncher):
    def query(self, query):
        return [
            {
                "Title": "Gemini {}".format(('Your query is: ' + query , query)[query == '']),
                "SubTitle": "Press enter to open Thibault-Savenkoff's GitHub",
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": ["https://github.com/Thibault-Savenkoff/Thibault-Savenkoff"]
                }
            }
        ]

    def context_menu(self, data):
        return [
            {
                "Title": "Gemini's Context menu",
                "SubTitle": "Press enter to open Flow the plugin's repo in GitHub",
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": ["https://github.com/Thibault-Savenkoff/Flow.Launcher.Plugin.Gemini"]
                }
            }
        ]

    def open_url(self, url):
        webbrowser.open(url)