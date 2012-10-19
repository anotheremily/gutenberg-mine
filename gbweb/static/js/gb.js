var sigInst = null,
    isRunning = false,
	hoverMode = false,
    init = null,
    removeNodeByLabel = null,
    removePct = null;

/**
 * Initializes SigmaJS functionality.
 */
init = function() {
    // Instantiate sigma.js and customize rendering :
    sigInst = sigma.init(document.getElementById('gb_graph')).drawingProperties({
        defaultLabelColor: '#fff',
        font: 'garamond,serif',
        defaultLabelSize: 12,
        defaultLabelBGColor: '#eee',
        defaultLabelHoverColor: '#181818',
        labelThreshold: 6,
        defaultEdgeType: 'curve'
    }).graphProperties({
        minNodeSize: 0.5,
        maxNodeSize: 10,
        minEdgeSize: 0.1,
        maxEdgeSize: 1
    }).mouseProperties({
        maxRatio: 32,
        zoomDelta: 0.02
    });

    // Parse a GEXF encoded file to fill the graph (requires "sigma.parseGexf.js" to be included)
    sigInst.parseGexf('static/data/gb-sm.gexf');

    // Draw the graph :
    sigInst.draw();

    addListeners();
};

/**
 *
 */
removeNodeByLabel = function(label) {
    sigInst.iterNodes(function(n) {
        if (n['label'] == label) {
            removeNode(n['id']);
        }
    });
};

/**
 *
 */
removePct = function(pct) {
    ids = [];
    sigInst.iterNodes(function(n) {
        if (Math.random() * 100 < pct) {
            //removeNode(n['id']);
            ids.push(n['id']);
        }
    });
    removeNode(ids);
};

/**
 *
 */
removeNode = function(id) {
    sigInst.dropNode(id);
};

/**
 * Listeners
 */
addListeners = function() {
    /**
     * Toggles movement on and off
     */
    document.getElementById('toggle-layout').addEventListener('click', function() {
        if (isRunning) {
            isRunning = false;
            sigInst.stopForceAtlas2();
            document.getElementById('toggle-layout').childNodes[0].nodeValue = 'Activate Layout Organizer';
        } else {
            isRunning = true;
            sigInst.startForceAtlas2();
            document.getElementById('toggle-layout').childNodes[0].nodeValue = 'Dectivate Layout Organizer';
        }
    }, true);

	/**
	 * Toggles hover functionality on and off
	 */
	document.getElementById('toggle-hover').addEventListener('click', function() {
        if (hoverMode) {
			hoverMode = false;
            document.getElementById('toggle-hover').childNodes[0].nodeValue = 'Activate Hover Mode';
        } else {
			hoverMode = true;
			document.getElementById('toggle-hover').childNodes[0].nodeValue = 'Dectivate Hover Mode';
        }
    }, true);

    /** 
     * Refocuses the graph
     */
    document.getElementById('rescale-graph').addEventListener('click', function() {
        sigInst.position(0, 0, 1).draw();
    }, true);

    /**
     * Removes orphans from the graph
     */
    document.getElementById('remove-orphans').addEventListener('click', function() {
        console.log('Removing orphans');
        sigInst.dropOrphans();
        console.log('Done removing orphans');
        sigInst.position(0, 0, 1).draw();
    }, true);

    /**
     * Removes a specific label from the graph
     */
    document.getElementById('remove-label').addEventListener('click', function() {
        var label = document.getElementById('remove-label-text').value;
        if (label) {
            console.log('Removing "' + label + '"');
            sigInst.dropNodeByLabel(label);
            console.log('Done removing node');
        }
        sigInst.position(0, 0, 1).draw();

    }, true);

    /**
     * Removes random nodes from the graph
     */
    rems = document.getElementsByClassName('remove-nodes');
    for (i in rems) {
        if (rems[i] && rems[i].getAttribute && rems[i].getAttribute('data-pct')) {

            var pct = rems[i].getAttribute('data-pct');

            rems[i].addEventListener('click', function() {
                console.log('Removing ' + this.getAttribute('data-pct') + '% of nodes');
                removePct(this.getAttribute('data-pct'));
                console.log('Done removing nodes');
                sigInst.position(0, 0, 1).draw();
            }, true);
        }
    }

    /**
     * Displays a subset of the graph
     */
    document.getElementById('graph-start').addEventListener('click', function() {
        var label = document.getElementById('graph-start-text').value,
            depth = document.getElementById('graph-start-depth').value

            console.log('Generating subset of graph starting with "' + label + '" and diving to a depth of ' + depth + ' links');

        sigInst.subGraph(label, depth);

        console.log('Done generating subgraph');

        sigInst.position(0, 0, 1).draw();
    }, true);

    /**
     * Toggle data set
     */
    rems = document.getElementsByClassName('toggle-data');
    for (i in rems) {
        if (rems[i] && rems[i].getAttribute && rems[i].getAttribute('data-dataset')) {

            var dataset = rems[i].getAttribute('data-dataset'),
                datamap = {
                    'small-data-set': 'gb-sm.gexf',
                    'medium-data-set': 'gb-med.gexf',
                    'large-data-set': 'gb-lg.gexf',
                    'full-data-set': 'gb-full.gexf'
                };

            rems[i].addEventListener('click', function() {
                console.log('Switching to ' + this.getAttribute('data-dataset'));

                /**
                 * Clear graph
                 * Parse new data file
                 * Redraw
                 */
                sigInst.emptyGraph();
                sigInst.parseGexf('static/data/' + datamap[this.getAttribute('data-dataset')] || datamap['small-data-set']);
                sigInst.draw();

                console.log('Done switching dataset');
                sigInst.position(0, 0, 1).draw();
            }, true);
        }
    }

    $('ul.technologies a').each(function() {
        $(this).bind('click', function() {
            var newWindow = window.open($(this).attr('href'));
            return false;
        });
    });

    sigInst.bind('overnodes', function(event) {
		if (hoverMode) {
			var nodes = event.content,
				neighbors = {};

			sigInst.iterEdges(function(e) {
				if (nodes.indexOf(e.source) >= 0 || nodes.indexOf(e.target) >= 0) {
					neighbors[e.source] = 1;
					neighbors[e.target] = 1;
				}
			}).iterNodes(function(n) {
				if (!neighbors[n.id]) {
					n.hidden = 1;
				} else {
					n.hidden = 0;
				}
			}).draw(2, 2, 2);
		}
    }).bind('outnodes', function() {
		if (hoverMode) {
			sigInst.iterEdges(function(e) {
				e.hidden = 0;
			}).iterNodes(function(n) {
				n.hidden = 0;
			}).draw(2, 2, 2);
		}
    });
};

/**
 * on dom ready, run init
 */
if (document.addEventListener) {
    document.addEventListener("DOMContentLoaded", init, false);
} else {
    window.onload = init;
}
