import numpy as np
import scipy.sparse as sp
import pandas as pd

def sparse_to_edge_list_df(sparse_matrix):
    """
    Convert a sparse matrix (in COO format) to a DataFrame edge list.
    
    Args:
    - sparse_matrix (sp.coo_matrix): A scipy sparse matrix in COO format.
    
    Returns:
    - pd.DataFrame: A DataFrame with two columns 'source' and 'target' representing edges.
    """
    if not isinstance(sparse_matrix, sp.coo_matrix):
        sparse_matrix = sparse_matrix.tocoo()
    
    rows, cols = sparse_matrix.row, sparse_matrix.col
    
    edge_list = list(zip(rows, cols))
    df = pd.DataFrame(edge_list, columns=['source', 'target'])
    
    return df


def sparse_to_node_df(sparse_matrix):
    """
    Convert a sparse matrix (in COO format) to a DataFrame.
    
    Args:
    - sparse_matrix (sp.coo_matrix): A scipy sparse matrix in COO format.
    
    Returns:
    - pd.DataFrame: A DataFrame with two columns 'node' and 'label' 
    """
    if not isinstance(sparse_matrix, sp.coo_matrix):
        sparse_matrix = sparse_matrix.tocoo()
    
    rows, cols = sparse_matrix.row, sparse_matrix.col
    
    node_label = list(zip(rows, cols))
    df = pd.DataFrame(node_label , columns=['node', 'label'])
    
    return df
