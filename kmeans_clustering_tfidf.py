def kmeans_clustering_tfidf(doc_clean, cluster_num):

    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer()
    vec = vectorizer.fit(doc_clean)  
    df = vec.transform(doc_clean)

    # save the vector
    import pickle
    f = open('kmeans_vec.pkl', 'wb')
    pickle.dump(vec, f, pickle.HIGHEST_PROTOCOL)
    f.close()

    # KMeans model
    from sklearn.cluster import KMeans
    model = KMeans(n_clusters=cluster_num, random_state = 10).fit(df)

    # save the model 
    f = open('kmeans_model.pkl', 'wb')
    pickle.dump(model, f, pickle.HIGHEST_PROTOCOL)
    f.close()

    # output
    import pandas as pd
    dfT = pd.DataFrame(model.transform(df))
    dfT['sum of square'] = pd.DataFrame((dfT.min(axis = 1) ** 2)).rename(columns = {0: 'sum of square'})  
    dfT["cluster"] = model.labels_
    
    for seq in sorted(dfT.cluster.unique().tolist()):
        indexes = dfT[dfT.cluster == seq].index.values
        print 'cluster: #' + str(seq)     
        for i in indexes:
            print ' '.join(input_doc[i]) 
    
    return dfT.groupby('cluster')['sum of square'].agg(['sum', 'size', 'mean', 'std'])