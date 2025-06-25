bash
#!/bin/bash
echo "Installing Requirements..."
pkg update -y && pkg install python -y
pip install requests beautifulsoup4
echo "Done. Run using: python extractor.py"