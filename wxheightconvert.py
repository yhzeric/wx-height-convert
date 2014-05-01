#!/usr/bin/env python
import wx
class NewFrame(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self, parent, wx.ID_ANY, "height unit converter")
        self.panel = wx.Panel(self)
        self.numberinput = wx.TextCtrl(self.panel, pos = (75,110))
        self.feetinput = wx.TextCtrl(self.panel, pos = (75,65))
        self.numberoutput = wx.StaticText(self.panel, pos = (215,100))
        self.textinput = wx.StaticText(self.panel, label = "inches", pos = (95,130))
        self.textoutput = wx.StaticText(self.panel, label = "centimeters", pos = (268,100))
        self.equalsign = wx.StaticText(self.panel, label = "=", pos = (190,100))
        self.footinput = wx.StaticText(self.panel, label = "feet", pos = (95,90))
        self.btnsubmit = wx.Button(self.panel, label = "submit", pos = (150,180))
        self.btnsubmit.Bind(wx.EVT_BUTTON, self.OnSubmit)
    def OnSubmit(self, e):
        self.numberget = self.numberinput.GetValue()
        self.numberget = float(self.numberget)
        self.numberfoot = self.feetinput.GetValue()
        self.numberfoot = float(self.numberfoot)
        self.numbercentimeters = (30.48*self.numberfoot+2.54*self.numberget)
        self.numbercentimeters = str(self.numbercentimeters)
        self.numberoutput.SetLabel(self.numbercentimeters)
app = wx.App(False)
frame = NewFrame(None)
frame.Show()
app.MainLoop()