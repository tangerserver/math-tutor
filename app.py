# -*- coding: utf-8 -*-
import json
import os
import random
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import urllib.request
import webbrowser

import webview

from core import G, check

APP_VERSION = "2.4.0"
WINDOW_TITLE = "數學解題練習 · 小一 ~ 高三"
RELEASE_API = "https://api.github.com/repos/tangerserver/math-tutor/releases/latest"


def version_tuple(v):
    try:
        return tuple(int(x) for x in v.lstrip("vV").split(".")[:3])
    except Exception:
        return (0, 0, 0)


def newer_than(remote, local):
    return version_tuple(remote) > version_tuple(local)


def resource(name):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, name)


def dark_title_bar():
    if sys.platform != "win32":
        return
    import ctypes

    user32 = ctypes.windll.user32
    dwmapi = ctypes.windll.dwmapi
    hwnd = 0
    for _ in range(300):
        hwnd = user32.FindWindowW(None, WINDOW_TITLE)
        if hwnd:
            break
        time.sleep(0.05)
    if not hwnd:
        return
    dark = ctypes.c_int(1)
    caption = ctypes.c_uint(0x00000000)
    text = ctypes.c_uint(0x00F0E8E2)
    for _ in range(20):
        for attr in (20, 19):
            dwmapi.DwmSetWindowAttribute(hwnd, attr, ctypes.byref(dark), ctypes.sizeof(dark))
        dwmapi.DwmSetWindowAttribute(hwnd, 35, ctypes.byref(caption), ctypes.sizeof(caption))
        dwmapi.DwmSetWindowAttribute(hwnd, 36, ctypes.byref(text), ctypes.sizeof(text))
        time.sleep(0.15)


class Api:
    def __init__(self):
        self.correct = 0
        self.total = 0
        self.streak = 0
        self.total_time = 0.0
        self.cur_answer = ""
        self.start = 0.0
        self.locked = False
        self.just_updated = "--updated" in sys.argv

    def grades(self):
        out = []
        for g, ts in G.items():
            out.append({"grade": g, "topics": ["綜合練習"] + [t for t, _ in ts]})
        return out

    def new_question(self, grade, topic):
        topics = G.get(grade, [])
        fn = None
        picked = topic
        if topic == "綜合練習":
            for _ in range(8):
                cand = random.choice(topics)
                if cand[0] != getattr(self, "_last_topic", None):
                    break
            picked, fn = cand[0], cand[1]
        else:
            for name, f in topics:
                if name == topic:
                    fn = f
                    break
            if fn is None and topics:
                fn, picked = topics[0][1], topics[0][0]
        self._last_topic = picked
        q, a = fn()
        self.cur_answer = a
        self.start = time.time()
        self.locked = False
        return {"question": q, "topic": picked, "grade": grade}

    def submit(self, answer):
        if self.locked:
            return None
        self.locked = True
        elapsed = time.time() - self.start
        self.total += 1
        self.total_time += elapsed
        ok = check(answer, self.cur_answer)
        if ok:
            self.correct += 1
            self.streak += 1
        else:
            self.streak = 0
        return {"ok": ok, "correct_answer": self.cur_answer, "elapsed": round(elapsed, 1),
                "stats": self.stats()}

    def reveal(self):
        return {"answer": self.cur_answer}

    def reset(self):
        self.correct = 0
        self.total = 0
        self.streak = 0
        self.total_time = 0.0
        return {"stats": self.stats()}

    def stats(self):
        wrong = self.total - self.correct
        rate = round(self.correct / self.total * 100) if self.total else 0
        avg = round(self.total_time / self.total, 1) if self.total else None
        return {"correct": self.correct, "wrong": wrong, "rate": rate,
                "streak": self.streak, "avg": avg, "total": self.total}

    def version(self):
        return {"version": APP_VERSION}

    def updated(self):
        return {"just_updated": self.just_updated, "version": APP_VERSION}

    def open_update(self, url):
        try:
            webbrowser.open(url)
            return True
        except Exception:
            return False

    def install_update(self, asset_url):
        try:
            dst = os.path.join(tempfile.gettempdir(), "MathTutor-Setup-latest.exe")
            req = urllib.request.Request(asset_url, headers={"User-Agent": "MathTutor"})
            with urllib.request.urlopen(req, timeout=180) as r, open(dst, "wb") as f:
                shutil.copyfileobj(r, f)
            try:
                subprocess.Popen([dst, "/S"])
            except Exception:
                os.startfile(dst)
            webview.exit()
            return True
        except Exception:
            self.open_update(asset_url)
            return False


def check_updates(win):
    try:
        req = urllib.request.Request(
            RELEASE_API,
            headers={"User-Agent": "MathTutor", "Accept": "application/vnd.github+json"},
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        remote = str(data.get("tag_name", ""))
        setup_url = ""
        assets = data.get("assets", []) or []
        for a in assets:
            if str(a.get("name", "")).lower().startswith("mathtutor-setup") or \
               a.get("name", "") == "MathTutor-Setup.exe":
                setup_url = a.get("browser_download_url", "")
                break
        if newer_than(remote, APP_VERSION):
            payload = json.dumps({
                "version": remote,
                "page_url": data.get("html_url", RELEASE_API),
                "asset_url": setup_url,
            })
            for _ in range(15):
                try:
                    win.evaluate_js("window.showUpdate(%s)" % payload)
                    return
                except Exception:
                    time.sleep(1)
    except Exception:
        pass


def main():
    api = Api()
    win = webview.create_window(
        title=WINDOW_TITLE,
        url=resource("ui.html"),
        js_api=api,
        min_size=(960, 660),
        background_color="#0b1120",
        text_select=False,
        maximized=True,
    )
    threading.Thread(target=dark_title_bar, daemon=True).start()
    check_updates_thread = threading.Thread(target=check_updates, args=(win,), daemon=True)
    check_updates_thread.start()
    win.events.shown += win.maximize
    webview.start()


if __name__ == "__main__":
    main()
