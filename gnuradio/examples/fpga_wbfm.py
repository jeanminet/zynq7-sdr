#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Sun Feb  9 18:46:47 2014
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import test1

class top_block(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 80000

        ##################################################
        # Blocks
        ##################################################
        self.test1_dds_fpga_0 = test1.dds_fpga(8192*2, "/dev/iqram")
	
	self.fir_filter_xxx_0 = filter.rational_resampler_ccc(
	        interpolation=1, decimation=1, taps=None,
	       fractional_bw = None,
        )

        self.audio_sink_0 = audio.sink(samp_rate/5, "", True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=samp_rate,
        	audio_decimation=5
        )
        #self.analog_wfm_rcv_0.set_max_output_buffer(4096)

        ##################################################
        # Connections
        ##################################################
        #self.connect((self.test1_dds_fpga_0, 0), (self.analog_wfm_rcv_0, 0))
        #self.connect((self.analog_wfm_rcv_0, 0), (self.audio_sink_0, 0))
        self.connect((self.test1_dds_fpga_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.audio_sink_0, 0))


# QT sink close method reimplementation

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = top_block()
    tb.start()
    raw_input('Press Enter to quit: ')
    tb.stop()
    tb.wait()

