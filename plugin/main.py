from pyflowlauncher import Plugin, Result, Method
from pyflowlauncher.result import ResultResponse
import webbrowser

plugin = Plugin()

class Query(Method):

    def __call__(self, query: str) -> ResultResponse:
        r = Result(
            Title="This is a title!",
            SubTitle="This is the subtitle!",
            IcoPath="Images/app.png",
            JsonRPCAction={"method": "open_url", "parameters": ["https://github.com/Thibault-Savenkoff/Thibault-Savenkoff"]},
            Score= 0
        )
        self.add_result(r)
        return self.return_results()

class ContextMenu(Method):

    def __call__(self, query: str) -> ResultResponse:
        r = Result(
            Title="This is a title!",
            SubTitle="This is the subtitle!",
            IcoPath="Images/app.png",
            JsonRPCAction={"method": "open_url", "parameters": ["https://github.com/Thibault-Savenkoff/Flow.Launcher.Plugin.Gemini"]},
            Score= 0
        )
        self.add_result(r)
        return self.return_results()

def open_url(self, url):
    webbrowser.open(url)

plugin.add_method(Query())
plugin.add_method(ContextMenu())
plugin.run()