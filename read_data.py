from util import *


import os
import glob
path_data = os.getcwd()  + "/data/"


name2file_name = dict()
name2file_name.update({"blogcatalog"            :path_data + "blogcatalog.mat",
                       "homosapiens"            :path_data + "Homo_sapiens.mat",
                       "wikipos"                :path_data + "POS.mat",
                       "enron"                  :path_data + "enron/",
                       "unvote"                 :path_data + "UNvote/",
                       "untrade"                :path_data + "UNtrade/",
                       "uslegis_net"            :path_data + "congress-bills-full-proj-graph/",
                       "uslegis_net_small_dyn"  :path_data + "USLegis/",
                       "uslegis_net_dyn"        :path_data + "congress-bills/",
                       "uslegis_hyp_dyn"        :path_data + "congress-bills_hyp/",
                       "contacts"               :path_data + "Contacts/",
                       "dawn_net"               :path_data + "DAWN-proj-graph/",
                       "dawn_hyp"               :path_data + "DAWN/",
                       "ndc_net"                :path_data + "NDC-substances-full-proj-graph/",
                       "ndc_hyp"                :path_data + "NDC-substances-full/",
                       "coauth_dblp_net"         :path_data + "coauth-DBLP-full-proj-graph/",
                       "coauth_dblp_hyp"        :path_data + "coauth-DBLP-full/",
                       "wiod2016"               :path_data + "WIOD2016/",
                       "wiod2013"               :path_data + "WIOD2013/",
                       "wiodlong"               :path_data + "LongrunWIOD/",
                       "eth"                    :path_data + "eth/",
                       "bitcoinalpha"           :path_data,
                       "bitcoinotc"             :path_data,
                       "uscourt"                :path_data,
                      })



