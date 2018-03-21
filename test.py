
# coding: utf-8

"""Count words."""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    
    # TODO: Return the top n most frequent words.
    splited=s.split()
    listed=[]
    for i in set(splited):    
        listed.append((i,splited.count(i)))
    sort_0=sorted(listed,key=lambda x:x[0])
    sort_1=sorted(sort_0,key=lambda x:x[1],reverse=True)
    top_n=sort_1[:n]
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print(count_words("cat bat mat cat bat cat", 3))
    print(count_words("betty bought a bit of butter but the butter was bitter", 3))


if __name__ == '__main__':
    test_run()
    

