from textual.app import App, ComposeResult
from textual.containers import Container, Vertical, Horizontal
from textual.widgets import Header, Footer, Input, Static, RichLog
from textual import on
from rich.text import Text

# Import local modules
from modules import stocks, crypto, ai

# ASCII Art Logo
WELCOME_LOGO = """
  _______  _______  _______  _______  __    _  _______  ______   _______
 |  _    ||  _    ||       ||       ||  |  | ||       ||    _ | |       |
 | |_|   || |_|   ||    ___||    ___||   |_| ||_     _||   | || |   _   |
 |       ||       ||   |___ |   |___ |       |  |   |  |   |_|| |  | |  |
 |  _   | |  _   | |    ___||    ___||  _    |  |   |  |    __ ||  |_|  |
 | |_|   || |_|   ||   |___ |   |___ | | |   |  |   |  |   |  |||       |
 |_______||_______||_______||_______||_|  |__|  |___|  |___|  |||_______|
 
 > SYSTEM READY.
 > CONNECTED TO: GLOBEX, NYSE, NASDAQ, BINANCE
 > TYPE 'HELP' FOR COMMANDS.
"""

class OpenTerminal(App):
    """
    Main Application Class for Bloomberg Terminal Free.
    Uses Textual for TUI rendering.
    """
    CSS_PATH = "styles.tcss"
    TITLE = "BLOOMBERG TERMINAL FREE (OPEN-TERMINAL)"
    
    def compose(self) -> ComposeResult:
        """Construct the UI layout."""
        yield Header(show_clock=True)
        
        with Horizontal():
            # Sidebar with Cheat Sheet
            with Container(id="sidebar"):
                yield Static(
                    "[bold underline]MARKET KEYS[/bold underline]\n\n"
                    "[green]F2: GOVT\n"
                    "F3: CORP\n"
                    "F8: EQUITY\n"
                    "F11: CRYPTO[/green]\n\n"
                    "[bold underline]FUNCTIONS[/bold underline]\n\n"
                    "[yellow]DES[/yellow]: Desc.\n"
                    "[yellow]GP[/yellow]: Chart\n"
                    "[yellow]CN[/yellow]: News"
                )
            
            # Main Content Window (Log)
            with Vertical(id="main-window"):
                yield RichLog(id="output_log", markup=True, wrap=True)
                
        # Command Line Input (Fixed at bottom)
        yield Input(placeholder="COMMAND LINE > Type ticker or command...", id="command_input")
        yield Footer()

    def on_mount(self):
        """Event fired when the application starts."""
        log = self.query_one("#output_log", RichLog)
        # Display welcome message
        log.write(Text(WELCOME_LOGO, style="bold orange1"))
        # Focus on input immediately
        self.query_one("#command_input").focus()

    @on(Input.Submitted)
    def handle_command(self, event: Input.Submitted):
        """Main Command Parser Logic."""
        command = event.value.upper().strip()
        input_widget = self.query_one("#command_input")
        log = self.query_one("#output_log", RichLog)
        
        # Clear input field after submission
        input_widget.value = ""
        
        # Log the command entered by user
        log.write(f"\n[reverse] COMMAND [/reverse] {command}")
        
        parts = command.split()
        if not parts:
            return

        cmd = parts[0]

        # --- SYSTEM COMMANDS ---
        if cmd == "HELP":
            help_text = """
            [bold]AVAILABLE COMMANDS:[/bold]
            
            [yellow]STOCKS:[/yellow]
            {TICKER} DES    -> Company Description (e.g., AAPL DES)
            {TICKER} CHART  -> Price Chart (e.g., TSLA CHART)
            
            [yellow]CRYPTO:[/yellow]
            CRYPTO          -> Top 10 Currencies
            
            [yellow]AI ASSISTANT:[/yellow]
            ASK {QUERY}     -> Ask Warren AI (e.g., ASK Why is market down?)
            
            [yellow]SYSTEM:[/yellow]
            CLS             -> Clear Screen
            EXIT            -> Quit
            """
            log.write(help_text)

        elif cmd == "CLS":
            log.clear()

        elif cmd in ("EXIT", "QUIT"):
            self.exit()

        # --- MODULE: CRYPTO ---
        elif cmd == "CRYPTO":
            log.write("[blink]Fetching Crypto Data...[/blink]")
            # Run in main thread for MVP (should be async in production)
            data = crypto.get_top_crypto()
            log.write(data)

        # --- MODULE: AI ---
        elif cmd == "ASK":
            if len(parts) < 2:
                log.write("[red]Error:[/red] Please provide a question.")
            else:
                question = " ".join(parts[1:])
                log.write("[blink]Thinking (Llama-3)...[/blink]")
                # Simulating response delay
                self.set_timer(1.0, lambda: log.write(ai.ask_warren(question)))

        # --- MODULE: STOCKS ---
        else:
            # Assume the first word is a Ticker (e.g., AAPL)
            ticker = cmd
            
            # Check for function (e.g., 'AAPL DES')
            if len(parts) > 1:
                sub_cmd = parts[1]
                
                if sub_cmd in ("DES", "QUOTE"):
                    log.write(stocks.get_stock_quote(ticker))
                
                elif sub_cmd in ("CHART", "GP"):
                    log.write(f"[bold]Plotting {ticker}...[/bold]")
                    chart = stocks.get_stock_chart(ticker)
                    log.write(Text(chart)) # Render ASCII chart
                
                else:
                    log.write(f"[red]Unknown function '{sub_cmd}' for ticker {ticker}. Try 'DES' or 'CHART'.[/red]")
            else:
                # Default action: Show Quote
                log.write(stocks.get_stock_quote(ticker))

if __name__ == "__main__":
    app = OpenTerminal()
    app.run()
