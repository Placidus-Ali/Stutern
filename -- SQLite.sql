-- SQLite
 /* Who is the most decorated celebrity */
 SELECT
 name,
    MAX(award)
 FROM
    celebrity;

/* Who is the oldest celebrity */
 SELECT
 name,
    MAX(age)
 FROM
    celebrity;

/* Which celebrity has been in the industry the longest */
SELECT
 name,
    MIN(years_in_industry)
 FROM
    celebrity;

/* Which celebrity has the least number of albums */
 SELECT
 name,
    MIN(num_albums)
 FROM
    celebrity;

/* What is the most popular genre of music amongst all celebrities in the dataset */
SELECT
name,
    MAX(award), (num_albums)
FROM
    celebrity;

