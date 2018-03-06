#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Simpleblocks
# Generated: Mon Mar  5 18:12:13 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class simpleBlocks(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Simpleblocks")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.summ = summ = 0
        self.samp_rate = samp_rate = 44100
        self.noiseEnable = noiseEnable = 0
        self.mult = mult = 0
        self.f2 = f2 = 100
        self.f1 = f1 = 100
        self.aN = aN = 1
        self.a2 = a2 = 0.2
        self.a1 = a1 = 0.2

        ##################################################
        # Blocks
        ##################################################
        self._summ_chooser = forms.drop_down(
        	parent=self.GetWin(),
        	value=self.summ,
        	callback=self.set_summ,
        	label="Sumar",
        	choices=[0, 1],
        	labels=[],
        )
        self.Add(self._summ_chooser)
        self._noiseEnable_chooser = forms.drop_down(
        	parent=self.GetWin(),
        	value=self.noiseEnable,
        	callback=self.set_noiseEnable,
        	label="Ruido Habilitado",
        	choices=[0, 1],
        	labels=[],
        )
        self.Add(self._noiseEnable_chooser)
        self._mult_chooser = forms.drop_down(
        	parent=self.GetWin(),
        	value=self.mult,
        	callback=self.set_mult,
        	label="Multiplicar",
        	choices=[0, 1],
        	labels=[],
        )
        self.Add(self._mult_chooser)
        _f2_sizer = wx.BoxSizer(wx.VERTICAL)
        self._f2_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_f2_sizer,
        	value=self.f2,
        	callback=self.set_f2,
        	label="Frecuencia 2",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._f2_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_f2_sizer,
        	value=self.f2,
        	callback=self.set_f2,
        	minimum=100,
        	maximum=samp_rate/4,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_f2_sizer)
        _f1_sizer = wx.BoxSizer(wx.VERTICAL)
        self._f1_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_f1_sizer,
        	value=self.f1,
        	callback=self.set_f1,
        	label="Frecuencia 1",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._f1_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_f1_sizer,
        	value=self.f1,
        	callback=self.set_f1,
        	minimum=100,
        	maximum=samp_rate/4,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_f1_sizer)
        _aN_sizer = wx.BoxSizer(wx.VERTICAL)
        self._aN_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_aN_sizer,
        	value=self.aN,
        	callback=self.set_aN,
        	label="Amplitud de Ruido",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._aN_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_aN_sizer,
        	value=self.aN,
        	callback=self.set_aN,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_aN_sizer)
        _a2_sizer = wx.BoxSizer(wx.VERTICAL)
        self._a2_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_a2_sizer,
        	value=self.a2,
        	callback=self.set_a2,
        	label="Amplitud 2",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._a2_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_a2_sizer,
        	value=self.a2,
        	callback=self.set_a2,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_a2_sizer)
        _a1_sizer = wx.BoxSizer(wx.VERTICAL)
        self._a1_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_a1_sizer,
        	value=self.a1,
        	callback=self.set_a1,
        	label="Amplitud 1",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._a1_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_a1_sizer,
        	value=self.a1,
        	callback=self.set_a1,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_a1_sizer)
        self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	dynamic_range=100,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=256,
        	fft_rate=60,
        	average=False,
        	avg_alpha=None,
        	title="Waterfall Plot",
        )
        self.Add(self.wxgui_waterfallsink2_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=256,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vcc((summ, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((mult, ))
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_add_xx_2 = blocks.add_vcc(1)
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.audio_sink_0 = audio.sink(samp_rate, "", True)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, f2, a2, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, f1, a1, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, aN*noiseEnable, 555)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_2, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_add_xx_2, 1))    
        self.connect((self.blocks_add_xx_2, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_add_xx_2, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.blocks_add_xx_2, 0), (self.wxgui_waterfallsink2_0, 0))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_1, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_1, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_complex_to_mag_0, 0))    

    def get_summ(self):
        return self.summ

    def set_summ(self, summ):
        self.summ = summ
        self._summ_chooser.set_value(self.summ)
        self.blocks_multiply_const_vxx_0_0.set_k((self.summ, ))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.wxgui_waterfallsink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)

    def get_noiseEnable(self):
        return self.noiseEnable

    def set_noiseEnable(self, noiseEnable):
        self.noiseEnable = noiseEnable
        self._noiseEnable_chooser.set_value(self.noiseEnable)
        self.analog_noise_source_x_0.set_amplitude(self.aN*self.noiseEnable)

    def get_mult(self):
        return self.mult

    def set_mult(self, mult):
        self.mult = mult
        self._mult_chooser.set_value(self.mult)
        self.blocks_multiply_const_vxx_0.set_k((self.mult, ))

    def get_f2(self):
        return self.f2

    def set_f2(self, f2):
        self.f2 = f2
        self._f2_slider.set_value(self.f2)
        self._f2_text_box.set_value(self.f2)
        self.analog_sig_source_x_0_0.set_frequency(self.f2)

    def get_f1(self):
        return self.f1

    def set_f1(self, f1):
        self.f1 = f1
        self._f1_slider.set_value(self.f1)
        self._f1_text_box.set_value(self.f1)
        self.analog_sig_source_x_0.set_frequency(self.f1)

    def get_aN(self):
        return self.aN

    def set_aN(self, aN):
        self.aN = aN
        self._aN_slider.set_value(self.aN)
        self._aN_text_box.set_value(self.aN)
        self.analog_noise_source_x_0.set_amplitude(self.aN*self.noiseEnable)

    def get_a2(self):
        return self.a2

    def set_a2(self, a2):
        self.a2 = a2
        self._a2_slider.set_value(self.a2)
        self._a2_text_box.set_value(self.a2)
        self.analog_sig_source_x_0_0.set_amplitude(self.a2)

    def get_a1(self):
        return self.a1

    def set_a1(self, a1):
        self.a1 = a1
        self._a1_slider.set_value(self.a1)
        self._a1_text_box.set_value(self.a1)
        self.analog_sig_source_x_0.set_amplitude(self.a1)


def main(top_block_cls=simpleBlocks, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
