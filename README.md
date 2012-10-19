Gutenberg Mine
==============

This project was an experiment in visualizing the relationship between words.

A subset of the texts hosted by Project Gutenberg were downloaded for this project. These books were parsed and imported into a Redis datastore. Each work was represented as a graph with nodes and edges. Each connection between two adjacent words was added as an edge, with another data structure, a super-edge, included the number of instances of a particular connection across all imported works.

GEXF (the Graph Exchange XML Format) provided a bridge between the graph stored in Redis and the front end of the application. A Python script was written to export GEXF formatted subsets of the data for analysis. The data was imported and displayed with SigmaJS on a 2D canvas.

The primary text used for analysis is the King James translation of the Bible. The small, medium, and large datasets are the first 100, 500, and 2,500 unique words (tokens/nodes) from the text. For most operations, the small or medium datasets are recommended as many operations will be slow on the large and full datasets. The small dataset includes up to Genesis 1:16 and the medium dataset includes up to Genesis 5:4. The large dataset includes text up to Genesis 46:16. The full dataset includes the entire text of the Bible.

The next phase of the project will involve including additional texts for comparison.

This tool allows you to visualize the relationships between words.


http://gutenberg-mine.appspot.com/
