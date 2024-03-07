from gn4pions.modules.data import GraphDataGenerator
from gn4pions.modules.models import MultiOutBlockModel

from gn4pions.modules.utils import convert_to_tuple

import glob
from graph_nets import utils_tf
import numpy as np
import yaml
import tensorflow as tf

if __name__ == '__main__':

    config = yaml.load(open("config.yaml"), Loader=yaml.FullLoader)

    #load the model configuration that was specified in the yaml config file
    model_config = config['model']
    model = MultiOutBlockModel(global_output_size=1, num_outputs=1, model_config=model_config)

    data_config = config['data']

    pion_files = np.sort(glob.glob('*.npy'))

    data_gen_train = GraphDataGenerator(pi0_file_list=None,
                                        pion_file_list=pion_files,
                                        cellGeo_file='/Users/markhodgkinson/ntupletonpy/cell_geo.root',
                                        batch_size=data_config['batch_size'],
                                        shuffle=data_config['shuffle'],
                                        num_procs=data_config['num_procs'],
                                        preprocess=data_config['preprocess'],
                                        output_dir=data_config['output_dir'])
    
    print("Data generator: ", data_gen_train)

    def get_batch(data_iter):
        print("Data iter: ", data_iter)
        for graphs, targets in data_iter:
            print("Graphs: ", graphs)
            targets = tf.convert_to_tensor(targets)
            graphs, energies, etas, em_probs, cluster_had_weights, truth_particle_es, truth_particle_pts, track_pts, track_etas, sum_cluster_es, sum_lcw_es = convert_to_tuple(graphs)
            yield graphs, targets, energies, etas, em_probs, cluster_had_weights, truth_particle_es, truth_particle_pts, track_pts, track_etas, sum_cluster_es, sum_lcw_es


    samp_graph, samp_target, _, _, _, _, _, _, _, _, _, _= next(get_batch(data_gen_train.generator()))
    #data_gen_train.kill_procs()
    print("A sample graph: ", samp_graph)
    graph_spec = utils_tf.specs_from_graphs_tuple(samp_graph, True, True, True)
    print("Graph spec: ", graph_spec)
