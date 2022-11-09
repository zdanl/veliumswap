def hi_chrome():
    # from xvfbwrapper import Xvfb
    from splinter import Browser
    # vdisplay = Xvfb()
    # vdisplay.start()

    print("spawning connector")
    oBrowser = Browser('chrome')
    oBrowser.visit("https://veliumswap.com/signin")
    assert oBrowser.title == "Google"
    print("yay")

    # vdisplay.stop()

if __name__ == '__main__':
    hi_chrome()
