import re

with open('lib/telnet.c', 'r') as f:
    content = f.read()

content = content.replace("  size_t nwritten;\n  size_t len;\n  CURLcode result = CURLE_OK;", "  size_t len;\n  CURLcode result = CURLE_OK;")

with open('lib/telnet.c', 'w') as f:
    f.write(content)
