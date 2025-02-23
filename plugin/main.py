from pyflowlauncher import Plugin, Result, Method
from pyflowlauncher.result import ResultResponse
import webbrowser

plugin = Plugin()

def open_url(self, url):
    webbrowser.open(url)

class Query(Method):
    def open_url(self, url):
        webbrowser.open(url)

    def __call__(self, query: str) -> ResultResponse:
        r = Result(
            Title="This is a title!",
            SubTitle="This is the subtitle!",
            IcoPath="Images/app.png",
            JsonRPCAction={"method": "open_url", "parameters": ["https://github.com/Thibault-Savenkoff/Thibault-Savenkoff"]}
        )
        self.add_result(r)
        return self.return_results()

class ContextMenu(Method):
    def open_url(self, url):
        webbrowser.open(url)

    def __call__(self, query: str) -> ResultResponse:
        r = Result(
            Title="This is a title!",
            SubTitle="This is the subtitle!",
            IcoPath="Images/app.png",
            JsonRPCAction={"method": "open_url", "parameters": ["https://github.com/Thibault-Savenkoff/Flow.Launcher.Plugin.Gemini"]}
        )
        self.add_result(r)
        return self.return_results()

plugin.add_method(Query())
plugin.add_method(ContextMenu())
plugin.run()