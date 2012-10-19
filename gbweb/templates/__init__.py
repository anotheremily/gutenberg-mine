from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def about():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<section class="explanation">\n'])
    extend_([u'        <h2>About</h2>\n'])
    extend_([u'        <p>A subset of the texts hosted by Project Gutenberg were downloaded for this project. These books were parsed and imported \n'])
    extend_([u'        into a Redis datastore. Each work was represented as a graph with nodes and edges. Each connection between two adjacent words \n'])
    extend_([u'        was added as an edge, with another data structure, a super-edge, included the number of instances of a particular connection \n'])
    extend_([u'        across all imported works.</p>\n'])
    extend_([u'\n'])
    extend_([u'        <p>GEXF (the Graph Exchange XML Format) provided a bridge between the graph stored in Redis and the front end of the application.\n'])
    extend_([u'        A Python script was written to export GEXF formatted subsets of the data for analysis. The data was imported and displayed with \n'])
    extend_([u'        SigmaJS on a 2D canvas.</p>\n'])
    extend_([u'\n'])
    extend_([u'        <p>The primary text used for analysis is the King James translation of the Bible. The small, medium, and large datasets are the \n'])
    extend_([u'        first <em>100</em>, <em>500</em>, and <em>2,500</em> unique words (tokens/nodes) from the text. For most operations, the small \n'])
    extend_([u'        or medium datasets are recommended as many operations will be slow on the large and full datasets. The small dataset includes up\n'])
    extend_([u'        to Genesis 1:16 and the medium dataset includes up to Genesis 5:4. The large dataset includes text up to Genesis 46:16. The full \n'])
    extend_([u'        dataset includes the entire text of the Bible.</p>\n'])
    extend_([u'\n'])
    extend_([u'        <p>The next phase of the project will involve including additional texts for comparison.</p>\n'])
    extend_([u'\n'])
    extend_([u'        <p>This tool allows you to visualize the relationships between words.</p>\n'])
    extend_([u'\n'])
    extend_([u'        <h2>Technology</h2>\n'])
    extend_([u'        <ul class="technologies">\n'])
    extend_([u'                <li>Front End\n'])
    extend_([u'                        <ul>\n'])
    extend_([u'                                <li><a href="http://www.html5rocks.com/en/">HTML5</a></li>\n'])
    extend_([u'                                <li><a href="http://javascript.crockford.com/">JavaScript</a></li>\n'])
    extend_([u'                                <li><a href="http://sigmajs.org/">SigmaJS</a> (with GEXF Plugin) (<a href="https://github.com/zyoung/sigma.js">custom fork</a> used for this project)</li>\n'])
    extend_([u'                        </ul>\n'])
    extend_([u'                </li>\n'])
    extend_([u'                <li>Back End\n'])
    extend_([u'                        <ul>\n'])
    extend_([u'                                <li><a href="http://redis.io/">Redis</a></li>\n'])
    extend_([u'                                <li><a href="http://www.python.org/">Python</a></li>\n'])
    extend_([u'                                <li><a href="http://gexf.net/format/">GEXF</a> (Graph Exchange XML Format)</li>\n'])
    extend_([u'                        </ul>\n'])
    extend_([u'                </li>\n'])
    extend_([u'        </ul>\n'])
    extend_([u'</section>\n'])

    return self

about = CompiledTemplate(about, 'templates/about.html')
join_ = about._join; escape_ = about._escape

