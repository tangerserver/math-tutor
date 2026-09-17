Unicode true
!include "MUI2.nsh"

!define APP_NAME "數學解題練習"
!define APP_NAME_SHORT "MathTutor"
!define APP_VERSION "2.4.0"
!define APP_EXE "MathTutor.exe"
!define APP_PUBLISHER "MathTutor"

Name "${APP_NAME}"
OutFile "dist\MathTutor-Setup.exe"
InstallDir "$PROGRAMFILES64\${APP_NAME_SHORT}"
InstallDirRegKey HKLM "Software\${APP_NAME_SHORT}" "InstallDir"
RequestExecutionLevel admin
SetCompressor /SOLID lzma

Function .onInit
  nsExec::ExecToLog 'taskkill /IM MathTutor.exe /F /T'
FunctionEnd

!define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\modern-install.ico"
!define MUI_UNICON "${NSISDIR}\Contrib\Graphics\Icons\modern-uninstall.ico"
!define MUI_ABORTWARNING
!define MUI_FINISHPAGE_RUN "$INSTDIR\${APP_EXE}"
!define MUI_FINISHPAGE_RUN_TEXT "立即啟動 ${APP_NAME}"

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

!insertmacro MUI_LANGUAGE "TradChinese"

Section "主程式" SEC_MAIN
    SetOutPath "$INSTDIR"
    File "dist\${APP_EXE}"

    WriteUninstaller "$INSTDIR\Uninstall.exe"

    CreateDirectory "$SMPROGRAMS\${APP_NAME_SHORT}"
    CreateShortcut "$SMPROGRAMS\${APP_NAME_SHORT}\${APP_NAME}.lnk" "$INSTDIR\${APP_EXE}"
    CreateShortcut "$SMPROGRAMS\${APP_NAME_SHORT}\解除安裝.lnk" "$INSTDIR\Uninstall.exe"
    CreateShortcut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\${APP_EXE}"

    IfSilent 0 nosilentrun
    Exec '"$INSTDIR\${APP_EXE}" --updated'
    nosilentrun:

    WriteRegStr HKLM "Software\${APP_NAME_SHORT}" "InstallDir" "$INSTDIR"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME_SHORT}" "DisplayName" "${APP_NAME}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME_SHORT}" "DisplayVersion" "${APP_VERSION}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME_SHORT}" "Publisher" "${APP_PUBLISHER}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME_SHORT}" "DisplayIcon" "$INSTDIR\${APP_EXE}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME_SHORT}" "UninstallString" "$INSTDIR\Uninstall.exe"
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME_SHORT}" "NoModify" 1
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME_SHORT}" "NoRepair" 1
SectionEnd

Section "Uninstall"
    Delete "$INSTDIR\Uninstall.exe"
    Delete "$INSTDIR\${APP_EXE}"
    RMDir "$INSTDIR"

    Delete "$SMPROGRAMS\${APP_NAME_SHORT}\${APP_NAME}.lnk"
    Delete "$SMPROGRAMS\${APP_NAME_SHORT}\解除安裝.lnk"
    RMDir "$SMPROGRAMS\${APP_NAME_SHORT}"
    Delete "$DESKTOP\${APP_NAME}.lnk"

    DeleteRegKey HKLM "Software\${APP_NAME_SHORT}"
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME_SHORT}"
SectionEnd