#
def get_data(name,original_format=False):

    # Initialize dictionary for outputs
    data_dict = dict()

    # Source
    # https://github.com/GemsLab/PhUSION/tree/master,
    # https://github.com/xptree/NetMF
    if name == "blogcatalog":

        # Load the .mat file
        import scipy.io
        file_name = name2file_name[name]
        mat_data = scipy.io.loadmat(file_name)

        # Just return original data
        if original_format == True:
            data_dict.update({"mat_data":mat_data})

        else:
            # Get node label information
            matrix_label = mat_data["group"]

            # Nodes
            df_nodes = sparse_to_node_df(matrix_label)
            df_nodes.sort_values(by="node",ascending=True,inplace=True)

            # Edgelist
            df_edges = sparse_to_edge_list_df(mat_data["network"])
            df_edges.sort_values(by=["source","target"],ascending=[True,True],inplace=True)

            # Update
            data_dict.update({"df_nodes":df_nodes,"df_edges":df_edges})

    # Source
    # https://github.com/GemsLab/PhUSION/tree/master,
    # https://github.com/xptree/NetMF
    elif name == "homosapiens":

        # Load the .mat file
        import scipy.io
        
        file_name = name2file_name[name]
        mat_data = scipy.io.loadmat(file_name)

        # Just return original data
        if original_format == True:
            data_dict.update({"mat_data":mat_data})

        else:
            # Get node label information
            matrix_label = mat_data["group"]

            # Nodes
            df_nodes = sparse_to_node_df(matrix_label)
            df_nodes.sort_values(by="node",ascending=True,inplace=True)

            # Edgelist
            df_edges = sparse_to_edge_list_df(mat_data["network"])
            df_edges.sort_values(by=["source","target"],ascending=[True,True],inplace=True)

            # Update
            data_dict.update({"df_nodes":df_nodes,"df_edges":df_edges})

    # Source
    # https://github.com/GemsLab/PhUSION/tree/master,
    # https://github.com/xptree/NetMF
    elif name == "wikipos":

        # Load the .mat file
        import scipy.io
        file_name = name2file_name[name]
        mat_data = scipy.io.loadmat(file_name)

        # Just return original data
        if original_format == True:
            data_dict.update({"mat_data":mat_data})

        else:
            # Get node label information
            matrix_label = mat_data["group"]

            # Nodes
            df_nodes = sparse_to_node_df(matrix_label)
            df_nodes.sort_values(by="node",ascending=True,inplace=True)

            # Edgelist
            df_edges = sparse_to_edge_list_df(mat_data["network"])
            df_edges.sort_values(by=["source","target"],ascending=[True,True],inplace=True)

            # Update
            data_dict.update({"df_nodes":df_nodes,"df_edges":df_edges})

    elif name == "enron":

        # ALL ZERO
        #file_name_1 = name2file_name[name] + "ml_enron_node.npy"
        #mat_1 = np.load(file_name_1)
        #file_name_2 = name2file_name[name] + "ml_enron.npy"
        #mat_2 = np.load(file_name_2)

        # Edge list
        file_name_3 = name2file_name[name] + "ml_enron.csv"
        df_edges = pd.read_csv(file_name_3)

        # Keep original format
        if original_format == True:
            pass
        # More human readable? format
        else:
            df_edges = df_edges[["idx","u","i","ts"]].copy()
            df_edges.columns = ["index","source","target","timestamp"]

        # Update
        data_dict.update({"df_edges":df_edges})

    elif name == "unvote":

        # ALL ZERO
        #file_name_1 = name2file_name[name] + "ml_UNvote_node.npy"
        #mat_1 = np.load(file_name_1)

        # Edge Features
        file_name_2 = name2file_name[name] + "ml_UNvote.npy"
        edge_features = np.load(file_name_2)

        # Edges
        file_name_3 = name2file_name[name]  + "ml_UNvote.csv"
        df_edges = pd.read_csv(file_name_3)

        # Keep original format
        if original_format:
            data_dict.update({"edge_features":edge_features})
            data_dict.update({"df_edges":df_edges})
        # More human readable? format
        else:
            df_edges = df_edges[["idx","u","i","ts"]].copy()
            df_edges.columns = ["index","source","target","timestamp"]
            df_edges["weight"] = list(edge_features[1:,0])
            data_dict.update({"df_edges":df_edges})


    elif name == "untrade":

        # ALL ZERO
        #file_name_1 = name2file_name[name] + "ml_UNtrade_node.npy"
        #mat_1 = np.load(file_name_1)

        # Edge Features
        file_name_2 = name2file_name[name] + "ml_UNtrade.npy"
        edge_features = np.load(file_name_2)

        # Edges
        file_name_3 = name2file_name[name]  + "ml_UNtrade.csv"
        df_edges = pd.read_csv(file_name_3)

        # Keep original format
        if original_format:
            data_dict.update({"edge_features":edge_features})
            data_dict.update({"df_edges":df_edges})
        # More human readable? format
        else:
            df_edges = df_edges[["idx","u","i","ts"]].copy()
            df_edges.columns = ["index","source","target","timestamp"]
            df_edges["weight"] = list(edge_features[1:,0])
            data_dict.update({"df_edges":df_edges})

    elif name == "uslegis_net":

        file_name_1 = name2file_name[name] + "congress-bills-full-node-labels.txt"
        df_nodes = pd.read_csv(file_name_1,sep="\t",header=None)
        df_nodes.columns = ["node","name"]

        file_name_2 = name2file_name[name] + "congress-bills-full-proj-graph.txt"
        df_edges = pd.read_csv(file_name_2,sep=" ",header=None)

        if original_format:
            df_edges.columns = ["i","j","w"]
        else:
            df_edges.columns = ["source","target","weight"]

        data_dict.update({"df_nodes":df_nodes,"df_edges":df_edges})


    elif name =="uslegis_net_small_dyn":

        # ALL ZERO
        #file_name_1 = name2file_name[name] + "ml_USLegis_node.npy"
        #mat_1 = np.load(file_name_1)

        # Edge feature
        file_name_2 = name2file_name[name] + "ml_USLegis.npy"
        edge_features = np.load(file_name_2)

        # Edge list
        file_name_3 = name2file_name[name]  + "ml_USLegis.csv"
        df_edges = pd.read_csv(file_name_3)

        # Keep original format
        if original_format:
            data_dict.update({"edge_features":edge_features})
            data_dict.update({"df_edges":df_edges})
        # More human readable? format
        else:
            df_edges = df_edges[["idx","u","i","ts"]].copy()
            df_edges.columns = ["index","source","target","timestamp"]
            df_edges["weight"] = list(edge_features[1:,0])
            data_dict.update({"df_edges":df_edges})


    elif name =="uslegis_net_dyn":
        # ALL ZERO
        #file_name_1 = name2file_name[name] + "ml_congress-bills_node.npy"
        #mat_1 = np.load(file_name_1)
        # Edge feature
        #file_name_2 = name2file_name[name] + "ml_congress-bills.npy"
        #edge_features = np.load(file_name_2)

        # Edge list
        file_name_3 = name2file_name[name]  + "ml_congress-bills.csv"
        df_edges = pd.read_csv(file_name_3)

        # Keep original format
        if original_format:
            data_dict.update({"df_edges":df_edges})
        # More human readable? format
        else:
            df_edges = df_edges[["idx","u","i","ts"]].copy()
            df_edges.columns = ["index","source","target","timestamp"]
            data_dict.update({"df_edges":df_edges})


    elif name == "uslegis_hyp_dyn":
        file_head = "congress-bills"
        # node name
        file_name_1 = name2file_name[name] + file_head + "-node-labels.txt"
        with open(file_name_1,"r") as f:
            v1 = f.readlines()
        out = []
        for i in range(len(v1)):
            v2 = v1[i].strip("\n").split("\t")
            out.append([int(v2[0]),v2[1]])
        df_nodes = pd.DataFrame(out)
        df_nodes.columns = ["node","name"]


        hyper_simplices = dict()
        hyper_time = dict()

        file_name_2 = name2file_name[name] + file_head + "-nverts.txt"
        with open(file_name_2,"r") as f:
            vec_num = f.readlines()

        file_name_3 = name2file_name[name] + file_head + "-times.txt"
        with open(file_name_3,"r") as f:
            vec_times = f.readlines()

        file_name_4 = name2file_name[name] + file_head + "-simplices.txt"
        with open(file_name_4,"r") as f:
            simplices = f.readlines()

        cnt = 0
        for i in range(len(vec_num)):

            num_vert = int(vec_num[i].strip("\n"))
            vec_tmp = simplices[cnt:cnt+num_vert]
            for j in range(len(vec_tmp)):
                vec_tmp[j] = int(vec_tmp[j].strip("\n"))
            hyper_simplices.update({i:vec_tmp})
            hyper_time.update({i:int(vec_times[i].strip("\n"))})
            cnt = cnt + num_vert

        data_dict.update({"df_nodes":df_nodes,"hyper_simplices":hyper_simplices,"hyper_time":hyper_time})


    elif name == "contacts":
        # ALL ZERO
        #file_name_1 = name2file_name[name] + "ml_Contacts_node.npy"
        #mat_1 = np.load(file_name_1)

        # Edge Features
        file_name_2 = name2file_name[name] + "ml_Contacts.npy"
        edge_features = np.load(file_name_2)


        # Edges
        file_name_3 = name2file_name[name]  + "ml_Contacts.csv"
        df_edges = pd.read_csv(file_name_3)

         # Keep original format
        if original_format:
            data_dict.update({"edge_features":edge_features})
            data_dict.update({"df_edges":df_edges})
        # More human readable? format
        else:
            df_edges = df_edges[["idx","u","i","ts"]].copy()
            df_edges.columns = ["index","source","target","timestamp"]
            df_edges["weight"] = list(edge_features[1:,0])
            data_dict.update({"df_edges":df_edges})

    elif name == "coauth_dblp_net":

        file_name_1 = name2file_name[name] + "coauth-DBLP-full-node-labels.txt"
        with open(file_name_1,"r") as f:
            v1 = f.readlines()
        out = []
        for i in range(len(v1)):
            v2 = v1[i].strip("\n").split(" ")
            out.append([v2[0],"" .join(v2[1:])])
        df_nodes = pd.DataFrame(out)
        df_nodes.columns = ["node","name"]
        file_name_2 = name2file_name[name] + "coauth-DBLP-full-proj-graph.txt"
        df_edges = pd.read_csv(file_name_2,sep=" ",header=None)
        if original_format:
            df_edges.columns = ["i","j","w"]
        else:
            df_edges.columns = ["source","target","weight"]

        data_dict.update({"df_nodes":df_nodes,"df_edges":df_edges})

    elif name == "coauth_dblp_hyp":

        file_head = "coauth-DBLP-full"
        # node name
        file_name_1 = name2file_name[name] + file_head + "-node-labels.txt"
        with open(file_name_1,"r") as f:
            v1 = f.readlines()
        out = []
        for i in range(len(v1)):
            v2 = v1[i].strip("\n").split(" ")
            out.append([v2[0]," ".join(v2[1:])])
        df_nodes = pd.DataFrame(out)
        df_nodes.columns = ["node","name"]

        hyper_simplices = dict()
        hyper_time = dict()

        file_name_2 = name2file_name[name] + file_head + "-nverts.txt"
        with open(file_name_2,"r") as f:
            vec_num = f.readlines()

        file_name_3 = name2file_name[name] + file_head + "-times.txt"
        with open(file_name_3,"r") as f:
            vec_times = f.readlines()

        file_name_4 = name2file_name[name] + file_head + "-simplices.txt"
        with open(file_name_4,"r") as f:
            simplices = f.readlines()

        cnt = 0
        for i in range(len(vec_num)):
            num_vert = int(vec_num[i].strip("\n"))
            vec_tmp = simplices[cnt:cnt+num_vert]
            for j in range(len(vec_tmp)):
                vec_tmp[j] = int(vec_tmp[j].strip("\n"))
            hyper_simplices.update({i:vec_tmp})
            hyper_time.update({i:int(vec_times[i].strip("\n"))})
            cnt = cnt + num_vert

        data_dict.update({"df_nodes":df_nodes,"hyper_simplices":hyper_simplices,"hyper_time":hyper_time})

    elif name == "dawn_net":

        file_name_1 = name2file_name[name] + "DAWN-node-labels.txt"
        with open(file_name_1,"r") as f:
            v1 = f.readlines()
        out = []
        for i in range(len(v1)):
            v2 = v1[i].strip("\n").split(" ")
            out.append([v2[0],v2[1]," ".join(v2[2:])])
        df_nodes = pd.DataFrame(out)
        df_nodes.columns = ["node","name","description"]
        file_name_2 = name2file_name[name] + "DAWN-proj-graph.txt"
        df_edges = pd.read_csv(file_name_2,sep=" ",header=None)
        if original_format:
            df_edges.columns = ["i","j","w"]
        else:
            df_edges.columns = ["source","target","weight"]

        data_dict.update({"df_nodes":df_nodes,"df_edges":df_edges})


    elif name == "dawn_hyp":
        file_head = "DAWN"
        # node name
        file_name_1 = name2file_name[name] + file_head + "-node-labels.txt"
        with open(file_name_1,"r") as f:
            v1 = f.readlines()
        out = []
        for i in range(len(v1)):
            v2 = v1[i].strip("\n").split(" ")
            out.append([v2[0],v2[1],v2[2]])
        df_nodes = pd.DataFrame(out)
        df_nodes.columns = ["node","name","description"]

        hyper_simplices = dict()
        hyper_time = dict()

        file_name_2 = name2file_name[name] + file_head + "-nverts.txt"
        with open(file_name_2,"r") as f:
            vec_num = f.readlines()

        file_name_3 = name2file_name[name] + file_head + "-times.txt"
        with open(file_name_3,"r") as f:
            vec_times = f.readlines()

        file_name_4 = name2file_name[name] + file_head + "-simplices.txt"
        with open(file_name_4,"r") as f:
            simplices = f.readlines()

        cnt = 0
        for i in range(len(vec_num)):
            num_vert = int(vec_num[i].strip("\n"))
            vec_tmp = simplices[cnt:cnt+num_vert]
            for j in range(len(vec_tmp)):
                vec_tmp[j] = int(vec_tmp[j].strip("\n"))
            hyper_simplices.update({i:vec_tmp})
            hyper_time.update({i:int(vec_times[i].strip("\n"))})
            cnt = cnt + num_vert

        data_dict.update({"df_nodes":df_nodes,"hyper_simplices":hyper_simplices,"hyper_time":hyper_time})

    elif name == "ndc_net":
        file_name_1 = name2file_name[name] + "NDC-substances-full-node-labels.txt"
        with open(file_name_1,"r") as f:
            v1 = f.readlines()

        out = []
        for i in range(len(v1)):
            v2 = v1[i].strip("\n").split(" ")
            out.append([v2[0]," ".join(v2[1:])])
        df_nodes = pd.DataFrame(out)
        df_nodes.columns = ["node","name"]
        file_name_2 = name2file_name[name] + "NDC-substances-full-proj-graph.txt"
        df_edges = pd.read_csv(file_name_2,sep=" ",header=None)
        if original_format:
            df_edges.columns = ["i","j","w"]
        else:
            df_edges.columns = ["source","target","weight"]

        data_dict.update({"df_nodes":df_nodes,"df_edges":df_edges})

    elif name == "ndc_hyp":
        file_head = "NDC-substances"
        # node name
        file_name_1 = name2file_name[name] + file_head + "-full-node-labels.txt"
        with open(file_name_1,"r") as f:
            v1 = f.readlines()
        out = []
        for i in range(len(v1)):
            v2 = v1[i].strip("\n").split(" ")
            out.append([v2[0]," ".join(v2[1:])])
        df_nodes = pd.DataFrame(out)
        df_nodes.columns = ["node","name"]

        hyper_simplices = dict()
        hyper_time = dict()
        hyper_labels = dict()

        file_name_2 = name2file_name[name] + file_head + "-full-nverts.txt"
        with open(file_name_2,"r") as f:
            vec_num = f.readlines()


        file_name_3 = name2file_name[name] + file_head + "-full-times.txt"
        with open(file_name_3,"r") as f:
            vec_times = f.readlines()

        file_name_4 = name2file_name[name] + file_head + "-full-simplices.txt"
        with open(file_name_4,"r") as f:
            simplices = f.readlines()

        file_name_5 = name2file_name[name] + file_head + "-full-simplex-labels.txt"
        with open(file_name_5,"r") as f:
            simplex_labels = f.readlines()

        cnt = 0
        for i in range(len(vec_num)):
            num_vert = int(vec_num[i].strip("\n"))
            vec_tmp = simplices[cnt:cnt+num_vert]
            for j in range(len(vec_tmp)):
                vec_tmp[j] = int(vec_tmp[j].strip("\n"))
            hyper_simplices.update({i:vec_tmp})
            hyper_time.update({i:int(vec_times[i].strip("\n"))})
            hyper_labels.update({i:simplex_labels[i]})
            cnt = cnt + num_vert

        data_dict.update({"df_nodes":df_nodes,"hyper_simplices":hyper_simplices,"hyper_time":hyper_time,
                         "hyper_labels":hyper_labels})

    elif name == "wiod2016":

        #file_list_edge = glob.glob(name2file_name[name] + "/*_edgelist.csv")
        #file_list_edge.sort()
        #df_list = []
        #for i in range(len(file_list_edge)):
        #    year = int(file_list_edge[i].split("/")[-1].split("_")[0].strip("WIOT"))
        #    df_tmp = pd.read_csv(file_list_edge[i],header=None)
        #    df_tmp["time"] = year
        #    df_list.append(df_tmp)
        #df_edges = pd.concat(df_list)
        #df_edges.columns = ["source","target","weight","time"]
        #file_list_index = glob.glob(name2file_name[name] + "*_index2nodes.csv")
        #file_list_index.sort()
        #df_list = []
        #for i in range(len(file_list_index)):
        #    year = int(file_list_index[i].split("/")[-1].split("_")[0].strip("WIOT"))
        #    df_tmp = pd.read_csv(file_list_index[i])
        #    df_tmp["time"] = year
        #    df_list.append(df_tmp)
        #df_nodes = pd.concat(df_list)
        #df_nodes.columns = ["node","name","time"]
        
        df_edges = pd.read_csv(name2file_name[name] + "wiod2016_all_edges.csv")
        df_nodes = pd.read_csv(name2file_name[name] + "wiod2016_all_nodes.csv")
        data_dict.update({"df_nodes":df_nodes,"df_edges":df_edges})
        

    elif name == "wiod2013":
        #file_list_edge = glob.glob(name2file_name[name] + "/*_edgelist.csv")
        #file_list_edge.sort()

        #df_list = []
        #for i in range(len(file_list_edge)):
        #    year = int(file_list_edge[i].split("/")[-1].split("_")[0].strip("WIOT"))
        #    df_tmp = pd.read_csv(file_list_edge[i],header=None)
        #    df_tmp["time"] = year
        #    df_list.append(df_tmp)

        #df_edges = pd.concat(df_list)
        #df_edges.columns = ["source","target","weight","time"]

        #file_list_index = glob.glob(name2file_name[name] + "*_index2nodes.csv")
        #file_list_index.sort()

        #df_list = []
        #for i in range(len(file_list_index)):
        #    year = int(file_list_index[i].split("/")[-1].split("_")[0].strip("WIOT"))
        #    df_tmp = pd.read_csv(file_list_index[i])
        #    df_tmp["time"] = year
        #    df_list.append(df_tmp)

        #df_nodes = pd.concat(df_list)
        #df_nodes.columns = ["node","name","time"]
        df_edges = pd.read_csv(name2file_name[name] + "wiod2013_all_edges.csv")
        df_nodes = pd.read_csv(name2file_name[name] + "wiod2013_all_nodes.csv")
        data_dict.update({"df_nodes":df_nodes,"df_edges":df_edges})


    elif name == "wiodlong":

        file_name_1 = name2file_name[name] + "LongrunWIOD_index2nodes.csv"
        df_nodes = pd.read_csv(file_name_1)
        df_nodes.columns = ["node","name"]

        file_name_2 = name2file_name[name] + "LongrunWIOD_edgelist.csv"
        df_edges = pd.read_csv(file_name_2,header=None)
        df_edges.columns = ["time","source","target","weight"]

        data_dict.update({"df_nodes":df_nodes,"df_edges":df_edges})


    elif name == "eth":

        file_name = name2file_name[name]
        # Retrieve address unifer
        df_unifier = pd.read_csv(file_name  + "/all_ens_pairs.csv")
        address2node = dict()
        for i in range(len(df_unifier)):
            address2node.update({df_unifier["address"].iloc[i]:df_unifier["name"].iloc[i]})

        df_edges = pd.read_csv(file_name + "/raw_normal_txs.csv")

        df_edges["from_uni"] = df_edges["from"].map(address2node)
        df_edges["to_uni"] = df_edges["to"].map(address2node)

        df_edges_sub = df_edges.dropna(subset=['from_uni', 'to_uni'])

        with open(file_name + "/labeledAddresses.json") as f:
            lines = f.read()

        import json
        category = json.loads(lines)

        list_df = []
        for i in category.keys():
            df_tmp = pd.DataFrame(category[i])
            df_tmp["category"] = i

            list_df.append(df_tmp)
        df_nodes_known = pd.concat(list_df)
        df_nodes_known.columns = ["address","name","category"]

        if original_format:
            data_dict.update({"df_edges":df_edges})
        else:
            df_edges = df_edges[["from","to","timeStamp","value"]].copy()
            df_edges.columns = ["source","target","time","weight"]
            df_edges_sub = df_edges_sub[["from_uni","to_uni","timeStamp","value"]].copy()
            df_edges_sub.columns = ["source","target","time","weight"]
            data_dict.update({"df_edges":df_edges,"df_edges_sub":df_edges_sub,"df_nodes_known":df_nodes_known})

    elif name == "bitcoinalpha":
        file_name = name2file_name[name]
        df_edges = pd.read_csv(file_name + "soc-sign-bitcoinalpha.csv",header=None)
        df_edges.columns = ["source","target","weight","time"]
        data_dict.update({"df_edges":df_edges})

    elif name == "bitcoinotc":
        file_name = name2file_name[name]
        df_edges = pd.read_csv(file_name + "soc-sign-bitcoinotc.csv",header=None)
        df_edges.columns = ["source","target","weight","time"]
        data_dict.update({"df_edges":df_edges})

    elif name == "uscourt":
        file_name = name2file_name[name]
        df_edges = pd.read_csv(name2file_name[name] + "us_court_500_edges.csv")
        df_nodes = pd.read_csv(name2file_name[name] + "us_court_500_nodes.csv")
        data_dict.update({"df_edges":df_edges,"df_nodes":df_nodes})
    else:
        print("Please enter correct data name")
        print(name2file_name.keys())


    return data_dict
