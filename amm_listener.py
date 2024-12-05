import tkinter as tk
from tkinter import ttk
import asyncio
import websockets
import json
import binascii
from datetime import datetime
import webbrowser
import platform

# Add sound functionality
def play_system_ping():
    """Play a system ping sound."""
    if platform.system() == "Windows":
        import winsound
        winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)  # System alert sound
    else:
        # For macOS/Linux, use `playsound` or a similar library
        from playsound import playsound
        playsound('/path/to/sound/file.wav')  # Update with your desired sound file

def decode_currency(asset_hex):
    """Decode the hexadecimal currency field to ASCII."""
    try:
        return binascii.unhexlify(asset_hex).decode('ascii').rstrip('\x00')
    except Exception:
        return "Unknown"

def display_amm_pool(timestamp, asset1_ticker, issuer, dex_screener_link, snipe_link, first_ledger_link):
    """Create a GUI window to display AMM pool information with clickable links."""
    # Play a notification sound when the window is displayed
    play_system_ping()

    root = tk.Tk()
    root.title("New AMM Pool Detected")
    root.attributes("-topmost", True)  # Keep the window always on top

    frame = ttk.Frame(root, padding="10")
    frame.grid()

    ttk.Label(frame, text=f"Timestamp: {timestamp}", font=("Arial", 12)).grid(column=0, row=0, sticky=tk.W)
    ttk.Label(frame, text=f"Asset 1: {asset1_ticker} (Issuer: {issuer})", font=("Arial", 12)).grid(column=0, row=1, sticky=tk.W)

    ttk.Button(frame, text="DEXSCREENER", command=lambda: webbrowser.open(dex_screener_link)).grid(column=0, row=2, pady=5, sticky=tk.W)
    ttk.Button(frame, text="SNIPE", command=lambda: webbrowser.open(snipe_link)).grid(column=0, row=3, pady=5, sticky=tk.W)
    ttk.Button(frame, text="FIRSTLEDGER", command=lambda: webbrowser.open(first_ledger_link)).grid(column=0, row=4, pady=5, sticky=tk.W)

    ttk.Button(frame, text="Close", command=root.destroy).grid(column=0, row=5, pady=10, sticky=tk.W)

    root.mainloop()

async def listen_for_amm_create():
    uri = "wss://s1.ripple.com"  # Mainnet WebSocket URL
    async with websockets.connect(uri, ping_interval=20, ping_timeout=20) as websocket:
        await websocket.send(json.dumps({
            "id": 1,
            "command": "subscribe",
            "streams": ["transactions"]
        }))
        print("Listening for AMMCreate transactions...")
        try:
            while True:
                try:
                    response = await websocket.recv()
                    data = json.loads(response)

                    if data.get("transaction", {}).get("TransactionType") == "AMMCreate":
                        transaction = data["transaction"]
                        timestamp = data.get('date')
                        human_readable_time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S') if timestamp else "N/A"

                        asset1 = transaction['Amount']
                        issuer = asset1.get("issuer", "Unknown")
                        asset1_hex = asset1.get("currency", "XRP")
                        asset1_ticker = decode_currency(asset1_hex)

                        dex_screener_link = f"https://dexscreener.com/xrpl/{asset1_hex}.{issuer}_xrp"
                        snipe_link = f"https://t.me/XrpLedgerSniperBot?start={issuer}"
                        first_ledger_link = f"https://firstledger.net/token/{issuer}/{asset1_hex}"

                        # Log information to the terminal
                        print(f"AMM Pool Created:\n - Timestamp: {human_readable_time}\n - Asset: {asset1_ticker}\n - Issuer: {issuer}\n")

                        # Display the AMM pool information in a GUI window
                        display_amm_pool(human_readable_time, asset1_ticker, issuer, dex_screener_link, snipe_link, first_ledger_link)
                except asyncio.TimeoutError:
                    print("Timeout occurred, keeping the connection alive")
        except websockets.exceptions.ConnectionClosedError as e:
            print(f"WebSocket connection closed: {e}")

asyncio.run(listen_for_amm_create())
