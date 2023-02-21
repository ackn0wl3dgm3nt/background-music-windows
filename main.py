from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import socket
import sys


class Url:
    @staticmethod
    def get():
        with open("url.txt") as f:
            return f.readline()

    @staticmethod
    def set(url):
        with open("url.txt", "w") as f:
            f.write(url.replace('"', '').replace("'", ""))


class Player:
    @staticmethod
    def get_chrome_options():
        chrome_options = Options()
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.add_argument('--ignore-certificate-errors')

        chrome_options.add_argument("--log-level=3")
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--headless")
        return chrome_options

    @staticmethod
    def play(url):
        driver = webdriver.Chrome(options=Player.get_chrome_options())
        driver.get(url)
        driver.find_element(By.CLASS_NAME, "ytp-large-play-button").click()
        return driver

    @staticmethod
    def toggle_pause(driver):
        driver.find_element(By.CLASS_NAME, "ytp-play-button").click()


def main():
    player = Player.play(Url.get())
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 8880))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        action = conn.recv(1024).decode()
        action = action.split(" ")
        if action[0] == "toggle":
            Player.toggle_pause(player)
        if action[0] == "change":
            player.close()
            Url.set(action[1])
            player = Player.play(action[1])
        conn.close()


if __name__ == "__main__":
    main()
