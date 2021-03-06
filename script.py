import os


dataset = "All_Beauty"
METADATA = "Dataset/%s/meta_%s.json.gz"%(dataset, dataset)
REVIEWDATA = "Dataset/%s/reviews_%s.json.gz"%(dataset, dataset)
TITLEINFO = "Data/%s/title"%(dataset)
DESCRIPTIONINFO = "Data/%s/description"%(dataset)
TITLESIM = "Data/%s/title_similarity_matrix"%(dataset)
DESCRIPTIONSIM = "Data/%s/description_similarity_matrix"%(dataset)
USERSIM = "Data/%s/user_similarity_matrix"%(dataset)
TRAINNPZ = "Data/%s/iu_sparse_matrix_train.npz"%(dataset)
TESTNPZ = "Data/%s/iu_sparse_matrix_test.npz"%(dataset)
UID = "Data/%s/uid"%(dataset)
TRAINITEMID = "Data/%s/train_item_id"%(dataset)
TESTITEMID = "Data/%s/test_item_id"%(dataset)
TOPIC_NUM = 15
CLUSTER_NUM = 200
INIT_PARAM_TITLE = 1.0
INIT_PARAM_DESCRIPTION = 1.0
DEPTH_OF_TREE = 5
NON_LINEAR = "D:/GitCode/Dissertation/Data/%s/nonlinreg.mat"%(dataset)
USER_CLUSTER = "Data/%s/user_cluster_set"%(dataset)
USERCLUSTER_ITEM_RATING_MATRIX_TRAIN = "Data/%s/iuclst_rating_matrix_train"%(dataset)
USERCLUSTER_ITEM_RATING_MATRIX_TEST = "Data/%s/iuclst_rating_matrix_test"%(dataset)
ITEM_SIM_MATRIX = "Data/%s/item_sim_matrix"%(dataset)


print("##################   item_information.py   ####################")
os.system('python Step1-Preprocessing/item_information.py %s %s %s'%(METADATA, TITLEINFO, DESCRIPTIONINFO))
print("\n")
print("##################   user_information.py   ####################")
os.system('python Step1-Preprocessing/user_information.py %s %s %s %s %s %s %s'%(REVIEWDATA, TITLEINFO, TRAINNPZ, TESTNPZ, UID, TRAINITEMID, TESTITEMID))
print("\n")
print("##################   item_similarity.py   ####################")
os.system('python Step1-Preprocessing/item_similarity.py %s %s %s %s %s %s %s'%(TOPIC_NUM, TITLEINFO, DESCRIPTIONINFO, TRAINITEMID, TESTITEMID, TITLESIM, DESCRIPTIONSIM))
print("\n")
print("##################   similarity_parameters.py   ####################")
os.system('python Step1-Preprocessing/similarity_parameters.py %s %s %s %s %s %s %s'%(TITLESIM, DESCRIPTIONSIM, TRAINITEMID, TESTITEMID, TRAINNPZ, TESTNPZ, NON_LINEAR))
print("\n")
print("##################   user_similarity.py   ####################")
os.system('python Step1-Preprocessing/user_similarity.py %s %s %s'%(UID, TRAINNPZ, USERSIM))
print("\n")
print("##################   user_clustering.py   ####################")
os.system('python Step1-Preprocessing/user_clustering.py %s %s %s'%(USERSIM, CLUSTER_NUM, USER_CLUSTER))
print("\n")
print("##################   buildtree_preparation.py   ####################")
os.system('python Step1-Preprocessing/buildtree_preparation.py %s %s %s %s %s %s %s %s %s %s %s'%(TRAINNPZ, TESTNPZ, TITLESIM, DESCRIPTIONSIM, USER_CLUSTER, TRAINITEMID, TESTITEMID, NON_LINEAR, INIT_PARAM_TITLE, INIT_PARAM_DESCRIPTION, USERCLUSTER_ITEM_RATING_MATRIX, USERCLUSTER_ITEM_RATING_MATRIX_TEST, ITEM_SIM_MATRIX))
print("\n")
print("##################   build_tree.py   ####################")
os.system('python Step2-Model/build_tree.py %s %s %s %s %s'%(TRAINNPZ, TESTNPZ, USERCLUSTER_ITEM_RATING_MATRIX_TRAIN, USERCLUSTER_ITEM_RATING_MATRIX_TEST, USER_CLUSTER, DEPTH_OF_TREE))
print("\n")
