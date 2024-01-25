import platform
import subprocess

from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.h2("Environment stuff!"),
    ui.span("Python"),
    ui.output_text_verbatim("python"),
    ui.input_text_area("cmd", "Command to run", placeholder="Enter text"),
    ui.output_text_verbatim("cmd_output"),
)


def server(input, output, session):
    @output
    @render.text
    def python():
        return platform.python_version()

    @output
    @render.text
    def cmd_output():
        cmd=input.cmd()
        try:
            return subprocess.check_output(cmd, shell=True).decode()
        except Exception as e:
            return f"Error: {e}"


app = App(app_ui, server)
