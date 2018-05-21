import matplotlib
matplotlib.use('nbAgg')  # i.e. %matplotlib notebook
import nslsii
import ophyd
from ophyd import Device, Component, EpicsSignal
try:
    del RE
except NameError:
    pass
nslsii.configure_base(get_ipython().user_ns, 'temp')


class Det(Device):
    det = Component(EpicsSignal, ':det', kind='hinted')
    exp = Component(EpicsSignal, ':exp', kind='config')


ph = Det('jitter_read:ph', name='ph')
edge = Det('jitter_read:edge', name='edge')
slit = Det('jitter_read:slit', name='slit')

motor_ph = EpicsSignal('jitter_read:ph:mtr', name='motor_ph')
motor_edge = EpicsSignal('jitter_read:edge:mtr', name='motor_edge')
motor_slit = EpicsSignal('jitter_read:slit:mtr', name='motor_slit')
