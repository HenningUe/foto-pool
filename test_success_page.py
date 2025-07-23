#!/usr/bin/env python3
"""Simple test script to verify the success page implementation."""

import time
from pathlib import Path
import webbrowser
import sys

from auth2fa.web_server import TwoFAWebServer

# Add the shared package to path
sys.path.append(str(Path(__file__).parent / "shared" / "auth2fa" / "src"))


def test_success_page():
    """Test that the success page route is available."""

    print("🔧 Starting 2FA web server...")
    server = TwoFAWebServer(port_range=(8090, 8095))

    if not server.start():
        print("❌ Failed to start web server")
        return False

    print(f"✅ Web server started at: {server.get_url()}")
    print(f"🌐 Success page available at: {server.get_url()}/success")
    print("📋 Available routes:")
    print("  - / (main 2FA page)")
    print("  - /success (authentication success page)")
    print("  - /status (JSON status endpoint)")
    print("  - /styles.css (CSS styles)")

    # Let it run for a few seconds to allow manual testing
    print("\n⏳ Server running for 60 seconds for manual testing...")
    print("   You can open the URLs above in your browser to test")
    webbrowser.open(f"{server.get_url()}/success")
    time.sleep(60)

    server.stop()
    print("🛑 Web server stopped")
    return True


if __name__ == "__main__":
    test_success_page()