# coding: utf-8
def desktop (content, title):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<!doctype html>\n'])
    extend_([u'<html>\n'])
    extend_([u'<head>\n'])
    extend_([u'        <title>', escape_(title, True), u' - Gutenberg Mine</title>\n'])
    extend_([u'        <link rel="stylesheet" type="text/css" href="static/css/gb.css" />\n'])
    extend_([u'        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.8/jquery.min.js"></script>\n'])
    extend_([u'        <script type="text/javascript">\n'])
    extend_([u'                var _gaq = _gaq || [];\n'])
    extend_([u"                _gaq.push(['_setAccount', 'UA-93196-17']);\n"])
    extend_([u"                _gaq.push(['_trackPageview']);\n"])
    extend_([u'                (function() {\n'])
    extend_([u"                        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;\n"])
    extend_([u"                        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';\n"])
    extend_([u"                        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);\n"])
    extend_([u'                })();\n'])
    extend_([u'        </script>\n'])
    extend_([u'</head>\n'])
    extend_([u'<body>\n'])
    extend_([u'        <header>\n'])
    extend_([u'                <h1>Gutenberg Mine</h1>\n'])
    extend_([u'                <p>\n'])
    extend_([u'                        <a href="/">home</a> | \n'])
    extend_([u'                        <a href="/about">about</a> |\n'])
    extend_([u'                        <a href="/visualizer">visualizer</a> |\n'])
    extend_([u'                        <a href="/examples">examples</a>\n'])
    extend_([u'                </p>\n'])
    extend_([u'        </header>\n'])
    extend_([u'\n'])
    extend_([u'        ', escape_(content, False), u'\n'])
    extend_([u'\n'])
    extend_([u'        <footer>\n'])
    extend_([u'                <p>2012 - Developed by Zach Young (<a href="mailto:me[at]zachyoung.org">me[at]zachyoung[dot]org</a>)</p>\n'])
    extend_([u'        </footer>\n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])

    return self

desktop = CompiledTemplate(desktop, 'templates/desktop.html')
join_ = desktop._join; escape_ = desktop._escape

# coding: utf-8
def examples():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<section class="examples">\n'])
    extend_([u'        <h2>Examples of Use</h2>\n'])
    extend_([u'\n'])
    extend_([u'        <h3>First 100 Nodes</h3>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/000-small.png"/>\n'])
    extend_([u'\n'])
    extend_([u'        <h3>Sections of the Full Graph</h3>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/009-full.png"/>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/001-full.png"/>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/002-full.png"/>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/003-full.png"/>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/004-full.png"/>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/005-full.png"/>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/006-full.png"/>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/007-full.png"/>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/008-full.png"/>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/010-full.png"/>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/011-full.png"/>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/012-full.png"/>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/013-full.png"/>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/014-full.png"/>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/015-full.png"/>\n'])
    extend_([u'\n'])
    extend_([u'        <h3>Start/Stop Layout Organizer</h3>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/016-full.png"/>\n'])
    extend_([u'\n'])
    extend_([u'        <h3>Removal of Random Nodes</h3>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/017-full.png"/>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/018-full.png"/>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/019-full.png"/>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/020-full-2.png"/>\n'])
    extend_([u'\n'])
    extend_([u'        <h2>Start Point: Begat, Depth: 2</h2>   \n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/021-small-begat.png"/>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/022-medium-begat.png"/>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/023-large-begat.png"/>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/024-full-begat.png"/>\n'])
    extend_([u'\n'])
    extend_([u'        <h2>Start Point: Moses, Depth: 2</h2>   \n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/025-small-moses.png"/>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/026-medium-moses.png"/>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/027-large-moses.png"/>\n'])
    extend_([u'        <img src="http://dl.dropbox.com/u/7942138/gae_gbmine/img/screenshots/028-full-moses.png"/>\n'])
    extend_([u'</section>\n'])

    return self

examples = CompiledTemplate(examples, 'templates/examples.html')
join_ = examples._join; escape_ = examples._escape

# coding: utf-8
def index():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<section class="introduction">\n'])
    extend_([u'        <h2>Welcome</h2>\n'])
    extend_([u'        <p>This project is a visualization of the connections between words in the English language.</p>\n'])
    extend_([u'        <p><a href="/visualizer">Try</a> the visualization tool or <a href="/examples">view</a> examples.</p>\n'])
    extend_([u'</section>\n'])

    return self

index = CompiledTemplate(index, 'templates/index.html')
join_ = index._join; escape_ = index._escape

# coding: utf-8
def visualizer():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<section class="settings">\n'])
    extend_([u'        <h2>Settings</h2>\n'])
    extend_([u'        <div>\n'])
    extend_([u'                <h3>Switch Dataset</h3>\n'])
    extend_([u'                <button class="toggle-data" data-dataset="small-data-set">Small (100 Nodes, 2,488 Edges)</button>\n'])
    extend_([u'                <button class="toggle-data" data-dataset="medium-data-set">Medium (500 Nodes, 24,207 Edges)</button>\n'])
    extend_([u'                <button class="toggle-data" data-dataset="large-data-set">Large (2,500 Nodes, 79,691 Edges)</button>\n'])
    extend_([u'                <button class="toggle-data" data-dataset="full-data-set">Full (13,904 Nodes, 166,427 Edges)</button>\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <div>\n'])
    extend_([u'                <h3>Layout</h3>\n'])
    extend_([u'                <button id="toggle-layout">Activate Layout Organizer</button>\n'])
    extend_([u'                <button id="toggle-hover">Activate Hover Mode</button>\n'])
    extend_([u'                <button id="rescale-graph">Refresh Graph</button>\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <div>\n'])
    extend_([u'                <h3>Node Removal:</h3>\n'])
    extend_([u'                <div>\n'])
    extend_([u'                        <button class="remove-nodes" data-pct="25">Remove 25% of Nodes</button>\n'])
    extend_([u'                        <button class="remove-nodes" data-pct="50">Remove 50% of Nodes</button>\n'])
    extend_([u'                        <button class="remove-nodes" data-pct="75">Remove 75% of Nodes</button>\n'])
    extend_([u'                        <button class="remove-nodes" data-pct="95">Remove 95% of Nodes</button>\n'])
    extend_([u'                        <button id="remove-orphans" class="remove-orphans">Remove Orphans (Nodes without Edges)</button>\n'])
    extend_([u'                </div>\n'])
    extend_([u'                <div>\n'])
    extend_([u'                        <span>Node to remove: </span>\n'])
    extend_([u'                        <input type="text" name="remove-label-text" id="remove-label-text" value=""/>\n'])
    extend_([u'                        <button id="remove-label">Remove Node</button>\n'])
    extend_([u'                </div>\n'])
    extend_([u'                <div>\n'])
    extend_([u'                        <h3>Graph Subsets</h3>\n'])
    extend_([u'                        <span>Start point:</span>\n'])
    extend_([u'                        <input type="text" name="graph-start-text" id="graph-start-text" value=""/>\n'])
    extend_([u'                        <span>Depth:</span>\n'])
    extend_([u'                        <select name="graph-start-depth" id="graph-start-depth">\n'])
    extend_([u'                                <option value="1">1\n'])
    extend_([u'                                <option value="2">2\n'])
    extend_([u'                                <option value="3">3\n'])
    extend_([u'                                <option value="4">4\n'])
    extend_([u'                                <option value="5">5\n'])
    extend_([u'                                <option value="6">6\n'])
    extend_([u'                                <option value="7">7\n'])
    extend_([u'                                <option value="8">8\n'])
    extend_([u'                                <option value="9">9\n'])
    extend_([u'                                <option value="10">10\n'])
    extend_([u'                        </select>\n'])
    extend_([u'                        <button id="graph-start">Filter Graph</button>\n'])
    extend_([u'                </div>\n'])
    extend_([u'\n'])
    extend_([u'                <p><em>Note that some functions may execute slowly on a large graph.</em></p>\n'])
    extend_([u'        </div>\n'])
    extend_([u'</section>\n'])
    extend_([u'\n'])
    extend_([u'<section class="graph_holder">\n'])
    extend_([u'        <div id="gb_graph" class="graph"></div> \n'])
    extend_([u'</section>\n'])
    extend_([u'\n'])
    extend_([u'<script src="static/js/underscore.min.js"></script>\n'])
    extend_([u'<script src="static/js/sigma.concat.js"></script>\n'])
    extend_([u'<script src="static/js/gb.js"></script>\n'])
    extend_([u'\n'])

    return self

visualizer = CompiledTemplate(visualizer, 'templates/visualizer.html')
join_ = visualizer._join; escape_ = visualizer._escape

