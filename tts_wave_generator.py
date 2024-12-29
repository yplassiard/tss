import wx
import os
import json
import pyttsx3

class PhraseDialog(wx.Dialog):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)
        self.phraseLabel = wx.StaticText(self, label="Phrase:")
        self.phraseText = wx.TextCtrl(self)
        self.keywordLabel = wx.StaticText(self, label="Keyword")
        self.keywordText = wx.TextCtrl(self)
        okButton = wx.Button(self, wx.ID_OK, "OK")
        cancelButton = wx.Button(self, wx.ID_CANCEL, "Cancel")
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        phraseSizer = wx.BoxSizer(wx.HORIZONTAL)
        phraseSizer.Add(self.phraseLabel, 0, wx.ALIGN_CENTER_VERTICAL)
        phraseSizer.Add(self.phraseText, 1, wx.EXPAND | wx.ALL, 5)
        mainSizer.Add(phraseSizer, 0, wx.EXPAND | wx.ALL, 5)
        
        keywordSizer = wx.BoxSizer(wx.HORIZONTAL)
        keywordSizer.Add(self.keywordLabel, 0, wx.ALIGN_CENTER_VERTICAL)
        keywordSizer.Add(self.keywordText, 1, wx.EXPAND | wx.ALL, 5)
        mainSizer.Add(keywordSizer, 0, wx.EXPAND | wx.ALL, 5)

        buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        buttonSizer.Add(okButton, 0, wx.ALL, 5)
        buttonSizer.Add(cancelButton, 0, wx.ALL, 5)
        mainSizer.Add(buttonSizer, 0, wx.ALIGN_RIGHT)

        self.SetSizer(mainSizer)
        self.Fit()

    def getValues(self):
        return (self.phraseText.GetValue(), self.keywordText.GetValue())
    
        
