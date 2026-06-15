First of all make the substring valid, it should have enough needed characters, we keep count of our window and freqency by having window hash_map, after we made the substring valid we store the best length, best left and right indices. Then shrink the windown from the left. 

At the end return the best values if found, empty string otherwise.