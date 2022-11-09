#!/usr/bin/env python3.12
# -*- encoding: utf-8 -*-

import mechanize
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

user_agent = [('User-agent',
    'Mozilla/5.0 (X11;U;Linux 2.4.2.-2 i586; en-us;m18) Gecko/200010131 Netscape6/6.01'
)]

def main():
    try:
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.addheaders=user_agent
        page = br.open("https://www.veliumswap.com/signin")
        source_code = page.read()
        if b"Email" in source_code and b"Password" in source_code:
            print("We can proceed.")
        else:
            print("Something is wrong.")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
