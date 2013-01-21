# IPython log file

get_ipython().magic(u'logstart source/_static/skrf_introduction.py')
from pylab import *
ion()
rcParams['savefig.dpi'] =120
rcParams['figure.figsize'] = [4,3]
rcParams['figure.subplot.left'] = 0.15
clf()
get_ipython().magic(u'bookmark -d ipy_savedir')
get_ipython().magic(u'bookmark ipy_savedir /mnt/ubuntu/home/alex/data/docs/code/scikit-rf/doc/source/_static')
import skrf as rf
get_ipython().system(u'ls -F --color ../skrf/data/ro*')
get_ipython().magic(u'bookmark -d ipy_savedir')
get_ipython().magic(u'bookmark ipy_savedir /mnt/ubuntu/home/alex/data/docs/code/scikit-rf/doc/source/_static')
rf.read_all('../skrf/data/', contains='ro')
get_ipython().magic(u'bookmark -d ipy_savedir')
get_ipython().magic(u'bookmark ipy_savedir /mnt/ubuntu/home/alex/data/docs/code/scikit-rf/doc/source/_static')
ro_dict = rf.read_all('../skrf/data/', contains='ro')
ro_ns = rf.NetworkSet(ro_dict, name='ro set') #name is optional
ro_ns
get_ipython().magic(u'bookmark -d ipy_savedir')
get_ipython().magic(u'bookmark ipy_savedir /mnt/ubuntu/home/alex/data/docs/code/scikit-rf/doc/source/_static')
ro_ns[0]
get_ipython().magic(u'bookmark -d ipy_savedir')
get_ipython().magic(u'bookmark ipy_savedir /mnt/ubuntu/home/alex/data/docs/code/scikit-rf/doc/source/_static')
ro_ns.plot_s_db()
import matplotlib.pyplot as plt
get_ipython().magic(u'bookmark ipy_thisdir')
get_ipython().magic(u'cd -b ipy_savedir')
plt.gcf().savefig("ns_plot_s_db.png")
get_ipython().magic(u'cd -b ipy_thisdir')
get_ipython().magic(u'bookmark -d ipy_thisdir')
get_ipython().magic(u'bookmark -d ipy_savedir')
get_ipython().magic(u'bookmark ipy_savedir /mnt/ubuntu/home/alex/data/docs/code/scikit-rf/doc/source/_static')
ro_ns.mean_s
get_ipython().magic(u'bookmark -d ipy_savedir')
get_ipython().magic(u'bookmark ipy_savedir /mnt/ubuntu/home/alex/data/docs/code/scikit-rf/doc/source/_static')
figure();
ro_ns.mean_s.plot_s_smith(r = .5)
import matplotlib.pyplot as plt
get_ipython().magic(u'bookmark ipy_thisdir')
get_ipython().magic(u'cd -b ipy_savedir')
plt.gcf().savefig("ns_mean_s_plot_s_smith.png")
get_ipython().magic(u'cd -b ipy_thisdir')
get_ipython().magic(u'bookmark -d ipy_thisdir')
get_ipython().magic(u'bookmark -d ipy_savedir')
get_ipython().magic(u'bookmark ipy_savedir /mnt/ubuntu/home/alex/data/docs/code/scikit-rf/doc/source/_static')
figure();
ro_ns.mean_s_deg.plot_s_re()
import matplotlib.pyplot as plt
get_ipython().magic(u'bookmark ipy_thisdir')
get_ipython().magic(u'cd -b ipy_savedir')
plt.gcf().savefig("ns_mean_s_deg.png")
get_ipython().magic(u'cd -b ipy_thisdir')
get_ipython().magic(u'bookmark -d ipy_thisdir')
get_ipython().magic(u'bookmark -d ipy_savedir')
get_ipython().magic(u'bookmark ipy_savedir /mnt/ubuntu/home/alex/data/docs/code/scikit-rf/doc/source/_static')
figure();
ro_ns.plot_uncertainty_bounds_s_db()
import matplotlib.pyplot as plt
get_ipython().magic(u'bookmark ipy_thisdir')
get_ipython().magic(u'cd -b ipy_savedir')
plt.gcf().savefig("ns_plot_uncertainty_bounds_s_db.png")
get_ipython().magic(u'cd -b ipy_thisdir')
get_ipython().magic(u'bookmark -d ipy_thisdir')
figure();
ro_ns.plot_uncertainty_bounds_s_deg()
import matplotlib.pyplot as plt
get_ipython().magic(u'bookmark ipy_thisdir')
get_ipython().magic(u'cd -b ipy_savedir')
plt.gcf().savefig("ns_plot_uncertainty_bounds_s_deg.png")
get_ipython().magic(u'cd -b ipy_thisdir')
get_ipython().magic(u'bookmark -d ipy_thisdir')
get_ipython().magic(u'bookmark -d ipy_savedir')
