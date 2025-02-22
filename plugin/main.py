from flowlauncher import FlowLauncher
import webbrowser

from pyflowlauncher import Plugin, Result, send_results
from pyflowlauncher.result import ResultResponse

plugin = Plugin()
def open_url(self, url):
    webbrowser.open(url)

@plugin.on_method
def query(query: str) -> ResultResponse:
    r = Result(
        Title="Gemini",
        SubTitle="Press enter to open Thibault-Savenkoff's GitHub",
        IcoPath="Images/app.png"
        "JsonRPCAction": {
            "method": "open_url",
            "parameters": ["https://github.com/Thibault-Savenkoff/Thibault-Savenkoff"]
        }
    )
    return send_results([r])

def context_menu(data: str) -> ResultResponse:
    r = Result(
        Title="Gemini's Context menu",
        SubTitle="Press enter to open Flow the plugin's repo in GitHub",
        IcoPath="Images/app.png",
        JsonRPCAction={
            "method": "open_url",
            "parameters": ["https://github.com/Thibault-Savenkoff/Flow.Launcher.Plugin.Gemini"]
        }

    )
    return send_results([r])

plugin.run()