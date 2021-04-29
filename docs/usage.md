# Spraygen Usage

Spraygen comes with a lot of different options for generating unique targeting lists for password spraying. These options provide robustness but can be overwhelming. Generating with `all` options is completable, but takes quite a long time, and it is unlikely that it will be practically useful in a real spray unless you have *alot* of time. These more robust options are more useful for generating lists for offline cracking and are included just because "we can".

Spraygen can generate some powerful lists, but keep in mind the more complexity you add, the longer generation will take (multi threading can only help so much!). Be sure you use the right switches and options for the job. For example:
    - Need to easily generate a list of all 10 character passwords in a given keyspace for offline cracking? You can do that, but it'll take some time. 
    - If you need to spray 10 character passwords, try picking from a smaller custom list of common 6-10 character passwords and mixing up flags to get more permutations of those passwords to increase your success rate. This will generate much more quickly and be much more useful in a spray attack.

While it is high recommended you experiment with the different options to make the most of the tool, below there are few common options that have proven to be highly effective and quick to generate.

# Custom
Generate limited custom separators and attributes with some of the most common. Escape "!" to avoid weird CLI parsing. Example usage with `password` permutation type:
`python3 spraygen.py --mode custom -s ".,_" -a "\!,\!\!,#,##,1,123,1234" --type password -o spray_list.txt`

Example with custom word list:
`python3 spraygen.py --mode custom -s ".,_" -a "\!,\!\!,#,##,1,123,1234" --type custom -w wordlist.txt -o spray_list.txt`


# Seasons and Months
Generate seasons and months with all attribute and separator types, defaults to current year. Try mixing up with the `year_start` and `year_end` parameters if you target has a weak rotation policy:
`python3 spraygen.py --mode all --type seasons months -o spray_list.txt`