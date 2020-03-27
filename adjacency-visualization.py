import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# PROBLEM 0
# a function that loads durbin.txt and returns it's file contents as a string
def load_durbin_data():
    durbin_data_path = './durbin.txt'
    durbin_text_data = ''
    with open(durbin_data_path) as durbin_file:
        durbin_text_data = durbin_file.read()

    return durbin_text_data

# PROBLEM 1
def print_repr(durbin_file_content_string):
    # change this to be the result of calling repr() on the durbin_file_content_string
    result = repr(durbin_file_content_string)

    print(result[:100])

# PROBLEM 2
def split_durbin_data_into_lines(durbin_text_string):
    # change this to return a list of strings where each string represents a line in the durbin text data

    return durbin_text_string.split('\n')


# PROBLEM 3
# s is of the form `A\tB\tC\tD\tE`
def tokenize_line(s):
    # change it to transform s into something like ['A', 'B', 'C', 'D', 'E' ]
    return s.split('\t')

# PROBLEM 4
# durbin_item_list will be something like ['ADAL', 'ADAR', 'Gap_junction', 'JSH', '2']
# or ['ADAL', 'AIBR', 'Send_joint', 'N2U', '2']
def is_gap_junction_info(durbin_item_list):
    # change this to return whether durbin_item_list is a gap junction info entry
    return durbin_item_list[2] == 'Gap_junction'

# gap_junction_info will be something like ['ADAL', 'ADAR', 'Gap_junction', 'JSH', '2']
# return ['ADAL', 'ADAR']
# https://docs.python.org/3/tutorial/datastructures.html
def get_gap_junction_neurons(gap_junction_info):

  return [ gap_junction_info[0], gap_junction_info[1] ]


if __name__ == '__main__':
    durbin_text = load_durbin_data()

    processed_data = [ tokenize_line(line) for line in split_durbin_data_into_lines(durbin_text) ]

    gap_junction_data = [ line for line in processed_data if is_gap_junction_info(line) ]

    graph = nx.Graph()

    for gj_info in gap_junction_data:
      neuron1, neuron2, _, _, weight = gj_info

      graph.add_node(neuron1)
      graph.add_node(neuron2)
      graph.add_edge(neuron1, neuron2, weight=int(weight))

    df = nx.convert_matrix.to_pandas_adjacency(graph)
    sns.heatmap(df)
    plt.show()