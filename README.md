# 數學解題練習 (MathTutor)

台灣 **小一 ~ 高三** 的數學隨機出題練習程式。支援 **Windows / macOS / Linux**。

## 下載

### Windows
- 安裝程式：`MathTutor-Setup.exe`（建議一般使用者下載）
- 免安裝版：直接執行 `MathTutor.exe`

### macOS / Linux
- 於 Release 頁面下載對應平台版本（`MathTutor-macOS.dmg` / `MathTutor-Linux`）
- Linux 需先安裝 `WebKit2GTK`（見下方說明）

下載後即可使用，免安裝任何 Python 執行環境。

## 功能

- 12 個年級（小一 ~ 高三），涵蓋：
  - 加減乘除、九九乘法、分數、小數、因數倍數、圓面積、比例、百分率
  - 負數、一元一次方程式（含不等式）、畢氏定理、斜率、科學記號、判別式
  - 指數、對數、等差等比數列與級數、排列組合、矩陣、骰子機率、微積分入門
- **85 種題型**，隨機出題不重複
- 多種答案輸入格式：整數、分數（`3/4`）、小數、座標（`3,-2`）、矩陣（`1,2;3,4`）
- 作答自動計時、統計正確率與連續答對題數
- **網頁級精美介面**：深色玻璃擬態設計、漸層動畫、流暢過場效果
- 啟動即為**最大化視窗**（佔滿工作區、不遮蔽工作列）

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

## 使用方式

1. 下載並執行對應平台的程式
2. 選擇年級與題型
3. 輸入答案後按 Enter 或「作答」按鈕

## 授權

僅供個人教學與學習使用。