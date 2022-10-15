import time

import pyLDAvis
import pyLDAvis.gensim_models as gensimvis

from src.model.tools_modelling import (_format_topics_sentences,
                                       compute_bag_of_words, compute_lda,
                                       compute_word_cloud, graph_topics,
                                       search_nb_topics)


def run_all(df_tweets, text, alias, do_search_best_topics, nb_topics=0):

    # filter only the necessary columns and drop nan
    df_tweets = df_tweets[["tweet_id", "text", "username", text]]
    df_tweets = df_tweets[~(df_tweets[text].isna())]
    df_tweets = df_tweets.reset_index()

    start_run = time.time()
    print(f"===== Method : {alias} =====")
    print("... Running bag of words")
    text_tokens, dico_words, doc_term_matrix = compute_bag_of_words(df_tweets[text])

    if do_search_best_topics:
        # search best nb of topics
        print("... Running search for best nb of topics")
        best_topics = search_nb_topics(
            dictionary=dico_words,
            corpus=doc_term_matrix,
            texts=text_tokens,
            start=2,
            limit=7,
            step=1,
            alias=alias,
        )
    else:
        best_topics = nb_topics

    # run lda model
    print(f"... Running lda with {best_topics} topics")
    lda_result, score = compute_lda(
        dictionary=dico_words,
        corpus=doc_term_matrix,
        texts=text_tokens,
        num_topics=best_topics,
    )

    print(f"... Running lda visualization")
    print(f"... Running lda visualization")
    vis = gensimvis.prepare(
        topic_model=lda_result, corpus=doc_term_matrix, dictionary=dico_words
    )
    pyLDAvis.enable_notebook()
    # pyLDAvis.display(vis)
    pyLDAvis.save_html(vis, f"output/img/lda_{alias}_{best_topics}topics.html")

    print(f"... Running dominant topics")
    df_dominant_topics = _format_topics_sentences(
        lda_model=lda_result, corpus=doc_term_matrix, texts=text_tokens
    )

    df_dominant_topics_ = df_tweets.join(df_dominant_topics, how="inner")
    df_dominant_topics_ = df_dominant_topics_.set_index("tweet_id")

    df_dominant_topics_.to_csv(
        f"output/dominant_topics_{alias}_{best_topics}topics.csv", sep=";"
    )

    print("... Graph topics and keywords")
    graph_topics(lda_result, df_dominant_topics_, alias)

    print("... Graph word cloud for each topic")
    compute_word_cloud(df_dominant_topics_, text, alias)

    end_run = time.time()

    running_time = (end_run - start_run) / 60

    print(f"\n Total running time: {running_time} minutes")

    return df_dominant_topics_
