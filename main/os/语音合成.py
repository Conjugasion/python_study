import win32com.client

Mark = win32com.client.Dispatch("SAPI.SPVOICE")
Mark.Speak("hello world")

