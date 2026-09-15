# 數學解題練習 (MathTutor)

台灣 **小一 ~ 高三** 的數學隨機出題練習程式。支援 **Windows / macOS / Linux / iOS / Android**。

## 下載

### 📱 手機版（iOS / Android / 任何瀏覽器）
- **網址：https://tangerserver.github.io/math-tutor/**
- 用手機瀏覽器（iPhone Safari / Android Chrome）開啟後選擇 **分享 → 加到主畫面**，即可像 App 一樣使用
- 離線可用，免安裝

### 💻 電腦版
前往 [Release 頁面](https://github.com/tangerserver/math-tutor/releases) 下載最新版：

| 平台 | 檔案 | 說明 |
|------|------|------|
| Windows | `MathTutor-Setup.exe` | 安裝程式（含自動更新） |
| Windows | `MathTutor.exe` | 免安裝版，直接執行 |
| macOS | `MathTutor-macOS.zip` | 解壓後拖入「應用程式」資料夾 |
| Linux | `MathTutor-Linux.zip` | 64 位元，需安裝 WebKit2GTK |

下載後即可使用，免安裝任何 Python 執行環境。

## 功能

- 12 個年級（小一 ~ 高三），涵蓋：
  - 加減乘除、九九乘法、分數、小數、因數倍數、圓面積、比例、百分率
  - 負數、一元一次方程式（含不等式）、畢氏定理、斜率、科學記號、判別式
  - 指數、對數、等差等比數列與級數、排列組合、矩陣、骰子機率、微積分入門
  - 生活應用題（購物、速率、利息、期望值…）
- **109 種題型**，隨機出題不重複
- **綜合練習**：跨年級隨機挑題，全面複習
- 多種答案輸入格式：整數、分數（`3/4`）、小數、座標（`3,-2`）、矩陣（`1,2;3,4`）
- 作答自動計時、統計正確率與連續答對題數
- **網頁級精美介面**：深色玻璃擬態設計、漸層動畫、流暢過場效果
- **自動更新**：啟動時檢查最新版本，有新版自動下載並更新

## 系統需求

### Windows
- Windows 10 / 11（64 位元）
- Microsoft Edge WebView2 Runtime（Windows 10/11 通常已內建）

### macOS
- macOS 11.0 以上（使用系統內建 WebKit）

### Linux
- 64 位元 Linux，需安裝 WebKit2GTK：
  - Debian/Ubuntu：`sudo apt install libwebkit2gtk-4.1-0`
  - Fedora：`sudo dnf install pango gdk-pixbuf2 libnotify webkit2gtk4.1`

### 手機
- iOS Safari 或 Android Chrome（現代瀏覽器即可）

## 使用方式

1. 下載並執行對應平台的程式（或開啟手機版網址）
2. 選擇年級與題型
3. 輸入答案後按 Enter 或「作答」按鈕

## 開發建置

- 桌面版使用 [pywebview](https://github.com/r0x0r/pywebview) + PyInstaller，跨平台由 GitHub Actions 自動編譯
- 手機版為 PWA（`docs/`），核心題庫引擎以 JavaScript 實作

## 授權

僅供個人教學與學習使用。