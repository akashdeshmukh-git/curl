import re

with open('lib/telnet.c', 'r') as f:
    content = f.read()

content = content.replace("static CURLcode send_telnet_data(struct Curl_easy *data,\n                                 struct TELNET *tn,\n                                 const char *buffer, ssize_t nread);\n\n", "")

with open('lib/telnet.c', 'w') as f:
    f.write(content)
