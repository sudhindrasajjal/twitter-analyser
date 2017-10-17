"""Analyser."""
import json
import pandas as pd
import re


def word_in_text(word, text):
    """Find word in tweet."""
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False


tweets_data_path = 'tweets.txt'
tweets_data = []
raw_data = []
metoo_count = 0
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        if 'RT @' not in tweet['text']:
            tweets_data.append(tweet)
        if tweet['text'].lower() == "#metoo":
            metoo_count += 1
        raw_data.append(tweet)
    except:
        continue

tweets = pd.DataFrame()

tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['favorite_count'] = map(lambda tweet: tweet['favorite_count'], tweets_data)
tweets['retweet_count'] = map(lambda tweet: tweet['retweet_count'], tweets_data)

# Victim
tweets['i_was'] = tweets['text'].apply(lambda tweet: word_in_text('I was', tweet))
tweets['happened'] = tweets['text'].apply(lambda tweet: word_in_text('happened', tweet))
tweets['victim'] = tweets['text'].apply(lambda tweet: word_in_text('victim', tweet))
tweets['cat'] = tweets['text'].apply(lambda tweet: word_in_text('catcalled', tweet))
tweets['quiet'] = tweets['text'].apply(lambda tweet: word_in_text('kept quiet', tweet))
tweets['tell'] = tweets['text'].apply(lambda tweet: word_in_text('didn\'t tell', tweet))
tweets['domestic'] = tweets['text'].apply(lambda tweet: word_in_text('domestic', tweet) and ( word_in_text('violence', tweet) or word_in_text('abuse', tweet)))
tweets['abuse'] = tweets['text'].apply(lambda tweet: word_in_text('abuse', tweet))

# place related
tweets['boss'] = tweets['text'].apply(lambda tweet: word_in_text('boss', tweet))
tweets['colleague'] = tweets['text'].apply(lambda tweet: word_in_text('colleague', tweet))
tweets['office'] = tweets['text'].apply(lambda tweet: word_in_text('office', tweet))
tweets['work'] = tweets['text'].apply(lambda tweet: word_in_text('work', tweet))
tweets['school'] = tweets['text'].apply(lambda tweet: word_in_text('school', tweet))
tweets['college'] = tweets['text'].apply(lambda tweet: word_in_text('college', tweet))
tweets['uni'] = tweets['text'].apply(lambda tweet: word_in_text('university', tweet))

# Age
tweets['teen'] = tweets['text'].apply(lambda tweet: word_in_text('teen', tweet))
tweets['kid'] = tweets['text'].apply(lambda tweet: word_in_text('kid', tweet))
tweets['child'] = tweets['text'].apply(lambda tweet: word_in_text('child', tweet))
tweets['small'] = tweets['text'].apply(lambda tweet: word_in_text('was small', tweet))

# Support
tweets['speak'] = tweets['text'].apply(lambda tweet: word_in_text('speak up', tweet))
tweets['support'] = tweets['text'].apply(lambda tweet: word_in_text('support', tweet))
tweets['awareness'] = tweets['text'].apply(lambda tweet: word_in_text('aware', tweet))
tweets['educate'] = tweets['text'].apply(lambda tweet: word_in_text('educate', tweet))
tweets['teach'] = tweets['text'].apply(lambda tweet: word_in_text('teach', tweet))
tweets['with'] = tweets['text'].apply(lambda tweet: word_in_text('with you', tweet))
tweets['there'] = tweets['text'].apply(lambda tweet: word_in_text('for you', tweet))
tweets['stand'] = tweets['text'].apply(lambda tweet: word_in_text('stand', tweet))
tweets['raise'] = tweets['text'].apply(lambda tweet: word_in_text('raise', tweet))
tweets['rise'] = tweets['text'].apply(lambda tweet: word_in_text('rise', tweet))

# Counter arguments
tweets['not_all_men'] = tweets['text'].apply(lambda tweet: word_in_text('men', tweet) and word_in_text('not', tweet) and word_in_text('all', tweet))

