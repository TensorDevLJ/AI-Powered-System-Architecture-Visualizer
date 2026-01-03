import networkx as nx

class LayoutEngine:
    """Step 8: Layout Engine - Position components on canvas"""
    
    def __init__(self):
        self.canvas_width = 1200
        self.canvas_height = 800
        self.margin = 100
        self.layer_spacing = 250
        self.node_spacing = 150
    
    def calculate_layout(self, visual_data):
        """
        Calculate positions for all components using layered layout
        """
        components = visual_data['components']
        relationships = visual_data['relationships']
        
        # Build dependency graph
        graph = self._build_graph(components, relationships)
        
        # Calculate layers (topological sort)
        layers = self._calculate_layers(graph, relationships)
        
        # Assign positions
        positions = self._assign_positions(layers, components)
        
        return {
            'components': components,
            'relationships': relationships,
            'positions': positions,
            'canvas_width': self.canvas_width,
            'canvas_height': self.canvas_height
        }
    
    def _build_graph(self, components, relationships):
        """
        Build directed graph from relationships
        """
        graph = nx.DiGraph()
        
        # Add all components as nodes
        for comp in components:
            graph.add_node(comp['name'])
        
        # Add edges
        for rel in relationships:
            if rel['from'] in graph and rel['to'] in graph:
                graph.add_edge(rel['from'], rel['to'])
        
        return graph
    
    def _calculate_layers(self, graph, relationships):
        """
        Assign components to layers using topological sort
        """
        try:
            # Try topological sort (works for DAGs)
            topo_order = list(nx.topological_sort(graph))
            
            # Assign layers based on longest path from source
            layers = {}
            for node in topo_order:
                # Find max layer of predecessors
                predecessors = list(graph.predecessors(node))
                if not predecessors:
                    layers[node] = 0
                else:
                    layers[node] = max(layers.get(pred, 0) for pred in predecessors) + 1
            
        except nx.NetworkXError:
            # Graph has cycles, use simple heuristic
            layers = self._simple_layering(graph)
        
        # Group by layer
        layer_groups = {}
        for node, layer in layers.items():
            if layer not in layer_groups:
                layer_groups[layer] = []
            layer_groups[layer].append(node)
        
        return layer_groups
    
    def _simple_layering(self, graph):
        """
        Simple layering for cyclic graphs
        """
        layers = {}
        nodes = list(graph.nodes())
        
        # Start nodes (no predecessors or few)
        for node in nodes:
            in_degree = graph.in_degree(node)
            if in_degree == 0:
                layers[node] = 0
        
        # Assign remaining nodes
        layer = 1
        assigned = set(layers.keys())
        
        while len(assigned) < len(nodes):
            for node in nodes:
                if node in assigned:
                    continue
                
                predecessors = list(graph.predecessors(node))
                if not predecessors or any(p in assigned for p in predecessors):
                    layers[node] = layer
                    assigned.add(node)
            
            layer += 1
            if layer > 10:  # Safety limit
                break
        
        # Assign any remaining
        for node in nodes:
            if node not in layers:
                layers[node] = layer
        
        return layers
    
    def _assign_positions(self, layer_groups, components):
        """
        Assign x, y coordinates to components
        """
        positions = {}
        
        num_layers = len(layer_groups)
        
        for layer_idx, nodes in layer_groups.items():
            num_nodes = len(nodes)
            
            # Calculate x position (layer)
            x = self.margin + (layer_idx * self.layer_spacing)
            
            # Calculate y positions (center vertically)
            total_height = (num_nodes - 1) * self.node_spacing
            start_y = (self.canvas_height - total_height) / 2
            
            for i, node in enumerate(nodes):
                y = start_y + (i * self.node_spacing)
                positions[node] = (int(x), int(y))
        
        return positions
