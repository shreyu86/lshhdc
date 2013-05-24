import os.path

import lshhdc.cluster
import lshhdc.utils


def test_names():
    data_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')
    names = open('{}/{}'.format(data_dir, 'sample-data.txt'), 'r').readlines()
    names = [name.strip().lower().replace('\n', '') for name in names if name]
    cluster = lshhdc.cluster.Cluster(threshold=0.5)
    for name in set(names):
        cluster.add_set(lshhdc.utils.shingle(name, 5), name)
    assert len(cluster.get_sets()) == 6


