# AMM Pool Tracker

A Python application that listens for `AMMCreate` transactions on the XRPL (XRP Ledger) network and notifies the user via a pop-up window when a new Automated Market Maker (AMM) pool is created. The app also logs details of the AMM pool in the terminal and provides clickable links for quick access to related resources.

---

## Features

- **Real-time Notifications**: Listens for `AMMCreate` transactions on the XRPL network.
- **GUI Pop-up Alerts**: Displays AMM pool details in a GUI window that stays on top of other windows.
- **Terminal Logging**: Logs AMM pool information in the terminal for easy tracking.
- **Interactive Links**: Provides links to DEX Screener, sniping bots, and First Ledger token information.
- **System Alert Sound**: Plays a notification sound when a new pool is detected.

---

## Prerequisites

- XRPL Sniper Bot by Suite
  - `https://t.me/XrpLedgerSniperBot?start=ULN0HR`
  - `https://www.suite.tech/`
- Python 3.8 or higher
- Dependencies:
  - `tkinter` (included with Python)
  - `websockets`
  - `playsound` (only for macOS/Linux if sound functionality is needed)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/amm-pool-tracker.git
   cd amm-pool-tracker
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) For sound functionality on macOS/Linux, ensure you have `playsound` installed:
   ```bash
   pip install playsound
   ```

---

## Usage

1. Run the script:
   ```bash
   python amm_pool_tracker.py
   ```

2. To create a standalone executable (Windows only):
   ```bash
   pyinstaller --noconfirm --onefile --console amm_pool_tracker.py
   ```
   The executable will be located in the `dist` folder.

3. The application will:
   - Start logging in the terminal.
   - Display a pop-up notification with AMM pool details when a new pool is created.

---

## Configuration

The WebSocket connection is configured to connect to the XRPL mainnet:
```python
uri = "wss://s1.ripple.com"
```
To change to a different XRPL server, replace the URL in the code.

---

## Example Output

**Terminal Log**:
```
Listening for AMMCreate transactions...
AMM Pool Created:
 - Timestamp: 2024-12-04 10:15:30
 - Asset: USD
 - Issuer: rEXAMPLEISSUER
```

**Pop-up Window**:
- Displays timestamp, asset, and issuer.
- Includes buttons for:
  - **DEX Screener**
  - **Snipe Bot**
  - **First Ledger**

---

## Known Issues

- Ensure a stable internet connection for WebSocket to function properly.
- On macOS/Linux, you may need to configure `playsound` with an appropriate `.wav` file path.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add feature-name'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- [XRPL WebSocket API](https://xrpl.org/websocket-api-tool.html)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)

---

## Author

- **Your Name**  
  GitHub: [your-username](https://github.com/your-username)