# Forms of abuse
tweets['touch'] = tweets['text'].apply(lambda tweet: word_in_text('touch', tweet))
tweets['grope'] = tweets['text'].apply(lambda tweet: word_in_text('grope', tweet))
tweets['stare'] = tweets['text'].apply(lambda tweet: word_in_text('stare', tweet))
tweets['molest'] = tweets['text'].apply(lambda tweet: word_in_text('molest', tweet))
tweets['sexual'] = tweets['text'].apply(lambda tweet: word_in_text('sexually abused', tweet))
tweets['dress'] = tweets['text'].apply(lambda tweet: word_in_text('dress', tweet))
tweets['drunk'] = tweets['text'].apply(lambda tweet: word_in_text('drunk', tweet) or word_in_text('drink', tweet))

# General stats
total = len(raw_data)
total_rt = len(tweets['text'])
total_favs = tweets['favorite_count'].sum()
total_retweets = tweets['retweet_count'].sum()

# Victim Counts
i_count = tweets['i_was'].value_counts()[True] | 0
h_count = tweets['happened'].value_counts()[True] | 0
v_count = tweets['victim'].value_counts()[True] | 0
c_count = tweets['cat'].value_counts()[True] | 0
d_count = tweets['domestic'].value_counts()[True] | 0
q_count = tweets['quiet'].value_counts()[True] | 0
t_count = tweets['tell'].value_counts()[True] | 0
a_count = tweets['abuse'].value_counts()[True] | 0

# Place related
b_count = tweets['boss'].value_counts()[True] | 0
co_count = tweets['colleague'].value_counts()[True] | 0
o_count = tweets['office'].value_counts()[True] | 0
w_count = tweets['work'].value_counts()[True] | 0
col_count = tweets['college'].value_counts()[True] | 0
uni_count = tweets['uni'].value_counts()[True] | 0
office_total = b_count + co_count + o_count + w_count
school_count = tweets['school'].value_counts()[True] | 0

# Age counts
t_count = tweets['teen'].value_counts()[True] | 0
k_count = tweets['kid'].value_counts()[True] | 0
ch_count = tweets['child'].value_counts()[True] | 0
# sm_count = tweets['small'].value_counts()[True] | 0
kid_total = k_count + ch_count

# Abuse counts
touch_count = tweets['touch'].value_counts()[True] | 0
grope_count = tweets['grope'].value_counts()[True] | 0
stare_count = tweets['stare'].value_counts()[True] | 0
molest_count = tweets['molest'].value_counts()[True] | 0
dress_count = tweets['dress'].value_counts()[True] | 0
drunk_count = tweets['drunk'].value_counts()[True] | 0
sex_count = tweets['sexual'].value_counts()[True] | 0

# Support counts
sp_count = tweets['speak'].value_counts()[True] | 0
su_count = tweets['support'].value_counts()[True] | 0
aw_count = tweets['awareness'].value_counts()[True] | 0
ed_count = tweets['educate'].value_counts()[True] | 0
te_count = tweets['teach'].value_counts()[True] | 0
wi_count = tweets['with'].value_counts()[True] | 0
th_count = tweets['there'].value_counts()[True] | 0
st_count = tweets['stand'].value_counts()[True] | 0
ra_count = tweets['raise'].value_counts()[True] | 0
ri_count = tweets['rise'].value_counts()[True] | 0

nam_count = tweets['not_all_men'].value_counts()[True] | 0

support_total = sp_count + su_count + aw_count + ed_count + te_count + wi_count + th_count + st_count + ra_count + ri_count
victim_total = i_count + h_count + v_count + d_count + q_count + t_count + a_count + sex_count

print "Total tweets collected so far: " + str(total)
print "Total tweets after removing RTs: " + str(total_rt)
print "Only #metoo: " + str(metoo_count)
print "Have been a victim: " + str(victim_total)
print "At workplace: " + str(office_total)
print "Teenagers: " + str(t_count + col_count + uni_count)
print "As kids: " + str(kid_total + school_count)
print "Touched: " + str(touch_count)
print "Groped: " + str(grope_count)
print "Stared at: " + str(stare_count)
print "Molested: " + str(molest_count)
print "Dress: " + str(dress_count)
print "Drunk: " + str(drunk_count)
print "Sexually Abused: " + str(sex_count)
print "Catcalled: " + str(c_count)
print "Domestic Abuse: " + str(d_count)
print "Support: " + str(support_total)
print "Not all men: " + str(nam_count)