class ProgressDialog(wx.Dialog):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(300, 100))

        self.gauge = wx.Gauge(self, range=100)
        self.label = wx.StaticText(self, label="Generating files...")
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.label, 0, wx.ALL, 10)
        sizer.Add(self.gauge, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(sizer)
        self.Centre()
    def update(self, value, label=None):
        wx.CallAfter(self.gauge.SetValue, value)
        if label:
            wx.CallAfter(self.label.SetLabel, label)
        
        
class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        # Initialize pyttsx3 engine
        self.engine = pyttsx3.init()
        super(MyFrame, self).__init__(*args, **kwargs)

        self.pg = None
        self.panel = wx.Panel(self)

        # UI elements
        self.phrase_list = wx.ListCtrl(self.panel, style=wx.LC_REPORT)
        self.phrase_list.InsertColumn(0, "Phrases", width=400)

        self.add_button = wx.Button(self.panel, label="&Add Phrase")
        self.remove_button = wx.Button(self.panel, label="&Remove Phrase")
        self.generate_all_button = wx.Button(self.panel, label="Generate A&ll")
        self.generate_selected_button = wx.Button(self.panel, label="Generate &Selected")
        self.generate_numbers_button = wx.Button(self.panel, label="Generate numbers")
        self.generate_phrases_button = wx.Button(self.panel, label="Generate phrases")
        self.generate_stations_button = wx.Button(self.panel, label="Generate stations")
        
        self.preview_button = wx.Button(self.panel, label="Pre&view")

        self.voice_choice = wx.Choice(self.panel, choices=self.get_available_voices())
        self.voice_label = wx.StaticText(self.panel, label="Voice:")

        self.rate_slider = wx.Slider(self.panel, value=100, minValue=50, maxValue=200, style=wx.SL_HORIZONTAL)
        self.rate_label = wx.StaticText(self.panel, label="Rate:")

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.phrase_list, 1, wx.EXPAND | wx.ALL, 5)

        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(self.add_button, 0, wx.ALL, 5)
        button_sizer.Add(self.remove_button, 0, wx.ALL, 5)
        button_sizer.Add(self.generate_phrases_button, 0, wx.ALL, 5)
        button_sizer.Add(self.generate_numbers_button, 0, wx.ALL, 5)
        button_sizer.Add(self.generate_stations_button, 0, wx.ALL, 5)
        button_sizer.Add(self.generate_selected_button, 0, wx.ALL, 5)
        button_sizer.Add(self.generate_all_button, 0, wx.ALL, 5)
        button_sizer.Add(self.preview_button, 0, wx.ALL, 5)
        sizer.Add(button_sizer, 0, wx.ALIGN_CENTER)

        voice_sizer = wx.BoxSizer(wx.HORIZONTAL)
        voice_sizer.Add(self.voice_label, 0, wx.ALIGN_CENTER_VERTICAL)
        voice_sizer.Add(self.voice_choice, 0, wx.ALL, 5)
        sizer.Add(voice_sizer, 0, wx.ALIGN_CENTER)

        rate_sizer = wx.BoxSizer(wx.HORIZONTAL)
        rate_sizer.Add(self.rate_label, 0, wx.ALIGN_CENTER_VERTICAL)
        rate_sizer.Add(self.rate_slider, 1, wx.EXPAND)
        sizer.Add(rate_sizer, 0, wx.ALIGN_CENTER)

        self.panel.SetSizer(sizer)

        # Event bindings
        self.add_button.Bind(wx.EVT_BUTTON, self.on_add_phrase)
        self.remove_button.Bind(wx.EVT_BUTTON, self.on_remove_phrase)
        self.generate_all_button.Bind(wx.EVT_BUTTON, self.on_generate_all)
        self.generate_phrases_button.Bind(wx.EVT_BUTTON, self.on_generate_phrases)
        self.generate_numbers_button.Bind(wx.EVT_BUTTON, self.on_generate_numbers)
        self.generate_stations_button.Bind(wx.EVT_BUTTON, self.on_generate_stations)
        self.generate_selected_button.Bind(wx.EVT_BUTTON, self.on_generate_selected)
        self.preview_button.Bind(wx.EVT_BUTTON, self.on_preview)
        self.voice_choice.Bind(wx.EVT_CHOICE, self.on_voice_selected)
        self.rate_slider.Bind(wx.EVT_SLIDER, self.on_rate_changed)


        # Load phrases from file
        self.load_phrases()

    def get_available_voices(self):
        voices = self.engine.getProperty('voices')
        voice_names = [voice.name for voice in voices]
        return voice_names

    def load_phrases(self):
        try:
            with open("data/phrases.json", "r") as f:
                self.phrases = json.load(f)
                self.phrases.sort(key=lambda x: x['phrase'])
                for phrase in self.phrases:
                    index = self.phrase_list.InsertItem(self.phrase_list.GetItemCount(), f"{phrase['phrase']}; {phrase['keyword']}")

        except FileNotFoundError:
            self.phrases = []

    def save_phrases(self):
        with open("data/phrases.json", "w") as f:
            json.dump(self.phrases, f, indent=4)

    def on_add_phrase(self, event):
        dlg = PhraseDialog(self, "New phrase")
        if dlg.ShowModal() == wx.ID_OK:
            values = dlg.getValues()
            self.phrases.append({"phrase": values[0], "keyword": values[1]})
            index = self.phrase_list.InsertItem(self.phrase_list.GetItemCount(), f"{values[0]}; {values[1]}")
            self.save_phrases()
        dlg.Destroy()

    def on_remove_phrase(self, event):
        selected_index = self.phrase_list.GetFirstSelected()
        if selected_index != -1:
            self.phrase_list.DeleteItem(selected_index)
            del self.phrases[selected_index]
            self.save_phrases()

    def generate_numbers(self):
        self.pg.update(0, "Generating numbers ...")
        numbers = [x for x in range(1, 100)]
        numbers.extend([x for x in range(100, 1000, 100)])
        numbers.extend([x for x in range(1000, 100000, 1000)])
        numbers.extend([f"{x}h" for x in range(24)])
        pct = 0
        tlen = len(numbers)
        for number in numbers:
            self.pg.update(int(pct * 100 / tlen))
            if isinstance(number, str) and number.endswith("h"):
                self.generate_wave_file(number + "?", filename=number + "_1", path=os.path.join("data", "sounds", "numbers"))
                self.generate_wave_file(number + ".", filename=number + "_2", path=os.path.join("data", "sounds", "numbers"))
            else:
                self.generate_wave_file(str(number) + "?" if number < 100 else str(number) + ".", path=os.path.join("data", "sounds", "numbers"))
            pct += 1

    def generate_stations(self):
        try:
            with open(os.path.join(os.getcwd(), "data", "stations.json")) as f:
                stations = json.load(f)
                self.pg.update(0, f"Generating {len(stations)} sttion names...")
                tlen = len(stations)
                pct = 0
                for station in stations:
                    if station["voyageurs"] == "O":
                        self.generate_wave_file(station["libelle"], station["code_uic"], True, path=os.path.join("data", "sounds", "stations"))
                    self.pg.update(int(pct * 100 / tlen))
                    pct += 1
        except Exception as ex:
            print(ex)

    def generate_phrases(self):
        pct = 0
        tlen = self.phrase_list.GetItemCount()
        self.pg.update(0, "Generating phrases...")
        for phrase in self.phrases:
            self.pg.update(int(pct * tlen / 100))
            self.generate_wave_file(phrase["phrase"], phrase["keyword"], path=os.path.join("data", "sounds", "phrases"))
            pct += 1
    def on_generate_numbers(self, event):
        self.pg = ProgressDialog(self, title="Generating audio")
        self.pg.Show()
        self.generate_numbers()
        self.pg.Destroy()
        self.pg = None
    def on_generate_phrases(self, event):
        self.pg = ProgressDialog(self, title="Generating audio")
        self.pg.Show()
        self.generate_phrases()
        self.pg.Destroy()
        self.pg = None
    def on_generate_stations(self, event):
        self.pg = ProgressDialog(self, title="Generating audio")
        self.pg.Show()
        self.generate_stations()
        self.pg.Destroy()
        self.pg = None

    def on_generate_all(self, event):
        self.pg = ProgressDialog(self, title="Generating audio")
        self.pg.Show()
        self.generate_numbers()
        self.generate_stations()
        self.generate_phrases()
        self.pg.Destroy()
        self.pg = None
    def on_generate_selected(self, event):
        selected_index = self.phrase_list.GetFirstSelected()
        if selected_index != -1:
            phrase = self.phrases[selected_index]
            self.generate_wave_file(phrase["phrase"], phrase["keyword"])

    def on_preview(self, event):
        selected_index = self.phrase_list.GetFirstSelected()
        if selected_index != -1:
            phrase = self.phrases[selected_index]
            self.speak_phrase(phrase['phrase'])

    def generate_wave_file(self, phrase, filename=None, is_station=False, path=None):
        if not filename:
            filename = phrase
        if not path:
            path = os.path.join("data", "sounds")
        filename = filename.replace(" ", "_")
        filename = filename.replace("?", "")
        filename = filename.replace(".", "")
        filename += ".wav"
        self.generate(phrase, os.path.join(path, filename), is_station)
    def generate(self, phrase, filename, is_station):
        if not is_station:
            self.engine.setProperty('voice', self.voice_choice.GetStringSelection())
            self.engine.setProperty('rate', self.rate_slider.GetValue())
            self.engine.save_to_file(phrase, filename)
            self.engine.runAndWait()
        else:
            self.engine.setProperty('voice', self.voice_choice.GetStringSelection())
            self.engine.setProperty('rate', self.rate_slider.GetValue())
            file_1 = filename.replace(".wav", "_1.wav")
            phrase_1 = phrase + "?"
            self.engine.save_to_file(phrase_1, file_1)
            self.engine.runAndWait()
            phrase_2 = phrase + "."
            file_2 = filename.replace(".wav", "_2.wav")
            self.engine.save_to_file(phrase_2, file_2)
            self.engine.runAndWait()
            phrase_3 = ""
            if phrase[0].lower() in ['a', 'e', 'h', 'i' 'o', 'u', 'y']:
                phrase_3 = "D'" + phrase_1
            else:
                phrase_3 = f"De {phrase_1}"
            file_3 = filename.replace(".wav", "_3.wav")
            self.engine.save_to_file(phrase_3, file_3)
            self.engine.runAndWait()
            phrase_4 = phrase_3.replace("?", ".")
            file_4 = filename.replace(".wav", "_4.wav")
            self.engine.save_to_file(phrase_4, file_4)
            self.engine.runAndWait()
            

    def speak_phrase(self, phrase):
        self.engine.setProperty('voice', self.voice_choice.GetStringSelection())
        self.engine.setProperty('rate', self.rate_slider.GetValue())
        self.engine.say(phrase)
        self.engine.runAndWait()

    def on_voice_selected(self, event):
        pass

    def on_rate_changed(self, event):
        pass

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(None, title="TTS Wave File Generator", size=(500, 300))
    frame.Show()
    app.MainLoop()
